import logging

class Colors:
    RESET = "\x1b[0m"
    GREY = "\x1b[38;21m"
    YELLOW = "\x1b[33;21m"
    RED = "\x1b[31;21m"
    BOLD_RED = "\x1b[31;1m"
    GREEN = "\x1b[32;21m"
    BLUE = "\x1b[34;21m"
    
class LogFormatter(logging.Formatter):
    FORMATS = {
        logging.DEBUG: Colors.GREY + "%(asctime)s - %(name)s - %(levelname)s - %(message)s" + Colors.RESET,
        logging.INFO: Colors.GREEN + "%(asctime)s - %(name)s - %(levelname)s - %(message)s" + Colors.RESET,
        logging.WARNING: Colors.YELLOW + "%(asctime)s - %(name)s - %(levelname)s - %(message)s" + Colors.RESET,
        logging.ERROR: Colors.RED + "%(asctime)s - %(name)s - %(levelname)s - %(message)s" + Colors.RESET,
        logging.CRITICAL: Colors.BOLD_RED + "%(asctime)s - %(name)s - %(levelname)s - %(message)s" + Colors.RESET,
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno, self._fmt)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)



import logging
import scrapy
import google.cloud.logging
from google.cloud.logging.handlers import CloudLoggingHandler

# ANSI escape codes for colors (for local logging)
class Colors:
    RESET = "\x1b[0m"
    GREY = "\x1b[38;21m"
    YELLOW = "\x1b[33;21m"
    RED = "\x1b[31;21m"
    BOLD_RED = "\x1b[31;1m"
    GREEN = "\x1b[32;21m"
    BLUE = "\x1b[34;21m"

# Custom Formatter for local logging
class CustomFormatter(logging.Formatter):
    FORMATS = {
        logging.DEBUG: Colors.GREY + "%(asctime)s - %(name)s - %(levelname)s - %(message)s" + Colors.RESET,
        logging.INFO: Colors.GREEN + "%(asctime)s - %(name)s - %(levelname)s - %(message)s" + Colors.RESET,
        logging.WARNING: Colors.YELLOW + "%(asctime)s - %(name)s - %(levellevel)s - %(message)s" + Colors.RESET,
        logging.ERROR: Colors.RED + "%(asctime)s - %(name)s - %(levelname)s - %(message)s" + Colors.RESET,
        logging.CRITICAL: Colors.BOLD_RED + "%(asctime)s - %(name)s - %(levelname)s - %(message)s" + Colors.RESET,
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno, self._fmt)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)

# class MySpider(scrapy.Spider):
#     name = "my_spider"

#     def __init__(self, *args, **kwargs):
#         super(MySpider, self).__init__(*args, **kwargs)
        
#         # Set up Google Cloud Logging Client
#         client = google.cloud.logging.Client()
        
#         # Create CloudLoggingHandler
#         cloud_handler = CloudLoggingHandler(client)
        
#         # Create local console handler with custom formatting
#         console_handler = logging.StreamHandler()
#         console_handler.setLevel(logging.DEBUG)
#         console_handler.setFormatter(CustomFormatter())

#         # Clear any existing handlers attached to spider.logger
#         self.logger.handlers.clear()
        
#         # Add the handlers to spider.logger
#         self.logger.addHandler(cloud_handler)  # Add cloud logging handler
#         self.logger.addHandler(console_handler)  # Add local console handler

#         # Set the logger level
#         self.logger.setLevel(logging.DEBUG)

#     def parse(self, response):
#         self.logger.debug("This is a debug message from the spider.")
#         self.logger.info("This is an info message from the spider.")
#         self.logger.warning("This is a warning message from the spider.")
#         self.logger.error("This is an error message from the spider.")
#         self.logger.critical("This is a critical message from the spider.")
