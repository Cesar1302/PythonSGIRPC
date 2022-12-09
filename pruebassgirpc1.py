# Importamos las librerías necesarias
from asyncore import read
from codecs import latin_1_decode
from dataclasses import replace
import os
import time  
from datetime import datetime
from datetime import date, datetime, timedelta,timezone
from os import remove
import urllib.request
import pandas as pd
import numpy as np

espacio='-------------'

print(espacio)
url1 = 'https://smn.conagua.gob.mx/tools/PHP/sivea_v2/siveaEsri2/php/get_reporteEstacion.php?tipo=1&estacion=ECOGUARDAS'
file1 = r'C:\Users\meteorologia\Documents\Mapas\EMAS\ECOGUARDAS.csv'
r = urllib.request.urlopen(url1)
f = open(file1,'wb')
f.write(r.read())
f.close()
print(file1)
#print('Datos de la estación Ecoguardas obtenidos')

ECOGUARDAS=pd.read_csv(file1, index_col=False, header=8, encoding='latin-1', usecols=(0,2,3,4,5,6,7,8,9,10))
ECOGUARDAS.to_csv(file1)
ECOGUARDAS1=open(file1,'r')
ECOGUARDAS1= ''.join([i for i in ECOGUARDAS1])
texto1=ECOGUARDAS1.replace('Fecha Local', 'fechaHora')
texto2=texto1.replace('DirecciÃ³n del Viento (grados)', 'direccionViento')
texto3=texto2.replace('DirecciÃ³n de rÃ¡faga (grados)','direccionRacha')
texto4=texto3.replace('Rapidez de viento (km/h)', 'velocidadViento')
texto5=texto4.replace('Rapidez de rÃ¡faga (km/h)', 'velocidadRacha')
texto6=texto5.replace('Temperatura del Aire (Â°C)', 'temperatura')
texto7=texto6.replace('Humedad relativa (%)', 'humedadRelativa')
texto8=texto7.replace('PresiÃ³n AtmosfÃ©rica (hpa)', 'presionBar')
texto9=texto8.replace('PrecipitaciÃ³n (mm)', 'lluvia')
texto10=texto9.replace('RadiaciÃ³n Solar (W/mÂ²)', 'radiacionSolar')
print(texto10)
ECOGUARDAS1=open(file1, 'w')
ECOGUARDAS1.writelines(texto10)
ECOGUARDAS1.close()

ECOGUARDAS=pd.read_csv(file1, index_col=0, header=0, usecols=(1,2,3,4,5,6,7,8,9,10))
print(ECOGUARDAS)
ECOGUARDAS.to_csv(file1)

DF=pd.read_csv(file1, index_col=0)
DF['idEstacion']=np.where(DF['temperatura'] !='[]', 'ECOGUARDAS', ' ', )
#print(DF)
DF.to_csv(file1)

DF=pd.read_csv(file1, index_col=0)
DF.fillna(9999, inplace=True)
DF
DF.to_csv(file1)
print(DF)


espacio='-------------'

print(espacio)
url1 = 'https://smn.conagua.gob.mx/tools/PHP/sivea_v2/siveaEsri2/php/get_reporteEstacion.php?tipo=1&estacion=TACUBAYA'
file1 = r'C:\Users\meteorologia\Documents\Mapas\EMAS\TACUBAYA.csv'
r = urllib.request.urlopen(url1)
f = open(file1,'wb')
f.write(r.read())
f.close()
print(file1)
#print('Datos de la estación TACUBAYA obtenidos')

TACUBAYA=pd.read_csv(file1, index_col=False, header=8, encoding='latin-1', usecols=(0,2,3,4,5,6,7,8,9,10))
TACUBAYA.to_csv(file1)
TACUBAYA1=open(file1,'r')
TACUBAYA1= ''.join([i for i in TACUBAYA1])
texto1=TACUBAYA1.replace('Fecha Local', 'fechaHora')
texto2=texto1.replace('DirecciÃ³n del Viento (grados)', 'direccionViento')
texto3=texto2.replace('DirecciÃ³n de rÃ¡faga (grados)','direccionRacha')
texto4=texto3.replace('Rapidez de viento (km/h)', 'velocidadViento')
texto5=texto4.replace('Rapidez de rÃ¡faga (km/h)', 'velocidadRacha')
texto6=texto5.replace('Temperatura del Aire (Â°C)', 'temperatura')
texto7=texto6.replace('Humedad relativa (%)', 'humedadRelativa')
texto8=texto7.replace('PresiÃ³n AtmosfÃ©rica (hpa)', 'presionBar')
texto9=texto8.replace('PrecipitaciÃ³n (mm)', 'lluvia')
texto10=texto9.replace('RadiaciÃ³n Solar (W/mÂ²)', 'radiacionSolar')
print(texto10)
TACUBAYA1=open(file1, 'w')
TACUBAYA1.writelines(texto10)
TACUBAYA1.close()

TACUBAYA=pd.read_csv(file1, index_col=0, header=0, usecols=(1,2,3,4,5,6,7,8,9,10))
print(TACUBAYA)
TACUBAYA.to_csv(file1)

