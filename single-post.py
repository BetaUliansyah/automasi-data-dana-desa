import requests
from bs4 import BeautifulSoup
import json
import csv
from datetime import datetime
from pytz import timezone
import sys
#from google.colab import drive # comment this line if you use local file instead of Google Drive files
#drive.mount('/content/drive')  # comment this line if you use local file instead of Google Drive files

debug = True
#filename = "0-data-desa-"+ datetime.now(timezone('Asia/Jakarta')).strftime("%Y-%m-%d--%H-%M") + ".csv"
#path = F"/content/drive/My Drive/Colab Notebooks/Portal APBD/"

# Populate kab_keys (manually copied from output of daftar-desa.py)

# single POST
s = requests.Session()
i = 0

tahun = '2018'
kode_desa = '1102022001'
r = s.get('https://jaga.id/api/v5/desa/detil_anggaran?tahun='+str(tahun)+'&kode='+str(kode_desa))

if r.status_code==200 and len(r.text) != 0:
    result = json.loads(r.text)['data']['result'][0]

    # create headers
    print(result) if debug else 0
    #with open(path+filename, mode='w', newline='') as apbdcsv_file:
    #    csv.writer(apbdcsv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL).writerow(result)

    # isi values
    #with open(path+filename, mode='a+', newline='') as apbdcsv_file:
    #    csv.writer(apbdcsv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL).writerow(result.values())

    # parse child values penyaluran dan penyerapan
    penyaluran = dict(result['penyaluran'])
    penyaluran_1 = dict(penyaluran['1'])
    penyaluran_2 = dict(penyaluran['2'])
    penyaluran_3 = dict(penyaluran['3'])
    #penyerapan = result['penyerapan']
    print(penyaluran)
    
    print(penyaluran_1)
    print(penyaluran_2)
    print(penyaluran_3)

    #print("Penyerapan: " + penyerapan)
    print("---")
    penyerapan = dict(result['penyerapan'])
    penyerapan_1 = dict(penyerapan['1'])
    penyerapan_2 = dict(penyerapan['2'])
    penyerapan_3 = dict(penyerapan['3'])
    #penyerapan = result['penyerapan']
    print(penyerapan)
    
    print(penyerapan_1)
    print(penyerapan_2)
    print(penyerapan_3)

    # hitung total penyerapan per bidang
    if len(penyerapan) > 0:
        for i in [1,2,3]:
            print(penyerapan[str(i)])




#    for row in json.loads(r.text)['data']['result']:
#        print(row) if debug else 0
#        with open(path+filename, mode='a+', newline='') as apbdcsv_file:
#            csv.writer(apbdcsv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL).writerow(row)