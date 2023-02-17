import urllib.request
import requests
import pandas as pd
from bs4 import BeautifulSoup
import csv

url="https://www.aviationweather.gov/metar/data?ids=mmmx&format=raw&date=&hours=48"
filein= r'C:\Users\meteorologia\Downloads\MMMX.txt'
fileout= r'C:\Users\meteorologia\Downloads\MMMXmetar.txt'

#Peticion para compiar los datos del html del METAR
 
r = requests.get(url)
soup= BeautifulSoup(r.content, "html.parser")
# tag=soup.find("code")
# datos=tag.text
# print(datos)

r = urllib.request.urlopen(url)
f = open(filein,'wb')
f.write(r.read())
f.close()
#print(file1)
print('Datos del html del METAR descargados')

with open(filein,"r") as fr:
    contenido= fr.read()

soup= BeautifulSoup(contenido,"html.parser")
tags_code=soup.find_all("code")
with open(fileout,"w") as f:
    for etiqueta in tags_code:
        tags_content=etiqueta.text
        print(tags_content)
        f.write(tags_content + "\n")