import urllib.request
import pandas as pd

url="https://www.aviationweather.gov/metar/data?ids=mmmx&format=raw&date=&hours=48"
dirmmmx= r'C:\Users\meteorologia\Downloads\MMMX.txt'
dirmmmxmetar= r'C:\Users\meteorologia\Downloads\MMMXmetar.txt'

try:  
    r = urllib.request.urlopen(url)
    f = open(dirmmmx,'wb')
    f.write(r.read())
    #print(f)
    f.close()

    datos = []
    with open(dirmmmx) as metar:
        lineas= metar.readlines()
        for linea in lineas:
            datos.append(linea.strip("METAR"))
    print(datos)
    
    
    print('Datos de MMMX obtenidos')
except:
    print("Se produjo un error al momento de descargar los datos")