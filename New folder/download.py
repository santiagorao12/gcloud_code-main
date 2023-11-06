import os
from google.cloud import storage
import logging

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "Insert the path here to json file"

storage_client = storage.Client()

bucket_name = 'bucket_name'

# Function to download an object from the custom bucket
def download_object(object_name, local_file_path):
    try:
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(object_name)
        blob.download_to_filename(local_file_path)
        print(f"Downloaded {object_name} to {local_file_path}")
    except Exception as e:
        log_exception(e)

# Function for error handling and logging
def log_exception(exception):
    logging.basicConfig(filename='error.log', level=logging.ERROR)
    logging.error(f"An error occurred: {exception}", exc_info=True)

if __name__ == "__main__":
    download_object("example.pdf", "Insert path to the file")
