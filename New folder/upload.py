import os
from google.cloud import storage
import logging

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "Insert the path here to json file"

storage_client = storage.Client()

bucket_name = 'bucket_name'

# Function to upload an object to the custom bucket
def upload_object(object_name, local_file_path):
    try:
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(object_name)
        blob.upload_from_filename(local_file_path)
        print(f"Uploaded {object_name} to {bucket_name}")
    except Exception as e:
        log_exception(e)

# Function for error handling and logging
def log_exception(exception):
    logging.basicConfig(filename='error.log', level=logging.ERROR)
    logging.error(f"An error occurred: {exception}", exc_info=True)

if __name__ == "__main__":
    upload_object("3.png", "Insert path to the file")
