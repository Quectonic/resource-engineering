# myproject/middlewares.py

from scrapy import signals
import random

class WikiDocDownloaderMiddleware:

    def __init__(self):
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0; Trident/5.0)",
            "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0; MDDCJS)",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393",
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)"
        ]

    def process_request(self, request, spider):
        # Modify the request before it is sent
        user_agent = random.choice(self.user_agents)
        request.headers['User-Agent'] = user_agent
        # For example, add a random User-Agent header to the request
        return None  # Continue processing

    def process_response(self, request, response, spider):
        # Modify the response before it is sent to the spider
        if response.status != 200:
            # Handle non-200 responses
            print(f'\nInvalid Reponses detected, response: {response}\n')
            return response  # Continue processing
        # Perform any other processing needed on the response
        return response

    def process_exception(self, request, exception, spider):
        # Handle exceptions that occur during the request
        spider.logger.error(f"Exception occurred: {exception}")
        # Retry the request or handle the error
        return None  # Continue processing with the next middleware