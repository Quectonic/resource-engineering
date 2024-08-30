# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from google.cloud import storage

class MdkengineeringPipeline:
    def process_item(self, item, spider):
        return item
    
class CloudStoragePipeline:
    def __init__(self, bucket_name) -> None:
        # Initialize GCS Bucket and client 
        # Make sure client has right permission and use ADC or other credential methods suggested by Google Cloud
        self.bucket_name = bucket_name
        self.storage_client = storage.Client()
        self.bucket = self.storage_client.bucket(self.bucket_name)
        
    @classmethod
    def from_crawler(cls, crawler):
        # Instantiate the pipeline with the bucket name from settings
        return cls(
            bucket_name=crawler.settings.get('GCS_BUCKET_NAME')
        )
        
    def process_item(self, item, spider):
        
        #### Follow Schema of Spider Return Item
        ## - content
        ## [ ] 0. RAW TEXT Content
        ##          0.1. section
        ##              0.1.1 text
        ## - Metadata types
        ## [ ] 1. last-modified (date it was last modified) : date
        ## [x] 2. source (url) : string [x]
        ## [x] 3. (page) title : string [x]
        ## [ ] 5. (custom) id (url-ending+last_modified date) : string
        ## [ ] 6. keyword : []
        ## [ ] 7. authors: []
        
        ## Extract text content from the JSON processed from the spider
        content = item.get('text', '')
        ## Extract url path ( excluding domain, just path ) from the JSON processed from the spider
        name = item.get('url-path', '')
        ## Extract title of the page from the JSON processed from the spider
        title = item.get('title', '')
        
    
        if content and name:
            # Upload to GCS
            self.upload_to_gcs(name=name, content=content, spider=spider)
        return item
    
    def upload_to_gcs(self, name, content, spider):
        
        # GCS Upload Code
        filename = f"{spider.name}_{name}.txt"
        try:
            blob = self.bucket.blob(filename)
            blob.upload_from_string(content)
            spider.logger.info(f"Uploaded {filename} to GCS bucket {self.bucket_name}")
        except Exception as e:
            spider.logger.error(f"Upload Failed: {e}")