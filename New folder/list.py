import os
from google.cloud import storage
import logging

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "Insert the path here to json file"

storage_client = storage.Client()

bucket_name = 'bucket_name'

# Function to list objects in the bucket and retrieve metadata
def list_objects_with_metadata():
    try:
        bucket = storage_client.bucket(bucket_name)
        blobs = list(bucket.list_blobs())
        
        print("Objects in the bucket:")
        for blob in blobs:
            print(f"Object name: {blob.name}")
            metadata = blob.metadata
            if metadata:
                print("Metadata:")
                for key, value in metadata.items():
                    print(f"{key}: {value}")
    except Exception as e:
        log_exception(e)

# Function for error handling and logging
def log_exception(exception):
    logging.basicConfig(filename='error.log', level=logging.ERROR)
    logging.error(f"An error occurred: {exception}", exc_info=True)

if __name__ == "__main__":
    list_objects_with_metadata()
