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


import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from lxml import etree
from ..utils.DataTransformer import HtmlTableTransformer
from bs4 import BeautifulSoup
import re


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
        
        
        
        "https://www.wikidoc.org/index.php/Sexually_transmitted_disease"
    ]
    
    visited_urls = set()

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
    
    custom_settings = {
        'CLOSESPIDER_ITEMCOUNT': 5,
    }

    
    ## If url ends with "_project"
    ######  do not parse --> follow links but no need for information extraction
    def parse_item(self, response):
        try: 
            ## Pages restricted here will not be parsed but the link follow logic still applies
            if response.meta.get('skip_item_extraction'):
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
            ## [ ] 0. (RAW TEXT) Content: [{}]
            ##          0.1. section
            ##              0.1.1 text
            ## - Metadata types
            ## [ ] 1. last-modified (date it was last modified) : date
            ## [x] 2. source (url) : string [x]
            ## [x] 3. (page) title : string [x]
            ## [ ] 5. (custom) id (url-ending+last_modified date) : string
            ## [ ] 6. keyword : []
            ## [ ] 7. authors: []
            item = {
                'content': lxml_html_target, ## TODO: Process the tags from html_tags
                'title': title,
                'source': response.url
            }
            
            # self.logger.info(f'Parsing page: {response.url}')
            # self.logger.info(f"response meta information: {response.meta['cleaned_details']['html_content']}")
            return item
        except Exception as error:
            self.logger.error(f'Unknown Error Encountered, {error}')
            return {}
    
    def transform_bs4_html_list(self, title: str, bs_html_list: list[BeautifulSoup]):
        
        ## Integrate 'transform_bs4_html' to process each item in 'bs_html_list'
        
        ## TODO: handle h2, h3, h4, ... tags
        
        base_content_dict = {
            "type": "article",
            "level": 1,
            "title": title, 
            "content": []
        }
        raise NotImplementedError
    
    
    
    def transform_bs4_html(self, level: int, bs_html: BeautifulSoup):
        """
            ------------------------------------------------------------------------------------------------------------
                Parses the document structure and returns a hierarchical JSON-like structure.

                The function returns a ElementDict.
                
                Rules for determining the hierarchy:
                - `level` is an integer indicating where this JSON should be placed in the hierarchy
                - If the level of the current item is less than the level of the last item, it becomes a parent.
                - If the level of the current item is equal to the level of the last item, it remains at the same 
                hierarchy.
                - If the level of the current item is greater than the level of the last item, it becomes a child 
                and initiates NEW HIERARCHICAL LEVEL SPACE, needed for parent function to process next tag if 
                applicable.
                - If the level of the current item is `-1`, it indicates a tag that falls under the children content 
                of the last tag, with the hierarchical level provided as 'level' parameter

                Returns:
                    level (int): The level of the current item.
                    content_dict (dict): Dictionary shown above
            ------------------------------------------------------------------------------------------------------------
        """
        ## check type of tag
        ## allocate types and content transformation methods correspondingly
        nested_content = ""
        if (bs_html.body.contents[0].name == 'p'):
            # bs_html.body.contents[0].string => the text string inside
            
            for text in bs_html.body.strings:
                nested_content += text
            
            return -1, {
                'type': "paragraph",
                'level': level,
                'content': nested_content
            }
        elif (bs_html.body.contents[0].name == 'table'):
            ## Table HTML tag to text
            
            str_soup = str(bs_html.body.contents[0])
            
            table_text = self.parse_table(str_soup)
            
            return -1, {
                'type': 'table',
                'content': table_text
            }
        elif (bs_html.body.contents[0].name == r'h\d+'):
            ## Heading tag to text
            
            pattern = 'h(\d+)'
            level = re.findall(pattern, bs_html.body.contents[0].name, re.IGNORECASE)[0]
            
            return level, {
                'type': 'section',
                'title': ''.join(bs_html.body.contents[0].strings),
                'content': []
            }
        elif (bs_html.body.contents[0].name == 'figure'):
            return None
        elif (bs_html.body.contents[0].name == 'div'):
            ## Div Tag 
            ## Require detection of special tags like "gallery", etc.
            div = bs_html.body.contents[0]
            
            ## recursive on every child tag found
            ## TODO: work on the return / yield mechanisms
            for sub in div.contents:
                self.transform_bs4_html(sub)
        
        elif (bs_html.body.contents[0].name == 'ul'):
            
            ## TODO
            return {}
            
        else:
            
            ## TODO
            return {}
    
    ## NOTE: before use, convert table_html to string format
    def parse_table(self, table_html):
        ## table_html: <table>...</table> in string format
        table_parser = HtmlTableTransformer(table_html=table_html)
        tagged_table = table_parser.rows.toText()
        
        return tagged_table
    
    ## NOTE: before use, convert ul_html to string format
    def parse_ul(self, ul_html):
        ## ul_html: <ul> <li> ... </li> ... </ul> in string format
        pass


