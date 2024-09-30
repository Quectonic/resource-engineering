# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter # type: ignore

from google.cloud import storage
from google.cloud import logging
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
    
    def open_spider(self, spider):
        # Create a directory for storing the JSON files if it doesn't exist
        bucket_name = spider.settings.get('GCS_BUCKET_NAME', '')
        if bucket_name == '':
            spider.logger.error("GCS_BUCKET_NAME not set in settings.py")
        self.bucket_name = bucket_name
        self.storage_client = storage.Client()
        self.logging_client = logging.Client()
        self.logger = self.logging_client.logger('mdkengineering')
        self.bucket = self.storage_client.bucket(self.bucket_name)
        
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
        
        name = item.get('id', '')
        
    
        if item and name:
            # Upload to GCS
            self.upload_to_gcs(name=name, content=item, spider=spider)
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
        filename = f"{spider.name}_{name}.json"
        try:
            upload_content = json.dumps(content, indent=4)
            blob = self.bucket.blob(f"data/{filename}")
            blob.upload_from_string(upload_content, content_type='application/json')
            self.logger.log_struct({
                'file': filename,
                'bucket': self.bucket_name,
                'status': 'success'
            }, severity='INFO')
            spider.logger.info(f"CloudStoragePipeline: Uploaded {filename} to GCS bucket {self.bucket_name}")
        except Exception as e:
            self.logger.log_struct({
                'file': filename,
                'bucket': self.bucket_name,
                'status': 'failed'
            }, severity='ERROR')
            spider.logger.error(f"CloudStoragePipeline: Upload Failed: {e}")