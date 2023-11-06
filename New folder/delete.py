import os
from google.cloud import storage
import logging

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "Insert the path here to json file"

storage_client = storage.Client()

bucket_name = 'bucket_name'

# Function to delete an object from the bucket
def delete_object(object_name):
    try:
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(object_name)
        blob.delete()
        print(f"Deleted {object_name} from {bucket_name}")
    except Exception as e:
        log_exception(e)

# Function for error handling and logging
def log_exception(exception):
    logging.basicConfig(filename='error.log', level=logging.ERROR)
    logging.error(f"An error occurred: {exception}", exc_info=True)

if __name__ == "__main__":
    # Use the following line to delete an object. 
    delete_object("example.pdf") #example
