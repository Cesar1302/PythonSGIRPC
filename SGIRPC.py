# Importamos las librerías necesarias
import time
from datetime import datetime
from datetime import date, datetime, timedelta,timezone
import ModuloSGIRPC
import threading

def timer(timer_runs):
    while timer_runs.is_set():
        try:
            ModuloSGIRPC.proceso("iztacalco","AGOS")
        except:
            print("Hubo un problema con la descarga de datos de estaestación")
            continue
        
        try:
            ModuloSGIRPC.proceso("azcapotzalco","FERS")
        except:
            print("Hubo un problema con la descarga de datos de estaestación")
            continue
        
        try:
            ModuloSGIRPC.proceso("cuautepec","CUAUS")
        except:
            print("Hubo un problema con la descarga de datos de estaestación")
            continue
        
        try:
            ModuloSGIRPC.proceso("cuajimalpa","STFS")
        except:
            print("Hubo un problema con la descarga de datos de estaestación")
            continue

        try:
            ModuloSGIRPC.proceso("juarez", "SGIRPC")
        except:
            print("Hubo un problema con la descarga de datos de estaestación")
            continue

        try:
            ModuloSGIRPC.proceso("miguelhidalgo","LEGS")
        except:
            print("Hubo un problema con la descarga de datos de estaestación")
            continue

        try:
            ModuloSGIRPC.proceso("milpaalta","MPAS")
        except:
            print("Hubo un problema con la descarga de datos de estaestación")
            continue

        try:
            ModuloSGIRPC.proceso("iztapa1","LOMS")
        except:
            print("Hubo un problema con la descarga de datos de estaestación")
            continue

        try:
            ModuloSGIRPC.proceso("topilejo","TPJS")
        except:
            print("Hubo un problema con la descarga de datos de estaestación")
            continue

        try:
            ModuloSGIRPC.proceso("coyoacan","SURS")
        except:
            print("Hubo un problema con la descarga de datos de estaestación")
            continue

        try:
            ModuloSGIRPC.proceso("xochimilco","TLHS")
        except:
            print("Hubo un problema con la descarga de datos de estaestación")
            continue

        final=datetime.now()
        print(final)
        print("El programa se volverá a ejecutar 10 minutos despues de",final)
        time.sleep(60)   # El tiempo esta dado en segundos 
timer_runs = threading.Event()
timer_runs.set()
t = threading.Thread(target=timer, args=(timer_runs,))
t.start()   