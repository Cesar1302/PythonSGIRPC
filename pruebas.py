# Importamos las librerías necesarias
from asyncore import read
from cgitb import text
from email import header
import os
import time  
from datetime import datetime
from datetime import date, datetime, timedelta,timezone
from os import remove, sep
import urllib.request
import pandas as pd
import numpy as np
import seaborn as sb
import threading

def timer(timer_runs):
    while timer_runs.is_set():
        url1 = 'https://www.oh-iiunam.mx/geojson/datospaginadia.txt'
        file1 = r'C:\Users\meteorologia\Downloads\LLUVIA-DATOSOH.csv'
        #file1 = 'LLUVIA-DATOSOH.csv'
        r = urllib.request.urlopen(url1)
        f = open(file1,'wb')
        f.write(r.read())
        f.close()
        print('Datos de OH obtenidos')
        time.sleep(120)   # 2 minutos.
timer_runs = threading.Event()
timer_runs.set()
t = threading.Thread(target=timer, args=(timer_runs,))
t.start()
# Esperar 10 segundos y luego detener el timer.
# time.sleep(10)
# timer_runs.clear()
# print("¡El timer ha sido detenido!")