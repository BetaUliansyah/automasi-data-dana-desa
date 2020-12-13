import requests
from bs4 import BeautifulSoup
import json
import csv
from datetime import datetime
from pytz import timezone
import sys
from google.colab import drive  # comment this line if you use local file instead of Google Drive files
drive.mount('/content/drive')   # comment this line if you use local file instead of Google Drive files

debug = True
filename = "daftar-desa-"+ datetime.now(timezone('Asia/Jakarta')).strftime("%Y-%m-%d--%H-%M") + ".csv"
path = F"/content/drive/My Drive/Colab Notebooks/Portal APBD/"

s = requests.Session()

# Populate kab_keys 

# create headers (diambil dari data APBD Nasional seluruh tahun)
for tiap_tahun in alltahun.find_all("option"): # populate all tahun
    print(tiap_tahun['value']) if debug else 0
    r = s.post('http://www.djpk.kemenkeu.go.id/portal/filter', 
                data={'_token': token, 'data': 'apbd ', 'tahun': tiap_tahun['value'], 'provinsi': '--', 'pemda': '--'}) # query nasional saja
    if "html" not in r.text and r.status_code==200:
        # create headers
        result = json.loads(r.text)
        if len(result) == 0:
            continue

        print(result) if debug else 0
        
        header_dict = {'no': '',
                      'tahun': '',
                      'pemda': '',
                      'provinsi': '' ,
                      'wilayah': '',
                      'disclaimer': '',
                      'special_row': '',
                      }

        # populate all kode akun
        for kode_postur in result['postur'].keys():
            print(kode_postur) if debug else 0
            header_dict[kode_postur+"_a"] = 0
            header_dict[kode_postur+"_r"] = 0
            header_dict[kode_postur+"_p"] = 0
            for kode_akun in result['postur'][kode_postur]['child'].keys():
                print(kode_akun) if debug else 0
                header_dict[kode_akun+"_a"] = 0
                header_dict[kode_akun+"_r"] = 0
                header_dict[kode_akun+"_p"] = 0
                for kode_subakun in result['postur'][kode_postur]['child'][kode_akun]['child'].keys():
                    print(kode_subakun) if debug else 0
                    header_dict[kode_subakun+"_a"] = 0
                    header_dict[kode_subakun+"_r"] = 0
                    header_dict[kode_subakun+"_p"] = 0
                    

# menuliskan header lengkap ke file
header_row = []
for key in header_dict.keys():
    header_row.append(key)

print("Saving to " + path + filename) if debug else 0 
with open(path+filename, mode='w', newline='') as apbdcsv_file:
    csv.writer(apbdcsv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL).writerow(header_dict)
print(header_dict) if debug else 0


# looping 2017-2020


tahun_range = [2017..2020]
for tahun in tahun_range:
    for kode_desa in desa_ids:
        r = s.get('https://jaga.id/api/v5/desa/detil_anggaran?tahun='+str(tahun)+'&kode='+str(kode_desa))
        if r.status_code==200 and len(r.text) != 0:
            result = json.loads(r.text)['data']['result']
            print(result) if debug else 0 