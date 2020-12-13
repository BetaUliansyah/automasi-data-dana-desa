import requests
from bs4 import BeautifulSoup
import json
import csv
from datetime import datetime
from pytz import timezone
import sys
from google.colab import drive
drive.mount('/content/drive')

debug = True
filename = "daftar-desa-"+ datetime.now(timezone('Asia/Jakarta')).strftime("%Y-%m-%d--%H-%M") + ".csv"
path = F"/content/drive/My Drive/Colab Notebooks/Portal APBD/"

# Populate kab_keys 
desa_ids = []
s = requests.Session()
r = s.get('https://jaga.id/api/v5/desa/search?limit=100000&offset=0&nama=&kota=')
if r.status_code==200:
    for row in json.loads(r.text)['data']['result']:
        desa_ids.append(row['id'])
        print(row['id']) if debug else 0 

with open(path+filename, mode='w', newline='') as apbdcsv_file:
    csv.writer(apbdcsv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL).writerow(desa_ids)
    
print(desa_ids) if debug else 0
