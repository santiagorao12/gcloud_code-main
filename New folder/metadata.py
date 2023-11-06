import os
from google.cloud import storage
import logging

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "Insert the path here to json file"

bucket_name = 'bucket_name'

# Function to set metadata for an object
def set_metadata(object_name, metadata):
    try:
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(object_name)
        blob.metadata = metadata
        blob.patch()
        print(f"Set metadata for {object_name}")
    except Exception as e:
        log_exception(e)

# Function for error handling and logging
def log_exception(exception):
    logging.basicConfig(filename='error.log', level=logging.ERROR)
    logging.error(f"An error occurred: {exception}", exc_info=True)

if __name__ == "__main__":
    # Modify metadata as needed 
    metadata = {
        "Content-Type": "image/png",  # Specifies the file type
        "Author": "John",        # Author or creator of the image
        "Description": "A receipt of a total of RM200",  # A brief description
    }
    set_metadata("Filename", metadata) #Add file name.extension // example.pdf or example.png
