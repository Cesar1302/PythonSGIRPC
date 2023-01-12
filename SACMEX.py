from asyncore import read
from cgi import print_arguments
from distutils import extension
from operator import not_
from os import close, remove, write
import os
import time  
from datetime import datetime
from datetime import date, datetime, timedelta,timezone
import shutil 
from shutil import copy2, copytree
from shutil import copy
from shutil import move
import glob
from os import remove
import urllib.request
from PIL import Image
import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import threading

def timer(timer_runs):
    while timer_runs.is_set():
        espacio='-------------'

        # Esrtablecemos el parametro de la fecha para despues con el bot colocarla en el datapicker del navegador web
        now=datetime.now()
        fecha_0=(now.strftime("%d/%m/%Y"))
        print(fecha_0)
        try:
            # Se instala de forma automatica el controlador de chrome,
            # de igual manera de establece el parametro de visualización de la pantalla y establece la dirección web
            driver=webdriver.Chrome(ChromeDriverManager().install())
            driver.maximize_window()
            driver.get('http://10.11.11.154/SACMEX/')
            driver.implicitly_wait(5)

            # El bot realizara los pasos o clicks a seguir para descargar los datos de la plataforma
            # click en informes
            driver.find_element(By.CSS_SELECTOR, "#menu > ul > li:nth-child(3) > a")\
                .click()
            # click en isoyetas
            driver.find_element(By.XPATH, "/html/body/div[4]/div[4]/div[1]/ul/li[7]/a")\
                .click()


            span=driver.find_element(By.CSS_SELECTOR, "#tab4_7 > iframe")

            driver.switch_to.frame(span)

            driver.find_element(By.XPATH,"//*[@id='form:calendar_input']")\
                .clear()\

            driver.find_element(By.XPATH,"//*[@id='form:calendar_input']")\
            .send_keys(fecha_0)

            driver.find_element(By.CSS_SELECTOR,"#form\:j_idt20 > span")\
                .click()

            time.sleep(5)

            driver.find_element(By.XPATH,"//*[@id='formDownload:j_idt31']/span")\
                .click()
            time.sleep(10)
            driver.close()
            print("Se obtuvieron los datos del portal de SACMEX")
        except:
            print("No fue posible la descarga de los datos de SACMEX")

        dircsvsacmex0 = r'C:\Users\meteorologia\Downloads\SACMEX0.csv'
        dircsvsacmex1 = r'C:\Users\meteorologia\Downloads\SACMEX1.csv'
        dircsvsacmex2 = r'C:\Users\meteorologia\Documents\Mapas\EMAS\SACMEX.csv'
        # Se obtiene la fecha con cambio de formato.
        fecha= date.today()
        print(espacio)

        # Se modifica el formato de la fecha para que el mes salga en español
        def current_date_format(date):
            months = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
            day = date.strftime("%d")
            month = months[date.month - 1]
            year = date.year
            messsage = "{}{}{}".format(day, month, year)

            return messsage

        fecha_final_lluvia=(current_date_format(fecha))
        print(fecha_final_lluvia)

        # Se leé el archivo .DAT y se cambía el formato a txt
        archivo = 'C:/Users/meteorologia/Downloads/'+fecha_final_lluvia+'_A.dat'
        print(archivo)
        sacmex = open(archivo, 'r')
        txt = sacmex.read()
        txt1=open(dircsvsacmex1,'w')
        txt1.write(txt)
        txt1.close()
        # Se filtran las columnas y se dejan los valores de lluvia con 2 decimales
        DSACMEX= pd.read_csv(dircsvsacmex1, index_col=0, header=0 , usecols=(0,1))
        #print(DSACMEX)
        roundplaces = np.round(DSACMEX,decimals=2)
        roundplaces.to_csv(dircsvsacmex1)
        print('Datos de SACMEX obtenidos')

        # Cambiamos los nombres de las columnas

        fecha_1=(now.strftime("%d/%m/%y %H:%M"))
        print(fecha_1)
        SACMEX=open(dircsvsacmex1)
        texto1=SACMEX.read()
        cambio1=texto1.replace("cat", "idEstacion")
        cambio2=cambio1.replace("elev", "lluvia")
        print(cambio2)
        SACMEX1=open(dircsvsacmex1, "w")
        SACMEX1.write(cambio2)
        SACMEX.close()
        SACMEX1.close()


        df00=pd.read_csv(dircsvsacmex0, index_col=0, header=0)
        df01=pd.DataFrame(df00)
        #print("archivo 1")
        #print(df01)

        df10=pd.read_csv(dircsvsacmex1, index_col=0, header=0)
        df11=pd.DataFrame(df10)
        #print("archivo 2")
        #print(df11)

        # Operación de resta para obtener el valor del acumulado en deacuerdo al programador de tareas (10 minutos)
        dfn=df11.sub(df01)
        print("resta")
        #print(dfn)
        dfn.to_csv(dircsvsacmex2)


        # Se agrega la columna de fecha y hora

        sacmex=pd.read_csv(dircsvsacmex2, index_col=False)
        sacmex['fechaHora']=np.where(sacmex['lluvia'] !='[]', fecha_1, ' ', )
        #print(sacmex)
        sacmex.to_csv(dircsvsacmex2)

        sacmex=pd.read_csv(dircsvsacmex2, usecols=(1, 2, 3), index_col=0, header=0) 
        #print(sacmex)
        sacmex.to_csv(dircsvsacmex2)

        time.sleep(5)
        remove(dircsvsacmex0)
        os.rename(dircsvsacmex1, dircsvsacmex0)
        remove(archivo)

        final=datetime.now()
        print(final)
        time.sleep(60)   # 15 minutos=850.
timer_runs = threading.Event()
timer_runs.set()
t = threading.Thread(target=timer, args=(timer_runs,))
t.start()

