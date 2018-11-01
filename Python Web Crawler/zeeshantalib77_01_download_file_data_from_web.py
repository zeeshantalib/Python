#------------------------ Download data of file(.csv) from internet
from urllib import request

goog_url='https://www.stats.govt.nz/assets/Uploads/Annual-balance-sheets/Annual-balance-sheets-2016-provisional/Download-data/annual-balance-sheet-2007-16-provisional-csv-tables.csv'

def download_file(csv_url):
    response=request.urlopen(csv_url)
    csv=response.read()
    csv_str =str(csv)
    lines=csv_str.split("\\n")
    destination_url= r'goog.csv'
    fx=open(destination_url,"w")
    for line in lines:
        fx.write(line+"\n")
    fx.close()

download_file(goog_url)
