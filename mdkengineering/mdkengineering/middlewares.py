# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from scrapy.http import HtmlResponse
from scrapy.exceptions import IgnoreRequest
import re
import random
from lxml.html.clean import Cleaner
from lxml import html, etree
import json
from datetime import datetime

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


class MdkengineeringSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.
        
        ## If the response contains no meaningful content but needs to be followed
        ## Examples:
        ##      1. https://www.wikidoc.org/index.php?title=category:<*>
        ##      2. https://www.wikidoc.org/index.php/The_WikiDoc_Living_Textbook_<*>
        ##      3. https://www.wikidoc.org/index.php/Category:<*>
        ##      4. https://www.wikidoc.org/index.php/
        
        if (not response.xpath('//p') or 
            'Error' in response.xpath('//head/title/text()').get() or 
            len(response.xpath('//*[@id="mw-content-text"]/div[1]/div/p[contains(., "This page does not exist.")]')) != 0
        ):
            spider.logger.info(f"MdkengineeringSpiderMiddleware: Skipping page {response.url} - No meaningful content found in this.")
            response.meta['skip_item_extraction'] = True
        
        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        spider.logger.error(f"MdkengineeringSpiderMiddleware: Exception occured when extracting html components: {exception}")

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info("MdkengineeringSpiderMiddleware: Spider opened: %s" % spider.name)

##################################################################



class RequestTracingDownloaderMiddleware:
    
    def process_request(self, request, spider):
        request_info = (
            f"Request URL: {request.url if request.url else 'None'}\n"
            f"Method: {request.method if request.method else 'None'}\n"
            f"Headers: {dict(request.headers) if request.method else 'None'}\n"
            f"Body: {request.body.decode('utf-8') if request.body else 'None'}\n"
            f"Cookies: {request.cookies if request.cookies else 'None'}\n"
            f"Meta: {request.meta if request.meta else 'None'}\n"
            f"Priority: {request.priority if request.priority else 'None'}\n"
            f"Callback: {request.callback if request.callback else 'None'}\n"
            f"Errback: {request.errback if request.errback else 'None'}\n"
            f"Dont Filter: {request.dont_filter if request.dont_filter else 'None'}\n"
            f"Flags: {request.flags if request.flags else 'None'}\n"
        )
        spider.logger.info(f"RequestTracingDownloaderMiddleware: Request Made:\n{request_info}")
        return None
        
    def process_response(self, request, response, spider):
        response_info = (
            f"Response URL: {response.url if response.url else 'None'}\n"
            f"Status Code: {response.status if response.status else 'None'}\n"
            f"Headers: {dict(response.headers) if response.headers else 'None'}\n"
            f"Body: {response.text[:500] + '...' if len(response.text) > 500 else response.text}\n"
            f"Cookies: {response.request.cookies if response.request and response.request.cookies else 'None'}\n"
            f"Meta: {response.meta if hasattr(response, 'request') and response.request and response.meta else 'None'}\n"
            f"Encoding: {response.encoding if response.encoding else 'None'}\n"
            f"Flags: {response.flags if response.flags else 'None'}\n"
            f"Request URL: {response.request.url if response.request and response.request.url else 'None'}\n"
        )
        spider.logger.info(f"RequestTracingDownloaderMiddleware: Response Object:\n{response_info}")
        return response



class RotateUserAgentDownloaderMiddleware:
    
    def __init__(self, user_agents) -> None:
        self.user_agents = user_agents

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        
        # 'cls' here refers to the CustomDownloaderMiddleware class itself.
        user_agents = crawler.settings.get('USER_AGENTS', [])
        
        # Creates an instance of the CustomDownloaderMiddleware class.
        s = cls(user_agents)
        
        # Connects the spider_opened method to the spider_opened signal.
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        
        # Returns the instance of the middleware.
        return s

    
    def process_request(self, request, spider):
        request.headers['User-Agent'] = random.choice(self.user_agents)
        spider.logger.info(f'RotateUserAgentDownloaderMiddleware: Using User-Agent: {request.headers["User-Agent"]}')
        return None
    
    
    def spider_opened(self, spider):
        spider.logger.info(f"RotateUserAgentDownloaderMiddleware: Spider opened: %s" % spider.name)




class WikiDocURLFilterDownloaderMiddleware:
    def __init__(self, deny_patterns) -> None:
        self.deny_patterns = [re.compile(pattern) for pattern in (deny_patterns or [])]
        
    @classmethod
    def from_crawler(cls, crawler):
        ## Those patterns would not be parsed nor used for link follow logics
        s = cls(deny_patterns=crawler.settings.get('DENY_URL_PATTERNS_WIKIDOC', []))
        
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s
    
    def spider_opened(self, spider):
        self.spider = spider
        spider.logger.info(f"WikiDocURLFilterDownloaderMiddleware: Spider opened: %s" % spider.name)
        
    def process_request(self, request, spider):
        if re.search(r'index\.php.*', request.url) and 'wikidoc.org' in request.url:
            return None  # Allow the request to continue
        else:
            spider.logger.info(f"WikiDocURLFilterDownloaderMiddleware: Blocked non-wikiDoc URL: {request.url}")
            raise IgnoreRequest  # Block the request by raising IgnoreRequest
        
    def process_response(self, request, response, spider):
        for pattern in self.deny_patterns:
            if pattern.search(request.url):
                spider.logger.info(f'WikiDocURLFilterDownloaderMiddleware: Blacklist URL Detected: Response Terminated from Entering Spider \nBlocked Pattern: {pattern}')
                return None
        return response



class MdkengineeringDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        spider.logger.info(f"MdkengineeringDownloaderMiddleware: Scraping url: {response.url}")
        if response.status >= 400 and response < 500:  
            ## 400 < - - - > 499 range code
            spider.logger.info(f"\nMdkengineeringDownloaderMiddleware: Invalid Response, response code: {response.status} \n Most likely not found or not allowed")
            
            if response.status == 403:
                spider.logger.info(f'MdkengineeringDownloaderMiddleware: {response.status} code response received, this machine might be banned by the web server')
            
            raise IgnoreRequest(f"MdkengineeringDownloaderMiddleware: Skipping {response.status} coded response from {response.url}")
        elif response.status >= 300 and response < 400:
            
            ## 300 < - - - > 399 range code
            spider.logger.info(f'\nMdkengineeringDownloaderMiddleware: Invalid Response, response code: {response.status} \n Redirect response received')
            raise IgnoreRequest(f"MdkengineeringDownloaderMiddleware: Skipping {response.status} coded response from {response.url}")
        
        elif response.status >= 500:
            
            ## 500 < - - - > 599 range code
            spider.logger.info(f'\nMdkengineeringDownloaderMiddleware: Invalid Response, response code: {response.status} \n Server side of the website screwed up')
            raise IgnoreRequest(f"MdkengineeringDownloaderMiddleware: Skipping {response.status} coded response from {response.url}")
        
        elif response.status != 200:
            
            ## any code below 300 but not 200
            spider.logger.info(f'\nMdkengineeringDownloaderMiddleware: Invalid Response, response code: {response.status} \n Content Quality Problems')
            raise IgnoreRequest(f"MdkengineeringDownloaderMiddleware: Skipping {response.status} coded response from {response.url}")
            
        elif isinstance(response, HtmlResponse):
            try:
                
                spider.logger.info(f'MdkengineeringDownloaderMiddleware: Cleaning html & Reconstructing response')
                cleaned_html = self.clean_html(response, spider)
                
                #### Follow schema of spider return item
                ## [x] 0. HTML Content
                ## [x] 1. last-modified (date it was last modified) : date
                ## [x] 2. source (url) : string [x]
                ## [x] 3. (page) title : string [x]
                ## [x] 5. (custom) id (url-ending+last_modified date) : string
                ## [x] 6. keyword : []
                ## [x] 7. authors: []
                ## [x] 8. path: string
                cleaned_response = {
                    'title': cleaned_html['title'],
                    'content': cleaned_html['content'], ## List of HTML Tags
                    'last-modified': cleaned_html['last-modified'],
                    'source': cleaned_html['source'],
                    'id': cleaned_html['id'],
                    'keywords': cleaned_html['keywords'],
                    'authors': cleaned_html['authors'],
                    'site-path': cleaned_html['site-path'],
                    'categories': cleaned_html['categories']
                }
                
                ## Remake HTML response
                new_response = HtmlResponse(
                    url=response.url,
                    status=response.status,
                    headers=response.headers,
                    body=response.body,  # Keep the original body
                    encoding=response.encoding,
                    request=request,
                )
                
                # Replace the original response's meta with the cleaned HTML
                new_response.meta['cleaned_details'] = cleaned_response
                
                return new_response

            except Exception as e:
                spider.logger.error(f"MdkengineeringDownloaderMiddleware: Error processing response: {e}")
                # Optionally, re-raise the exception or return None to let the process continue
                raise  # This will propagate the exception

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        spider.logger.error(f"MdkengineeringDownloaderMiddleware: Exception occurred: {exception}")

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info("MdkengineeringDownloaderMiddleware: Spider opened: %s" % spider.name)

    def clean_html(self, response, spider):
        returner = []
        
        """
            -------------------------------------------------------------------------------
             -  [x] Meta Data Extractions 
                    ************************* Schema *************************
                 -  title               ==> h1 heading text of the wikidoc page
                 -  last_modified_date  ==> date html in response object was last edited
                                        ==> in DateTime._Date object format
                 -  keywords            ==> keywords article in html was associated with
                                        ==> extracted from the html content 
                 -  url_suffix          ==> portion of url after 'index.php/'
                 -  authors             ==> authors who created and/or edited the medical
                                            content in html
                                        ==> extracted from html content
                 -  categories          ==> categories textual content in html related to
                                        ==> extracted from html content
                           
            -------------------------------------------------------------------------------
        """ 
        title = response.xpath('//h1[contains(@id, "firstHeading")]/text()').extract()
        last_modified = response.xpath('//*[@id="footer-info-credits"]/text()').extract()[0].split(' by ')[0].split(', ')[-1]
        last_modified_date = datetime.strptime(last_modified, "%d %B %Y").date()
        keyword_extract = response.xpath('//p[descendant::i[contains(., "Synonyms and keywords")]]/text()')
        keywords = []
        if len(keyword_extract) > 0:
            keywords = keyword_extract.extract()[0].replace('Synonyms and keywords', '').replace('.\n', '').split('; ')
        url_suffix = str(response.url).split('index.php')[1]
        authors = response.xpath('//p[contains(., "Editor")]/a[contains(@title, "User:")]/text()').extract()
        categories = response.xpath('//*[@id="mw-normal-catlinks"]/ul/li/a[contains(@title, "Category:")]/text()').extract() 
        
        try:
            
            """
                -------------------------------------------------------------------------------
                 -  [x] Primary Cleaning ~ Filter page structures or metadata: 
                     -  Extract information under the <div> with class 'mw-parser-output'
                        **  <div class="mw-parser-output ..." ... />
                -------------------------------------------------------------------------------
            """ 
            content = response.xpath('//div[contains(@class, "mw-parser-output")]')
             
            """
                -------------------------------------------------------------------------------
                 -  [x] Secondary Cleaning ~ Filter complexly formatted information or 
                                             programmatically assistive information: 
                     -  Extract all from 'content' except:
                        1. tag with class infobox
                        2. comments
                        3. referencing sections and labels
                        4. remaining metadata under 'content'
                        
                     - Focuses on tags that can be used to build text based articles
                -------------------------------------------------------------------------------
            """ 
            filtered_content = content.xpath( 
                './/*[ \
                    not(ancestor-or-self::table[contains(@class, "infobox")]) \
                    and not(comment()) \
                    and not(contains(., "Template:")) \
                    and not(descendant-or-self::*[contains(@id, "References")]) \
                    and not(contains(@class, "references-column-width")) \
                    and not(ancestor::*[contains(@class, "references-column-width")]) \
                    and not(self::p[contains(., "Editor")]) \
                    and not(ancestor::p[contains(., "Editor")]) \
                    and not(ancestor::p[contains(., "Synonyms and keywords")]) \
                    and not(self::p[contains(., "Synonyms and keywords")]) \
                    and not(self::p[contains(., "For patient information")]) \
                    and not(ancestor::p[contains(., "For patient information")]) \
                    and not(self::sup[contains(@class, "reference")]) \
                    and not(ancestor-or-self::div[contains(@class, "toc")]) \
                    and not(self::div[contains(@role, "note")]) \
                ]'
            )
            
            """
                -------------------------------------------------------------------------------
                 -  [x] Tertiary Cleaning ~ Remove duplicates returned by 'xpath' method: 
                     -  Nested tags would be extracted as a separated entry,
                        so this for loop is to remove nested subtags
                -------------------------------------------------------------------------------
            """ 
            for idx, item in enumerate(filtered_content.extract()):
                if idx == 0:
                    returner.append(item)
                    continue
                
                if item in returner[-1]:
                    continue
                else: 
                    returner.append(item)
            
            spider.logger.info(f'MdkengineeringDownloaderMiddleware: HTML Cleaning Completed.')
        except Exception as error:
            spider.logger.error(f'MdkengineeringDownloaderMiddleware: HTML cleaning Failed: {error}')
            raise error
        
        
        #### Follow Schema of Spider Return Item
        ## [x] 0. HTML Content
        ## [x] 1. last-modified (date it was last modified) : date
        ## [x] 2. source (url) : string 
        ## [x] 3. (page) title : string 
        ## [x] 5. (custom) id (url-ending+last_modified date) : string
        ## [x] 6. keyword : []
        ## [x] 7. authors: []
        ## [x] 8. site-path: string 
        ## [x] 9. categories: [string]
        if (len(returner) == 0):
            
            ## No error was thrown here due to children of 'mw-category-generated' class tag provides
            ## relevant links to medical knowledge for scraping
            
            spider.logger.info(f'MdkengineeringDownloaderMiddleware: Nothing was extracted')
            return {
                'title': title,
                'content': None, 
                'last-modified': last_modified_date,
                'source': response.url,
                'id': f'{url_suffix[1:].replace("_", "-").replace("/", "_")}__{str(last_modified_date)}',
                'keywords': keywords,
                'authors': authors,
                'site-path': url_suffix,
                'categories': categories
            }
        else:
            return {
                'title': title,
                'content': returner, ## List of HTML Tags
                'last-modified': last_modified_date,
                'source': response.url,
                'id': f'{url_suffix[1:].replace("_", "-").replace("/", "_")}__{str(last_modified_date)}',
                'keywords': keywords,
                'authors': authors,
                'site-path': url_suffix,
                'categories': categories
            }
