# Importamos las librerías necesarias
import time
from datetime import datetime
from datetime import date, datetime, timedelta,timezone
import ModuloSGIRPC
import threading

def timer(timer_runs):
    while timer_runs.is_set():
        ModuloSGIRPC.proceso("iztacalco","AGOS")
        ModuloSGIRPC.proceso("azcapotzalco","FERS")
        ModuloSGIRPC.proceso("cuautepec","CUAUS")
        ModuloSGIRPC.proceso("cuajimalpa","STFS")
        ModuloSGIRPC.proceso("juarez", "SGIRPC")
        ModuloSGIRPC.proceso("miguelhidalgo","LEGS")
        ModuloSGIRPC.proceso("milpaalta","MPAS")
        ModuloSGIRPC.proceso("iztapa1","LOMS")
        ModuloSGIRPC.proceso("topilejo","TPJS")
        ModuloSGIRPC.proceso("coyoacan","SURS")
        ModuloSGIRPC.proceso("xochimilco","TLHS")


        final=datetime.now()
        print(final)
        time.sleep(30)   # 15 minutos=850.
timer_runs = threading.Event()
timer_runs.set()
t = threading.Thread(target=timer, args=(timer_runs,))
t.start()   