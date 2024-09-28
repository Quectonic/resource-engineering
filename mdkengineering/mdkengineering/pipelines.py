# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from google.cloud import storage
import os
import json

class MdkengineeringPipeline:
    
    """# 🍪 **Status: _Default_**
    
    **Description**
    -----------
    This is a default pipeline that does nothing. It is a placeholder for custom pipelines.
    """
    
    def process_item(self, item, spider):
        
        """# 🍪 **Status: _Default_**

        **Description**
        -----------
            This is a default method that does nothing. It is a placeholder for custom methods.

        Returns
        -------
        `dict`
            _description_
        """
        return item
    
class JsonWriterPipeline:

    def open_spider(self, spider):
        # Create a directory for storing the JSON files if it doesn't exist
        output_dir = spider.settings.get('OUTPUT_JSON_DIR', 'output_json')
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        self.output_dir = output_dir

    def process_item(self, item, spider):
        # Create a file name based on some attribute of the item, e.g., title or id
        file_name = item.get('id', 'default') + '.json'  # Use item ID as filename, or 'default' if not present
        file_path = os.path.join(self.output_dir, file_name)

        # Write item to JSON file with indent
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(dict(item), file, ensure_ascii=False, indent=4)
        
        spider.logger.info(f"Item saved to {file_path}")
        return item
    
class CloudStoragePipeline:
    
    """# 🍪 **Status: _Default_**
    
    **Description**
    -----------
        This pipeline uploads the scraped content to Google Cloud Storage.
    
    """
    
    def __init__(self, bucket_name) -> None:
        
        """# 🍪 **Status: _Default_**
        
        **Description**
        -----------
            This is an initialization method that sets up the Google Cloud Storage client and bucket.
            
        **Parameters**
        ----------
        bucket_name : `str`
            The name of the Google Cloud Storage bucket.
        """
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
        
        """# 🍪 **Status: _Default_**
        
        **Description**
        -----------
            This method uploads the content to Google Cloud Storage.
            
        **Parameters**
        ----------
        name : `str`
            The name of the file to be uploaded.
        content : `str`
        spider : `scrapy.Spider`
        
        """
        
        # GCS Upload Code
        filename = f"{spider.name}_{name}.txt"
        try:
            blob = self.bucket.blob(filename)
            blob.upload_from_string(content)
            spider.logger.info(f"Uploaded {filename} to GCS bucket {self.bucket_name}")
        except Exception as e:
            spider.logger.error(f"Upload Failed: {e}")