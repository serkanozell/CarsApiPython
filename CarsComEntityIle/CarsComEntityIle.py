
import requests
from bs4 import BeautifulSoup
import pandas as pd

url ="https://www.bkmkitap.com/kitap/cok-satan-kitaplar"

response=requests.get(url)
icerik = response.content
soup=BeautifulSoup(icerik,"html.parser")
fiyat = soup.find_all("div",{"class":"col col-12 currentPrice"})
isim =soup.find_all("a",{"class":"fl col-12 text-description detailLink"})
yazar = soup.find_all("a",{"class":"fl col-12 text-title"})
yayın = soup.find_all("a",{"class":"col col-12 text-title mt"})


liste = list()

for i in range(len(isim)):
    isim[i] = (isim[i].text).strip("\n").strip()
    yazar[i] = (yazar[i].text).strip("\n").strip()
    yayın[i] = (yayın[i].text).strip("\n").strip()
    fiyat[i] = (fiyat[i].text).strip("\n").replace("\nTL"," TL").strip()
    liste.append([isim[i],yazar[i],yayın[i],fiyat[i]])

df = pd.DataFrame(liste,columns = ["Kitap İsmi","Yazar","Yayın Evi","Fiyat"])
print(df)