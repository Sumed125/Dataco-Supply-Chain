import requests
import pandas as pd
import numpy as np
import os
from bs4 import BeautifulSoup


# Setting raw file path
script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir_path = os.path.dirname(script_dir)
raw_files_path = os.path.join(parent_dir_path, 'raw')

# Checking if raw file path exists or not
if os.path.isdir(raw_files_path):
    os.chdir(raw_files_path)
else: 
    os.makedirs(raw_files_path)
    os.chdir(raw_files_path)

# url to website hosting dataset
url = 'https://data.mendeley.com/public-api/datasets/8gx2fvg2k6/files?folder_id=root&version=1'
response = requests.get(url)

print(response.status_code)

main_data = response.json()

# retrieving url to download csv file of dataset
supply_chain_dataset_url = main_data[0].get("content_details").get('download_url')


# Extracting and saving file into local computer/server
with requests.get(supply_chain_dataset_url, stream = True) as response:
    response.raise_for_status()
    
    with open('dataset.csv', 'wb') as file:
        for chunk in response.iter_content(chunk_size = 1024*1024):
            file.write(chunk)

# retrieving url to download description csv fle
supply_chain_description_url = main_data[1].get("content_details").get("download_url")

# Extracting and saving file into local computer/server
with requests.get(supply_chain_description_url, stream = True) as response:
    response.raise_for_status()
    
    with open('description.csv', 'wb') as file:
        for chunk in response.iter_content(chunk_size = 1024*1024):
            file.write(chunk)
            

