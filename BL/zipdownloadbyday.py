from zipfile import ZipFile
from urllib.request import urlopen
from io import BytesIO
from datetime import datetime
import os


def download_and_unzip(url, extract_to='.'):
    http_response = urlopen(url)
    zipfile = ZipFile(BytesIO(http_response.read()))
    zipfile.extractall(path=extract_to)

def download_and_unzip_by_day(dt_string,pathh):
    url = "https://dados.cvm.gov.br/dados/FI/DOC/INF_DIARIO/DADOS/inf_diario_fi_"+dt_string+".zip"

    if os.path.exists(pathh):
        os.remove(path)

    try: 
        download_and_unzip(url, extract_to="data")

    except:
        return

today = datetime.today()
dt_string = today.strftime("%Y%m")
path = "../data/inf_diario_fi_"+dt_string+".csv"

if __name__ == '__main__':
    download_and_unzip_by_day(dt_string,path)
