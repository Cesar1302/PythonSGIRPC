# Importamos las librerías necesarias
import os
from pickle import FALSE, NONE
import time
from datetime import datetime
from datetime import date, datetime, timedelta,timezone
import urllib.request
import pandas as pd
import numpy as np
import seaborn as sb
from os import remove
import SGIRPCtst
import threading

def timer(timer_runs):
    while timer_runs.is_set():
        SGIRPCtst.proceso("iztacalco","AGOS")
        SGIRPCtst.proceso("azcapotzalco","FERS")

        final=datetime.now()
        print(final)
        time.sleep(30)   # 15 minutos=850.
timer_runs = threading.Event()
timer_runs.set()
t = threading.Thread(target=timer, args=(timer_runs,))
t.start()   
