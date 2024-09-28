import random

# Scrapy settings for mdkengineering project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "mdkengineering"

SPIDER_MODULES = ["mdkengineering.spiders"]
NEWSPIDER_MODULE = "mdkengineering.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "mdkengineering (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = random.uniform(0.25, 3)
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 32
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
   "mdkengineering.middlewares.MdkengineeringSpiderMiddleware": 543,
}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   "mdkengineering.middlewares.WikiDocURLFilterDownloaderMiddleware": 550,
   "mdkengineering.middlewares.RequestTracingDownloaderMiddleware": 545,
   "mdkengineering.middlewares.RotateUserAgentDownloaderMiddleware": 535,
   "mdkengineering.middlewares.MdkengineeringDownloaderMiddleware": 540,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
#    "mdkengineering.pipelines.CloudStoragePipeline": 300,
   ## Test Pipeline:
   "mdkengineering.pipelines.JsonWriterPipeline": 400,
}

OUTPUT_JSON_DIR = "output/json"

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
AUTOTHROTTLE_START_DELAY = 1
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 10
# The average number of requests Scrapy should be sending in parallel to
# each remote server
AUTOTHROTTLE_TARGET_CONCURRENCY = 2.0
# Enable showing throttling stats for every response received:
AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"


USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0; Trident/5.0)",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0; MDDCJS)",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)"
]

GCS_BUCKET_NAME = ""

# All are simply rules and guidelines on how to use wikiDoc
## Calculator topics are not yet implemented --> not text and involve logical calculation, should be separated from RAG
DENY_URL_PATTERNS_WIKIDOC = [
   ## Media
   r'index\.php\/Audios', r'index\.php\/Images', r'index\.php.*Image', 
   r'index\.php.*Editor', r'index\.php.*editor', r'index\.php\/Movies', r'index\.php\/mp3',
   
   ## Projects: Some contain crucial medical knowledge, e.g. drugs
   r'index\.php.*project', r'index\.php.*survival_guide', r'index\.php\/Calculator_topics',
   
   ## General Notes & Usage of WikiDoc
   r'index\.php\/Calendar', r'index\.php\/Footnotes', r'index\.php.*wikidoc:', r'index\.php.*Font', 
   r'index\.php\/Capitalization', r'index\.php.*edit', r'index\.php.*Edit', r'index\.php.*text', r'index\.php\/Basic_formatting',
   r'index\.php\/Get_Started_Here', r'index\.php\/Getting_started_video',
   r'index\.php\/Guide_to_medical_syntax', r'index\.php.*template', r'index\.php\/Templates:.*'
   r'index\.php.*How_to', r'index\.php\/IPA', r'index\.php\/Links', r'index\.php\/Magic_words',
   r'index\.php\/MakeBot', r'index\.php\/Login', r'index\.php\/Lists',
   r'index\.php\/Moving_pages', r'index\.php\/New_pages', r'index\.php\/NewPage', r'index\.php\/Ogg',
   r'index\.php\/Navigational_images', r'index\.php.*Special:', r'index\.php\/Columns', r'index\.php\/Citations', r'index\.php\/Categories',
   r'index\.php\/Editorial_Board', r'index\.php.*WikiDoc_Foundation', r'index\.php\/There_is_No_Industry_Support_for_This_Site', 
   r'index\.php\/Policies_%26_Guidelines', r'index\.php\/User:.*', 
   
   ## Special Parameters
   r'index\.php.*oldid=',
   r'index\.php.*returnto=', r'index\.php.*action=',
]

### List of url to be excluded:
    # 1. http://www.wikidoc.org/index.php/Audios ---
    # 2. http://www.wikidoc.org/index.php/Apply_to_be_an_Editor_in_Chief ** [ any kind of editor ] ---
    # 3. http://www.wikidoc.org/index.php/Basic_formatting ---
    # 4. http://www.wikidoc.org/index.php/Become_an_Editor_in_Chief ---
    # 5. http://www.wikidoc.org/index.php/Board_review_project ---
    # 6. http://www.wikidoc.org/index.php/Bolding_and_italicizing_text ---
    # 7. http://www.wikidoc.org/index.php/Bolding_text ---
    # 8. http://www.wikidoc.org/index.php/Botulism_resident_survival_guide **[ any kind of survival_guide ] ---
    # 9. http://www.wikidoc.org/index.php/Calculator_project ** [ any kind of project ] ---
    # 10. http://www.wikidoc.org/index.php/Calculator_topics ---
    # 11. http://www.wikidoc.org/index.php/Calendar ---
    # 12. http://www.wikidoc.org/index.php/Capitalization ---
    # 13. http://www.wikidoc.org/index.php/Differential_diagnosis_project ** [ any kind of project ] ---
    # 14. http://www.wikidoc.org/index.php/Differentiating_(disease_name)_from_other_diseases_page
    # 15. http://www.wikidoc.org/index.php/Dummy_edit ** [ any kind of edit ] ---
    # 16. 