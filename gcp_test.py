from google.cloud import storage
from PIL import Image
import io
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'gcp_key.json'
client = storage.Client()
bucket_name = 'hha504-storage-test'
bucket = client.bucket(bucket_name)

files_upload = []
for root, dirs, files in os.walk("gcp-images"):
    for file in files:
        files_upload.append(os.path.join(root, file))

for file in files_upload:
    print(f"Working on {file}")
    with open(file, 'rb') as f:
        file_byte_array = f.read()
    print(file)
    file = file.split("/")[-1]
    print('new file name: ', file)

    try:
        blob = bucket.blob(file)
        blob.upload_from_string(file_byte_array, content_type='image/png')
        print(f"Image uploaded successfully to Google Cloud Storage!")
    except Exception as e:
        print(f"Error: {e}")

print("Image uploaded successfully to Google Cloud Storage!")

