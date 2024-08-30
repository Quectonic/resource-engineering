# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from scrapy.http import HtmlResponse
from scrapy.exceptions import IgnoreRequest
import random
from lxml.html.clean import Cleaner
from lxml import html, etree
import json

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


class MedicalDomainKnowledgeBaseSpiderMiddleware:
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
        
        if (not response.xpath('//p') or 'Error' in response.xpath('//title/text()').get()):
            spider.logger.info(f"Skipping page {response.url} - No meaningful content found in this.")
            response.meta['skip_item_extraction'] = True
        
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
        
        spider.logger.error(f"Exception occured when extracting html components: {exception}")

        # Should return either None or an iterable of Request or item objects.
        return None

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)

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
        spider.logger.info(f"Request Made:\n{request_info}")
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
        spider.logger.info(f"Response Object:\n{response_info}")
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
        spider.logger.info(f'Using User-Agent: {request.headers["User-Agent"]}')
        return None
    
    
    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)
        
class MedicalDomainKnowledgeBaseDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.
    
    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        # Creates an instance of the CustomDownloaderMiddleware class.
        s = cls()
        # Connects the spider_opened method to the spider_opened signal.
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        # Returns the instance of the middleware.
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
        spider.logger.info(f"Scraping url: {response.url}")
        if response.status != 200:
            spider.logger.info(f"\nInvalid Responses Detected, response code: {response.status}")
            raise IgnoreRequest(f"Skipping {response.status} coded response from {response.url}")
        elif isinstance(response, HtmlResponse):
            try:
                # # Initialize the Cleaner with specific options
                # cleaner = Cleaner()
                # cleaner.javascript = True
                # cleaner.style = True
                # cleaner.comments = True

                # # Clean the HTML content
                # cleaned_html = cleaner.clean_html(response.text)
                
                # html_content = response.text
                
                print(f'request: {str(request)}\nresponse: {str(response)}')
                
                spider.logger.info(f'Cleaning html & Reconstructing response')
                cleaned_html = self.clean_html(response)
                
                cleaned_response = {
                    'title': cleaned_html['title'],
                    'html_content': cleaned_html['content']
                }
                
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
                spider.logger.error(f"Error processing response: {e}")
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
        
        spider.logger.error(f"Exception occurred: {exception}")

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        return None

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)
        
    def clean_html(self, response):
        title = response.xpath('//h1[contains(@id, "firstHeading")]').get()
        content = response.xpath('//div[contains(@class, "mw-parser-output")]')
        
        # Tags are still present, 
        # use xpath('//<something>/text') and further processing in the spider to turn into actual documents
        
        # TODO: filter "Shown below is ...:" text
        # TODO: filter "External links" 'sections' and correspondingly sectional contents
        filtered_content = content.xpath(
            './/*[not(self::table[contains(@class, "infobox")])]'
        )
        
        returner = []
        
        for element in filtered_content:
            returner.append(etree.tostring(element, pretty_print=True).decode('utf-8'))
        
        
        # filtered_content = filtered_content.getall()
        return {
            'title': title,
            'content': returner
        }
