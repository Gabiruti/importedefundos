from zipfile import ZipFile
from urllib.request import urlopen
from io import BytesIO

def download_and_unzip(url, extract_to='.'):
    http_response = urlopen(url)
    zipfile = ZipFile(BytesIO(http_response.read()))
    zipfile.extractall(path=extract_to)

def find_year(year):
    ct = 1
    for ct in range(1,13):
        if ct < 10:
            download_and_unzip("https://dados.cvm.gov.br/dados/FI/DOC/INF_DIARIO/DADOS/inf_diario_fi_"+str(year)+"0"+str(ct)+".zip", extract_to="data")
        else:
            download_and_unzip("https://dados.cvm.gov.br/dados/FI/DOC/INF_DIARIO/DADOS/inf_diario_fi_"+str(year)+str(ct)+".zip", extract_to="data")


def download_and_unzip_all():
    ano = 2021
    
    while ano <= 2023:
        find_year(ano)
        ano += 1

if __name__ == '__main__':
    download_and_unzip_all()