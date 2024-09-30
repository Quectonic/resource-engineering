""" JSON STORAGE DESIGNS
    For the sakes of future processing (e.g. chunking), content relevance, etc. 
    Hierarchy of the scraped data would be sectioned based on heading tags (e.g. h1, h2, ...)
    Therefore the processing would include:
     -  List or bullet point items (ul --> li) would be concatenated into one single
        paragraph. 
        {
            'type': "paragraph",
            'content': "`1st li item`, `2nd li item`, ...
        }
     -  Table would be textualized
        {
            'type': "table",
            'content': " || col1 | col2 | col3 ||\n|| row1 | field1 | field2 ||\n"
        }
     -  Headings would contain content in list format
        {
            'type': "section",
            'title': "title",
            'content': []
        }
     -  Figure, gallery (specific to WikiDoc) and other media would be contained in the format
        {
            'type': "media",
            'media-source': "source of media",
            'description': "caption or description (usually from <figcaption /> or <div class="gallerytext" />)"
        }
"""


import scrapy # type: ignore 
from scrapy.linkextractors import LinkExtractor # type: ignore
from scrapy.spiders import CrawlSpider, Rule # type: ignore
from lxml import etree # type: ignore
from ..utils.DataTransformer import HtmlTableTransformer
from bs4 import BeautifulSoup # type: ignore
import re
import json


## NOTE: Might be good for future implementation for scalability
# from dataclasses import dataclass, field
# from typing import Optional, Union

# @dataclass
# class ContentItem:
#     type: str
#     level: int
#     content: str
#     section_title: Optional[str] = field(default=None)


class WikidocspiderSpider(CrawlSpider):
    
    """# 🍪 **Status: _Default_**

    Description
    -----------
        This spider crawls through the WikiDoc website and extracts medical information.
        
    """
    
    name = "wikiDocSpider"
    allowed_domains = ["wikidoc.org"]
    start_urls = [
        # "https://www.wikidoc.org/index.php/Category:Signs_and_symptoms",
        # "https://www.wikidoc.org/index.php/Category:Physical_examination",
        # "https://www.wikidoc.org/index.php/Category:Blood_tests",
        # "https://www.wikidoc.org/index.php/Drug_project_list_of_medications",
        # "https://www.wikidoc.org/index.php/Drug_project_high-priority_medications",
        
        # # Sort by study subjects
        # "https://www.wikidoc.org/index.php/Main_Page"
        
        ## TODO: ADD NODAL PAGES
        # 'https://www.wikidoc.org/index.php/DNA',
        "https://www.wikidoc.org/index.php/Sexually_transmitted_disease",
        "https://www.wikidoc.org/index.php/Heart",
        
    ]

    rules = (
        ## Example:
        #
        # Rule(
        #     LinkExtractor(
        #         allow=r'/category/',  # Follow only URLs that include '/category/'
        #         deny=r'/category/special/',  # Don't follow URLs that include '/category/special/'
        #         restrict_xpaths='//div[@class="content"]',  # Extract links only from specific parts of the page
        #         tags=['a', 'area'],  # Extract from 'a' and 'area' tags only
        #         attrs=['href'],  # Consider only 'href' attributes for URLs
        #     ),
        #     callback='parse_item',
        #     follow=True,
        # ),
        Rule(LinkExtractor(), callback="parse_item", follow=True),
    )
    
    
    ## FOR DEBUGGING PURPOSES
    custom_settings = {
        'CLOSESPIDER_ITEMCOUNT': 5,
    }
    
    ## If url ends with "_project"
    ######  do not parse --> follow links but no need for information extraction
    def parse_item(self, response):
        
        self.logger.info(f"Processing URL: {response.url}")
        
        try: 
            ## Pages restricted here will not be parsed but the link follow logic still applies
            if response.meta.get('skip_item_extraction') or response.url.endswith('Main_Page'):
                self.logger.info(f'Spider => Skipping Page: {response.url}')
                return
            
            ### NOTE: Using response.meta as an intermediate for scraping
            ## Retrieve HTML from response meta
            ## [x] 0. (HTML) content
            ## [x] 1. last-modified (date it was last modified) : date
            ## [x] 2. source (url) : string [x]
            ## [x] 3. (page) title : string [x]
            ## [x] 5. (custom) id (url-ending+last_modified date) : string
            ## [x] 6. keywords : []
            ## [x] 7. authors: []
            ## [x] 8. site-path: string
            target = response.meta['cleaned_details']
            title = target['title']
            html_target = target['content']
            last_modified = target['last-modified']
            source = target['source']
            id = target['id']
            keywords = target['keywords']
            authors = target['authors']
            site_path = target['site-path']
            categories = target['categories']
            
            ## Nothing is scraped under the 'mw-parser-output' class
            ## either it does not exist or there is nothing or only comment
            if not html_target:
                self.logger.info(f'{response.url}: No Valuable Content Detected, but following links in the page')
                return
            
            """
                -------------------------------------------------------------------------------
                 -  [x] Quaternary Cleaning ~ Filter content on relevance level: 
                     -  Last cleaning carrying out filters that were 
                        easier with BeautifulSoup
                     -  Purify content, ensuring everything is medically related
                     -  Migrating tags from 'lxml' to 'BeautifulSoup'  
                -------------------------------------------------------------------------------
            """ 
            lxml_html_target = []
            remove_mode = False
            for idx, item in enumerate(html_target):
                tmp_soup = BeautifulSoup(item, 'lxml')
                
                matcher = re.compile(r'h\d+')
                
                if (matcher.match(tmp_soup.body.contents[0].name)):
                    if (tmp_soup.find(lambda tag: tag.name \
                            and ("Further reading" in tag.text or "External links" in tag.text or "See also" in tag.text)
                        )):
                        remove_mode = True
                    else:
                        remove_mode = False
                if (not remove_mode):
                    lxml_html_target.append(tmp_soup)
            
            
            ## Final check on the content --> not empty after strip()
            lxml_html_target_str = []
            for item in lxml_html_target:
                if len(item.text.strip()) != 0:
                    lxml_html_target_str.append(item)
                    
            if len(lxml_html_target_str) == 0:
                return
            
            """
                -------------------------------------------------------------------------------
                 -  [ ] 1st Phase Transformation ~ Convert tag content into human readable text: 
                     -  'lxml_html_target':   list of BeautifulSoup tags consisting of 
                                            medically relevant texts, tables, bullet points, 
                                            figures, galleries, ...
                     -  Looping through all tags in 'lxml_html_target' and implement different
                        parsing functions according to type of tags
                -------------------------------------------------------------------------------
            """ 
            
            ## - content
            ## [x] 0. (RAW TEXT) Content: [{}]
            ##          0.1. section
            ##              0.1.1 text
            ## - Metadata types
            ## [x] 1. last-modified (date it was last modified) : date
            ## [x] 2. source (url) : string [x]
            ## [x] 3. (page) title : string [x]
            ## [x] 5. (custom) id (url-ending+last_modified date) : string
            ## [x] 6. keywords : []
            ## [x] 7. authors: []
            ## [x] 8. categories : [] 
            item = {
                'content': lxml_html_target_str, 
                'title': title,
                'source': response.url,
                'categories': categories,
                'keywords': keywords,
                'id': id,
                'last-modified': last_modified.strftime('%Y-%m-%d'),
                'authors': authors,
            }
            
            self.logger.info(f"Extracted Content from {response.url}: {json.dumps(item, indent=4)}")
            
            
            return item
        except Exception as error:
            self.logger.error(f'Unknown Error Encountered, {error}')
            return {}

