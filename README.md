
# Azure Blob Storage Backup Automation

Automates the backup process of files to Azure Blob Storage at regular intervals using Python.

## Features

- **Scheduled Backups**: Automates file uploads to Azure Blob Storage at specified intervals (e.g., every 10 seconds, configurable).
- **Overwrite Capability**: Ensures the latest version of the backup file replaces the existing file in Azure Blob Storage.
- **Error Handling**: Includes basic error handling to manage and log exceptions during the backup process.
- **Azure Integration**: Utilizes Azure SDK for Python (`azure-storage-blob`) for seamless integration with Azure Blob Storage.
- **Customizable**: Easily configurable for different file types, backup frequencies, and Azure Blob Storage configurations.

## Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/azure-blob-storage-backup.git
   cd azure-blob-storage-backup
   ```

2. **Install Dependencies**

   Ensure Python 3.x and pip are installed. Install required packages using pip:

   ```bash
   pip install azure-storage-blob schedule
   ```

3. **Azure Setup**

   - Create an Azure Blob Storage account if you haven't already.
   - Obtain the connection string from Azure portal (`AZURE_STORAGE_CONNECTION_STRING`).

4. **Configure Environment**

   Set the `AZURE_STORAGE_CONNECTION_STRING` environment variable with your Azure Blob Storage credentials.

   ```bash
   export AZURE_STORAGE_CONNECTION_STRING="DefaultEndpointsProtocol=https;AccountName=<your_account_name>;AccountKey=<your_account_key>;EndpointSuffix=core.windows.net"
   ```

5. **Run the Script**

   Customize `FILE_TO_UPLOAD` variable with the path to the file you want to backup. Then, run `backup.py` to initiate automated backups.

   ```bash
   python backup.py
   ```

## Usage

- The script will upload the specified file (`FILE_TO_UPLOAD`) to Azure Blob Storage every 10 seconds (adjustable in the script) by default.
- Ensure `sample_file.txt` or your specified file exists and contains the data you want to backup.
- Monitor the console output for status and error messages during the backup process.

## Notes

- Adjust `schedule.every(10).seconds.do(upload_file_to_blob)` in `backup.py` to change the backup frequency.
- Customize error handling, logging, and additional features based on your specific requirements.
- Consider deploying as an Azure Function for serverless execution or on Azure VM for continuous operation.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
