# Importamos las librerías necesarias
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
url1 = 'https://www.oh-iiunam.mx/geojson/datospaginadia.txt'
file1 = 'OH1.csv'
r = urllib.request.urlopen(url1)
f = open(file1,'wb')
f.write(r.read())
f.close()
print(file1)
print('Datos de la estación Tlalnepantla obtenidos')




