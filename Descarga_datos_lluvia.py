#Librerias
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
import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager

espacio='-------------'


try:
    # Insertamos la fecha
    now=datetime.now()
    fecha=(now.strftime("%d/%m/%y %H:%M"))
    print(fecha)
    fileOH = r'C:\Users\meteorologia\Documents\Archivos_temporales\OH.csv'

    #Se buscan los datos del OH en la web por medio de un request, así mismo se guarda en un csv
    print("OH")
    print(espacio)
    urlOH='https://www.oh-iiunam.mx/geojson/datospaginaquince.txt'

    r = urllib.request.urlopen(urlOH)
    f = open(fileOH,'wb')
    f.write(r.read())
    f.close()
    print('Datos de OH obtenidos de su portal')

    # Se hacen algunos cambios dentro del archivo para darle el formato correspondiente al csv y que la libreria pandas lo pueda leer correctamente
    oh=open(fileOH)
    texto=oh.read()
    texto1=texto.replace(" ", ",")
    print("Datos brutos en csv")
    print(texto1)
    oh1=open(fileOH,"w")
    oh1.write(texto1)
    oh.close()
    oh1.close()

    # Este paso de lectura y guardado solo fue para asignar un indice de forma automatica
    oh=pd.read_csv(fileOH, index_col=False, header=None)
    oh.to_csv(fileOH)

    # Se renombran las columnas con ls claves requeridas
    oh=pd.read_csv(fileOH, index_col=0, header=0)
    print("Tabla de datos con indice y encabezado")
    print(oh)
    texto1=oh.rename({'2': 'idEstacion'}, axis=1)
    texto2=texto1.rename({'3': 'lluvia'}, axis=1)
    print("Encabezados renombrados de numeros a ID y valor de lluvia")
    print(texto2)
    texto2.to_csv(fileOH)

    # Se filtran las columnas y se dejan los valores de lluvia con 2 decimales
    OH = pd.read_csv(fileOH, index_col=0, header=0, usecols=(3,4))
    print("Datos antes de ser ajustados a 2 decimales y usando solo las columnas 3 y 4 de la lista anterior")
    print(OH)
    roundplaces = np.round(OH,decimals=2)
    roundplaces.to_csv(fileOH)

    # Ordenamos las estaciones alfabeticamente 
    oh=pd.read_csv(fileOH, index_col=0, header=0) 
    by_name = oh.sort_values('idEstacion')
    by_name.head()
    print("Datos ordenados por ID de manera alfabetica")
    print(by_name)
    by_name.to_csv(fileOH)

    #Reemplazamos el valor inexistente por posible integración de una estación que no estaba en linea y por lo tanto no esta en el dataframe anterior
    oh=pd.read_csv(fileOH, index_col=False)
    print("Tabla con los datos de  precipitación cada 10 minutos")
    print(oh)
    print("Se reemplaza las celdas de lluvia vacias (NaN) con un cero")
    oh=open(fileOH)
    texto=oh.read()
    print(texto)
    texto1=texto.replace(" ", "0")
    print("Se realiza el ajuste")
    print(texto1)
    oh1=open(fileOH,"w")
    oh1.write(texto1)
    oh.close()
    oh1.close()

    # Se agrega la columna de fecha y hora

    oh=pd.read_csv(fileOH, index_col=False)
    oh['fechaHora']=np.where(oh['lluvia'] !='[]', fecha, ' ', )
    print("Se han agregado los datos de Fecha y hora")
    print(oh)
    oh.to_csv(fileOH)


    # Filtra las columnas para quedarnos solo con estación, lluvia y fecha con hora.
    oh=pd.read_csv(fileOH, usecols=(1, 2, 3), index_col=0, header=0)
    print("Se eliminan las columnas que no son necesarias") 
    print(oh)
    oh.to_csv(fileOH)

    print("DATOS OH OK")
except:
    print("NO SE OBTUVIERON LOS DATOS DE OH")


dircorteorigen=r"C:\Users\meteorologia\Documents\Mapas\SACMEX0.csv"
dircortedestino=r"C:\Users\meteorologia\Documents\Archivos_temporales\SACMEX0.csv"
hora=datetime.now()
local=hora.strftime("%H:%M")
corte1="06:00"
corte2="06:15"
print(corte1 +" "+corte2)

if local < corte2 and local > corte1:
    print ("La hora local esta entre "+corte2+" y "+corte1)
    shutil.copy(dircorteorigen,dircortedestino)
    print("Se ha realizado el corte de datos de SACMEX")
else:
    print("La hora local esta fuera del rango especificado del corte de datos de SACMEX.")

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
    time.sleep(5)
    driver.close()
    print("Se obtuvieron los datos del portal de SACMEX")
except:
    print("No fue posible la descarga de los datos de SACMEX")

dircsvsacmex0 = r'C:\Users\meteorologia\Downloads\SACMEX0.csv'
dircsvsacmex1 = r'C:\Users\meteorologia\Downloads\SACMEX1.csv'
dircsvsacmex2 = r'C:\Users\meteorologia\Documents\Archivos_temporales\SACMEX.csv'
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
    print("Fecha con nombre del mes es"+ messsage)

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
print(sacmex)
sacmex.to_csv(dircsvsacmex2)

time.sleep(5)
remove(dircsvsacmex0)
os.rename(dircsvsacmex1, dircsvsacmex0)

remove(archivo)
print("El archivo .dat de SACMEX ha sido eliminado")