DF=pd.read_csv(file1, index_col=0)
DF['idEstacion']=np.where(DF['temperatura'] !='[]', 'TACUBAYA', ' ', )
#print(DF)
DF.to_csv(file1)

DF=pd.read_csv(file1, index_col=0)
DF.fillna(9999, inplace=True)
DF
DF.to_csv(file1)
print(DF)


espacio='-------------'

print(espacio)
url1 = 'https://smn.conagua.gob.mx/tools/PHP/sivea_v2/siveaEsri2/php/get_reporteEstacion.php?tipo=1&estacion=TEZONTLE'
file1 = r'C:\Users\meteorologia\Documents\Mapas\EMAS\TEZONTLE.csv'
r = urllib.request.urlopen(url1)
f = open(file1,'wb')
f.write(r.read())
f.close()
print(file1)
#print('Datos de la estación TEZONTLE obtenidos')

TEZONTLE=pd.read_csv(file1, index_col=False, header=8, encoding='latin-1', usecols=(0,2,3,4,5,6,7,8,9,10))
TEZONTLE.to_csv(file1)
TEZONTLE1=open(file1,'r')
TEZONTLE1= ''.join([i for i in TEZONTLE1])
texto1=TEZONTLE1.replace('Fecha Local', 'fechaHora')
texto2=texto1.replace('DirecciÃ³n del Viento (grados)', 'direccionViento')
texto3=texto2.replace('DirecciÃ³n de rÃ¡faga (grados)','direccionRacha')
texto4=texto3.replace('Rapidez de viento (km/h)', 'velocidadViento')
texto5=texto4.replace('Rapidez de rÃ¡faga (km/h)', 'velocidadRacha')
texto6=texto5.replace('Temperatura del Aire (Â°C)', 'temperatura')
texto7=texto6.replace('Humedad relativa (%)', 'humedadRelativa')
texto8=texto7.replace('PresiÃ³n AtmosfÃ©rica (hpa)', 'presionBar')
texto9=texto8.replace('PrecipitaciÃ³n (mm)', 'lluvia')
texto10=texto9.replace('RadiaciÃ³n Solar (W/mÂ²)', 'radiacionSolar')
print(texto10)
TEZONTLE1=open(file1, 'w')
TEZONTLE1.writelines(texto10)
TEZONTLE1.close()

TEZONTLE=pd.read_csv(file1, index_col=0, header=0, usecols=(1,2,3,4,5,6,7,8,9,10))
print(TEZONTLE)
TEZONTLE.to_csv(file1)

DF=pd.read_csv(file1, index_col=0)
DF['idEstacion']=np.where(DF['temperatura'] !='[]', 'TEZONTLE', ' ', )
#print(DF)
DF.to_csv(file1)

DF=pd.read_csv(file1, index_col=0)
DF.fillna(9999, inplace=True)
DF
DF.to_csv(file1)
print(DF)


espacio='-------------'

print(espacio)
url1 = 'https://smn.conagua.gob.mx/tools/PHP/sivea_v2/siveaEsri2/php/get_reporteEstacion.php?tipo=1&estacion=ESCNALCIENCIASBIOLOGICAS'
file1 = r'C:\Users\meteorologia\Documents\Mapas\EMAS\ENCB.csv'
r = urllib.request.urlopen(url1)
f = open(file1,'wb')
f.write(r.read())
f.close()
print(file1)
#print('Datos de la estación ENCB obtenidos')

ENCB=pd.read_csv(file1, index_col=False, header=8, encoding='latin-1', usecols=(0,2,3,4,5,6,7,8,9,10))
ENCB.to_csv(file1)
ENCB1=open(file1,'r')
ENCB1= ''.join([i for i in ENCB1])
texto1=ENCB1.replace('Fecha Local', 'fechaHora')
texto2=texto1.replace('DirecciÃ³n del Viento (grados)', 'direccionViento')
texto3=texto2.replace('DirecciÃ³n de rÃ¡faga (grados)','direccionRacha')
texto4=texto3.replace('Rapidez de viento (km/h)', 'velocidadViento')
texto5=texto4.replace('Rapidez de rÃ¡faga (km/h)', 'velocidadRacha')
texto6=texto5.replace('Temperatura del Aire (Â°C)', 'temperatura')
texto7=texto6.replace('Humedad relativa (%)', 'humedadRelativa')
texto8=texto7.replace('PresiÃ³n AtmosfÃ©rica (hpa)', 'presionBar')
texto9=texto8.replace('PrecipitaciÃ³n (mm)', 'lluvia')
texto10=texto9.replace('RadiaciÃ³n Solar (W/mÂ²)', 'radiacionSolar')
print(texto10)
ENCB1=open(file1, 'w')
ENCB1.writelines(texto10)
ENCB1.close()

ENCB=pd.read_csv(file1, index_col=0, header=0, usecols=(1,2,3,4,5,6,7,8,9,10))
print(ENCB)
ENCB.to_csv(file1)

DF=pd.read_csv(file1, index_col=0)
DF['idEstacion']=np.where(DF['temperatura'] !='[]', 'ENCB', ' ', )
#print(DF)
DF.to_csv(file1)

DF=pd.read_csv(file1, index_col=0)
DF.fillna(9999, inplace=True)
DF
DF.to_csv(file1)
print(DF)
