import os
import datetime
import schedule
import time
from azure.storage.blob import BlobServiceClient

AZURE_STORAGE_CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName= #your storage account name# ;AccountKey= #your storage account key# ;EndpointSuffix=core.windows.net"
CONTAINER_NAME = 'backup-container'
FILE_TO_UPLOAD = 'sample_file.txt' #file which has to be back up

def upload_file_to_blob():
    try:
        blob_service_client = BlobServiceClient.from_connection_string(AZURE_STORAGE_CONNECTION_STRING)

        container_client = blob_service_client.get_container_client(CONTAINER_NAME)
        if not container_client.exists():
            container_client.create_container()

        file_name = f'backup_file.txt' #file name which should be show on blob
        blob_client = blob_service_client.get_blob_client(container=CONTAINER_NAME, blob=file_name)

        with open(FILE_TO_UPLOAD, 'rb') as data:
            blob_client.upload_blob(data, overwrite=True)

        print(f"Backup uploaded to Azure Blob Storage: {file_name}")

    except Exception as e:
        print(f"Error: {str(e)}")

schedule.every(5).minutes.do(upload_file_to_blob) #time for scheduling backup

while True:
    schedule.run_pending()
    time.sleep(1)
