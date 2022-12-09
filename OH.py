from asyncore import read
from os import close, remove, write
import os
import time  
from datetime import datetime
from datetime import date, datetime, timedelta,timezone
import urllib.request
import pandas as pd
import numpy as np
from os import remove



espacio='-------------'
# Insertamos la fecha
now=datetime.now()
fecha=(now.strftime("%d/%m/%y %H:%M"))
print(fecha)

#Se buscan los datos en la web por medio de un request, así mismo se guarda en un csv
print("OH")
print(espacio)
urlOH='https://www.oh-iiunam.mx/geojson/datospaginadia.txt'
fileOH0 = r'C:\Users\meteorologia\Downloads\OH0.csv'
fileOH1 = r'C:\Users\meteorologia\Downloads\OH1.csv'
fileOH2 = r'C:\Users\meteorologia\Documents\Mapas\EMAS\OH.csv'
try:  
    r = urllib.request.urlopen(urlOH)
    f = open(fileOH1,'wb')
    f.write(r.read())
    f.close()
    print('Datos de OH obtenidos')
except:
    print("Se produjo un error al momento de descargar los datos")

# Se hacen algunos cambios dentro del archivo para darle el formato correspondiente al csv y que la libreria pandas lo pueda leer correctamente
oh=open(fileOH1)
texto=oh.read()
texto1=texto.replace(" ", ",")
#print(texto1)
oh1=open(fileOH1,"w")
oh1.write(texto1)
oh.close()
oh1.close()

# Este paso de lectura y guardado solo fue para asignar un indice de forma automatica
oh=pd.read_csv(fileOH1, index_col=False, header=None)
oh.to_csv(fileOH1)

# Se renombran las columnas con ls claves requeridas
oh=pd.read_csv(fileOH1, index_col=0, header=0)
texto1=oh.rename({'2': 'idEstacion'}, axis=1)
texto2=texto1.rename({'3': 'lluvia'}, axis=1)
#print(texto2)
texto2.to_csv(fileOH1)

# Se filtran las columnas y se dejan los valores de lluvia con 2 decimales
OH = pd.read_csv(fileOH1, index_col=0, header=0, usecols=(3,4))
#print(OH)
roundplaces = np.round(OH,decimals=2)
roundplaces.to_csv(fileOH1)
print('Datos de OH obtenidos')


# Ordenamos las estaciones alfabeticamente 
oh=pd.read_csv(fileOH1, index_col=0, header=0) 
by_name = oh.sort_values('idEstacion')
by_name.head()
#print(by_name)
by_name.to_csv(fileOH1)

# Leemos los archivos csv como dataframes

df00=pd.read_csv(fileOH0, index_col=0, header=0)
df01=pd.DataFrame(df00)
#print("archivo 1")
#print(df01)

df10=pd.read_csv(fileOH1, index_col=0, header=0)
df11=pd.DataFrame(df10)
#print("archivo 2")
#print(df11)

# Operación de resta para obtener el valor del acumulado en deacuerdo al programador de tareas (10 minutos)
dfn=df11.sub(df01)
print("resta")
#print(dfn)
dfn.to_csv(fileOH2)

# Se agrega la columna de fecha y hora

oh=pd.read_csv(fileOH2, index_col=False)
oh['fechaHora']=np.where(oh['lluvia'] !='[]', fecha, ' ', )
#print(oh)
oh.to_csv(fileOH2)

oh=pd.read_csv(fileOH2, usecols=(1, 2, 3), index_col=0, header=0) 
print(oh)
oh.to_csv(fileOH2)

time.sleep(5)
remove(fileOH0)
os.rename(fileOH1, fileOH0)