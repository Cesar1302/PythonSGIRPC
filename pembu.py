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

espacio='-------------'

now = datetime.now()

yesterday=now-timedelta(days=1)
print(yesterday)
hoy0=datetime.strftime(now,'%d').lstrip('0')
meshoy0=datetime.strftime(now,'%m')
añohoy0=datetime.strftime(now,'%y')
fecha_hoy0= hoy0 +"/"+ meshoy0 +"/"+ añohoy0
print("la fecha de hoy con un digito es (hoy0) " + fecha_hoy0)

ayer0=datetime.strftime(yesterday,'%d').lstrip('0')
mesayer0=datetime.strftime(yesterday,'%m')
añoayer0=datetime.strftime(yesterday,'%y')
fecha_ayer0= ayer0 +"/"+ mesayer0 +"/"+ añoayer0
print("la fecha de ayer con un digito es (ayer0) " + fecha_ayer0)


hoy1=datetime.strftime(now,'%d')
meshoy1=datetime.strftime(now,'%m')
añohoy1=datetime.strftime(now,'%y')
fecha_hoy1= hoy1 +"/"+ meshoy1 +"/"+ añohoy1
fecha_hoyc= "," + hoy1 +"/"+ meshoy1 +"/"+ añohoy1
print("la fecha de hoy con dos digitos es " + fecha_hoy1)

ayer1=datetime.strftime(yesterday,'%d')
mesayer1=datetime.strftime(yesterday,'%m')
añoayer1=datetime.strftime(yesterday,'%y')
fecha_ayer1= ayer1 +"/"+ mesayer1 +"/"+ añoayer1
fecha_ayerc=  "," + ayer1 +"/"+ mesayer1 +"/"+ añoayer1
print("la fecha de hoy con dos digitos es " + fecha_ayer1)

print("DIRECTORIOS Y LINKS")

dirtxtenp1=r'C:\Users\meteorologia\Downloads\enp1.txt'
dircsvenp1=r'C:\Users\meteorologia\Documents\Mapas\EstacionesSGIRPC\enp1.csv'
urlenp1 = 'https://www.ruoa.unam.mx/pembu/datos/enp1/downld02.txt'

dirtxtenp2=r'C:\Users\meteorologia\Downloads\enp2.txt'
dircsvenp2=r'C:\Users\meteorologia\Documents\Mapas\EstacionesSGIRPC\enp2.csv'
urlenp2 = 'https://www.ruoa.unam.mx/pembu/datos/enp2/downld02.txt'

dirtxtenp3=r'C:\Users\meteorologia\Downloads\enp3.txt'
dircsvenp3=r'C:\Users\meteorologia\Documents\Mapas\EstacionesSGIRPC\enp3.csv'
urlenp3 = 'https://www.ruoa.unam.mx/pembu/datos/enp3/downld02.txt'

dirtxtenp4=r'C:\Users\meteorologia\Downloads\enp4.txt'
dircsvenp4=r'C:\Users\meteorologia\Documents\Mapas\EstacionesSGIRPC\enp4.csv'
urlenp4 = 'https://www.ruoa.unam.mx/pembu/datos/enp4/downld02.txt'

dirtxtenp4=r'C:\Users\meteorologia\Downloads\enp4.txt'
dircsvenp4=r'C:\Users\meteorologia\Documents\Mapas\EstacionesSGIRPC\enp4.csv'
urlenp4 = 'https://www.ruoa.unam.mx/pembu/datos/enp4/downld02.txt'

dirtxtenp5=r'C:\Users\meteorologia\Downloads\enp5.txt'
dircsvenp5=r'C:\Users\meteorologia\Documents\Mapas\EstacionesSGIRPC\enp5.csv'
urlenp5 = 'https://www.ruoa.unam.mx/pembu/datos/enp5/downld02.txt'

dirtxtenp6=r'C:\Users\meteorologia\Downloads\enp6.txt'
dircsvenp6=r'C:\Users\meteorologia\Documents\Mapas\EstacionesSGIRPC\enp6.csv'
urlenp6 = 'https://www.ruoa.unam.mx/pembu/datos/enp6/downld02.txt'

dirtxtenp7=r'C:\Users\meteorologia\Downloads\enp7.txt'
dircsvenp7=r'C:\Users\meteorologia\Documents\Mapas\EstacionesSGIRPC\enp7.csv'
urlenp7 = 'https://www.ruoa.unam.mx/pembu/datos/enp7/downld02.txt'

dirtxtenp8=r'C:\Users\meteorologia\Downloads\enp8.txt'
dircsvenp8=r'C:\Users\meteorologia\Documents\Mapas\EstacionesSGIRPC\enp8.csv'
urlenp8 = 'https://www.ruoa.unam.mx/pembu/datos/enp8/downld02.txt'

dirtxtenp9=r'C:\Users\meteorologia\Downloads\enp9.txt'
dircsvenp9=r'C:\Users\meteorologia\Documents\Mapas\EstacionesSGIRPC\enp9.csv'
urlenp9 = 'https://www.ruoa.unam.mx/pembu/datos/enp9/downld02.txt'

dirtxtccha=r'C:\Users\meteorologia\Downloads\ccha.txt'
dircsvccha=r'C:\Users\meteorologia\Documents\Mapas\EstacionesSGIRPC\ccha.csv'
urlccha = 'https://www.ruoa.unam.mx/pembu/datos/ccha/downld02.txt'


dirtxtcchn=r'C:\Users\meteorologia\Downloads\cchn.txt'
dircsvcchn=r'C:\Users\meteorologia\Documents\Mapas\EstacionesSGIRPC\cchn.csv'
urlcchn = 'https://www.ruoa.unam.mx/pembu/datos/cchn/downld02.txt'

dirtxtccho=r'C:\Users\meteorologia\Downloads\ccho.txt'
dircsvccho=r'C:\Users\meteorologia\Documents\Mapas\EstacionesSGIRPC\ccho.csv'
urlccho = 'https://www.ruoa.unam.mx/pembu/datos/ccho/downld02.txt'

dirtxtcchs=r'C:\Users\meteorologia\Downloads\cchs.txt'
dircsvcchs=r'C:\Users\meteorologia\Documents\Mapas\EstacionesSGIRPC\cchs.csv'
urlcchs = 'https://www.ruoa.unam.mx/pembu/datos/cchs/downld02.txt'

dirtxtcchv=r'C:\Users\meteorologia\Downloads\cchv.txt'
dircsvcchv=r'C:\Users\meteorologia\Documents\Mapas\EstacionesSGIRPC\cchv.csv'
urlcchv = 'https://www.ruoa.unam.mx/pembu/datos/cchv/downld02.txt'

dirtxtICAyCC=r'C:\Users\meteorologia\Downloads\ICAyCC.txt'
dircsvICAyCC=r'C:\Users\meteorologia\Documents\Mapas\EstacionesSGIRPC\ICAyCC.csv'
urlICAyCC = 'https://www.ruoa.unam.mx/pembu/datos/ICAyCC/downld02.txt'

print('enp1')
try:
    print(espacio)
    file1 = dirtxtenp1
    r = urllib.request.urlopen(urlenp1)
    f = open(file1,'wb')
    f.write(r.read())
    f.close()
    #print(file1)
    print('Datos de la estación enp1 obtenidos')

    try:
        with open(dirtxtenp1, 'r') as fr:
            # reading line by line
            lines = fr.readlines()

            # pointer for position
            ptr = 1

            # opening in writing mode
            with open(dirtxtenp1, 'w') as fw:
                for line in lines:

                    # we want to remove 5th line
                    if ptr != 1:
                        fw.write(line)
                    ptr += 1
        print("Deleted")

    except:
        print("Oops! No se pudo eliminar fila")

    try:
        with open(dirtxtenp1, 'r') as fr:
            # reading line by line
            lines = fr.readlines()

            # pointer for position
            ptr = 1

            # opening in writing mode
            with open(dirtxtenp1, 'w') as fw:
                for line in lines:

                    # we want to remove 5th line
                    if ptr != 2:
                        fw.write(line)
                    ptr += 1
        print("Deleted")

    except:
        print("Oops! No se pudo eliminar fila")


    enp1=open(dirtxtenp1)
    texto0=enp1.read()
    texto1=texto0.replace(" ",",")
    texto2=texto1.replace("---","9999")
    texto3=texto2.replace(",,",",")
    texto4=texto3.replace(",,,",",")
    texto5=texto4.replace(",,,,",",")
    texto6=texto5.replace(fecha_ayer0,fecha_ayerc)
    texto7=texto6.replace(fecha_hoy0,fecha_hoyc)
    #print(texto7)
    enp11=open(dirtxtenp1,"w")
    enp11.write(texto7)
    enp11.close()

    enp1=open(dirtxtenp1)
    texto=enp1.read()
    texto0=texto.replace("12:00a","00:00")
    texto1=texto0.replace("12:10a","00:10")
    texto2=texto1.replace("12:20a","00:20")
    texto3=texto2.replace("12:30a","00:30")
    texto4=texto3.replace("12:40a","00:40")
    texto5=texto4.replace("12:50a","00:50")
    texto6=texto5.replace("1:00a","1:00")
    texto7=texto6.replace("1:10a","1:10")
    texto8=texto7.replace("1:20a","1:20")
    texto9=texto8.replace("1:30a","1:30")
    texto10=texto9.replace("1:40a","1:40")
    texto11=texto10.replace("1:50a","1:50")
    texto12=texto11.replace("2:00a","2:00")
    texto13=texto12.replace("2:10a","2:10")
    texto14=texto13.replace("2:20a","2:20")
    texto15=texto14.replace("2:30a","2:30")
    texto16=texto15.replace("2:40a","2:40")
    texto17=texto16.replace("2:50a","2:50")
    texto18=texto17.replace("3:00a","3:00")
    texto19=texto18.replace("3:10a","3:10")
    texto20=texto19.replace("3:20a","3:20")
    texto21=texto20.replace("3:30a","3:30")
    texto22=texto21.replace("3:40a","3:40")
    texto23=texto22.replace("3:50a","3:50")
    texto24=texto23.replace("4:00a","4:00")
    texto25=texto24.replace("4:10a","4:10")
    texto26=texto25.replace("4:20a","4:20")
    texto27=texto26.replace("4:30a","4:30")
    texto28=texto27.replace("4:40a","4:40")
    texto29=texto28.replace("4:50a","4:50")
    texto30=texto29.replace("5:00a","5:00")
    texto31=texto30.replace("5:10a","5:10")
    texto32=texto31.replace("5:20a","5:20")
    texto33=texto32.replace("5:30a","5:30")
    texto34=texto33.replace("5:40a","5:40")
    texto35=texto34.replace("5:50a","5:50")
    texto36=texto35.replace("6:00a","6:00")
    texto37=texto36.replace("6:10a","6:10")
    texto38=texto37.replace("6:20a","6:20")
    texto39=texto38.replace("6:30a","6:30")
    texto40=texto39.replace("6:40a","6:40")
    texto41=texto40.replace("6:50a","6:50")
    texto42=texto41.replace("7:00a","7:00")
    texto43=texto42.replace("7:10a","7:10")
    texto44=texto43.replace("7:20a","7:20")
    texto45=texto44.replace("7:30a","7:30")
    texto46=texto45.replace("7:40a","7:40")
    texto47=texto46.replace("7:50a","7:50")
    texto48=texto47.replace("8:00a","8:00")
    texto49=texto48.replace("8:10a","8:10")
    texto50=texto49.replace("8:20a","8:20")
    texto51=texto50.replace("8:30a","8:30")
    texto52=texto51.replace("8:40a","8:40")
    texto53=texto52.replace("8:50a","8:50")
    texto54=texto53.replace("9:00a","9:00")
    texto55=texto54.replace("9:10a","9:10")
    texto56=texto55.replace("9:20a","9:20")
    texto57=texto56.replace("9:30a","9:30")
    texto58=texto57.replace("9:40a","9:40")
    texto59=texto58.replace("9:50a","9:50")
    texto60=texto59.replace("10:00a","10:00")
    texto61=texto60.replace("10:10a","10:10")
    texto62=texto61.replace("10:20a","10:20")
    texto63=texto62.replace("10:30a","10:30")
    texto64=texto63.replace("10:40a","10:40")
    texto65=texto64.replace("10:50a","10:50")
    texto66=texto65.replace("11:00a","11:00")
    texto67=texto66.replace("11:10a","11:10")
    texto68=texto67.replace("11:20a","11:20")
    texto69=texto68.replace("11:30a","11:30")
    texto70=texto69.replace("11:40a","11:40")
    texto71=texto70.replace("11:50a","11:50")
    texto72=texto71.replace("12:00p","12:00")
    texto73=texto72.replace("12:10p","12:10")
    texto74=texto73.replace("12:20p","12:20")
    texto75=texto74.replace("12:30p","12:30")
    texto76=texto75.replace("12:40p","12:40")
    texto77=texto76.replace("12:50p","12:50")
    texto78=texto77.replace("1:00p","13:00")
    texto79=texto78.replace("1:10p","13:10")
    texto80=texto79.replace("1:20p","13:20")
    texto81=texto80.replace("1:30p","13:30")
    texto82=texto81.replace("1:40p","13:40")
    texto83=texto82.replace("1:50p","13:50")
    texto84=texto83.replace("2:00p","14:00")
    texto85=texto84.replace("2:10p","14:10")
    texto86=texto85.replace("2:20p","14:20")
    texto87=texto86.replace("2:30p","14:30")
    texto88=texto87.replace("2:40p","14:40")
    texto89=texto88.replace("2:50p","14:50")
    texto90=texto89.replace("3:00p","15:00")
    texto91=texto90.replace("3:10p","15:10")
    texto92=texto91.replace("3:20p","15:20")
    texto93=texto92.replace("3:30p","15:30")
    texto94=texto93.replace("3:40p","15:40")
    texto95=texto94.replace("3:50p","15:50")
    texto96=texto95.replace("4:00p","16:00")
    texto97=texto96.replace("4:10p","16:10")
    texto98=texto97.replace("4:20p","16:20")
    texto99=texto98.replace("4:30p","16:30")
    texto100=texto99.replace("4:40p","16:40")
    texto11=texto100.replace("4:50p","16:50")
    texto12=texto11.replace("5:00p","17:00")
    texto13=texto12.replace("5:10p","17:10")
    texto14=texto13.replace("5:20p","17:20")
    texto15=texto14.replace("5:30p","17:30")
    texto16=texto15.replace("5:40p","17:40")
    texto17=texto16.replace("5:50p","17:50")
    texto18=texto17.replace("6:00p","18:00")
    texto19=texto18.replace("6:10p","18:10")
    texto110=texto19.replace("6:20p","18:20")
    texto111=texto110.replace("6:30p","18:30")
    texto112=texto111.replace("6:40p","18:40")
    texto113=texto112.replace("6:50p","18:50")
    texto114=texto113.replace("7:00p","19:00")
    texto115=texto114.replace("7:10p","19:10")
    texto116=texto115.replace("7:20p","19:20")
    texto117=texto116.replace("7:30p","19:30")
    texto118=texto117.replace("7:40p","19:40")
    texto119=texto118.replace("7:50p","19:50")
    texto120=texto119.replace("8:00p","20:00")
    texto121=texto120.replace("8:10p","20:10")
    texto122=texto121.replace("8:20p","20:20")
    texto123=texto122.replace("8:30p","20:30")
    texto124=texto123.replace("8:40p","20:40")
    texto125=texto124.replace("8:50p","20:50")
    texto126=texto125.replace("9:00p","21:00")
    texto127=texto126.replace("9:10p","21:10")
    texto128=texto127.replace("9:20p","21:20")
    texto129=texto128.replace("9:30p","21:30")
    texto130=texto129.replace("9:40p","21:40")
    texto131=texto130.replace("9:50p","21:50")
    texto132=texto131.replace("10:00p","22:00")
    texto133=texto132.replace("10:10p","22:10")
    texto134=texto133.replace("10:20p","22:20")
    texto135=texto134.replace("10:30p","22:30")
    texto136=texto135.replace("10:40p","22:40")
    texto137=texto136.replace("10:50p","22:50")
    texto138=texto137.replace("11:00p","23:00")
    texto139=texto138.replace("11:10p","23:10")
    texto140=texto139.replace("11:20p","23:20")
    texto141=texto140.replace("11:30p","23:30")
    texto142=texto141.replace("11:40p","23:40")
    texto143=texto142.replace("11:50p","23:50")
    texto144=texto143.replace("113:00","23:00")
    texto145=texto144.replace("113:10","23:10")
    texto146=texto145.replace("113:20","23:20")
    texto147=texto146.replace("113:30","23:30")
    texto148=texto147.replace("113:40","23:40")
    texto149=texto148.replace("113:50","23:50")
    enp11=open(dirtxtenp1,"w")
    enp11.write(texto149)
    enp11.close()
    enp1.close()

    enp1=open(dirtxtenp1)
    texto0=enp1.read()
    texto1=texto0.replace(",,",",")
    texto2=texto1.replace(",Date",",Fecha")
    enp11=open(dircsvenp1,"w")
    enp11.write(texto2)
    #print(texto2)
    enp11.close()
    enp1.close()

    enp1=pd.read_csv(dircsvenp1, usecols=(1,2,3,6,7,8,10,11,17,18,23), index_col=0, header=0)
    #print(enp1)
    enp1.to_csv(dircsvenp1)


    enp1=open(dircsvenp1)
    nombrescol=enp1.read()
    texto1=nombrescol.replace("Out","temperatura")
    texto2=texto1.replace("Hum","humedadRelativa")
    texto3=texto2.replace("Pt.","puntoRocio")
    texto4=texto3.replace("Speed.1","velocidadRacha")
    texto5=texto4.replace("Dir.1","direccionRacha")
    texto6=texto5.replace("Speed","velocidadViento")
    texto7=texto6.replace("Dir","direccionViento")
    texto8=texto7.replace("Bar","presionBar")
    texto9=texto8.replace("Rain","lluvia")
    texto10=texto9.replace("Index.3","UV")

    enp11=open(dircsvenp1,"w")
    enp11.write(texto10)
    enp11.close()
    enp1.close()

    enp1=open(dircsvenp1)
    texto=enp1.read()
    texto1=texto.replace("NNE","22.5")
    texto2=texto1.replace("ENE","67.5")
    texto3=texto2.replace("ESE","112.5")
    texto4=texto3.replace("SSE","157.5")
    texto5=texto4.replace("SSW","202.5")
    texto6=texto5.replace("WSW","247.5")
    texto7=texto6.replace("WNW","292.5")
    texto8=texto7.replace("NNW","337.5")
    texto9=texto8.replace("NE","45")
    texto10=texto9.replace("SE","135")
    texto11=texto10.replace("SW","225")
    texto12=texto11.replace("NW","315")
    enp11=open(dircsvenp1,"w")
    enp11.write(texto12)
    enp11.close()
    enp1.close()

    enp1=open(dircsvenp1)
    texto=enp1.read()
    texto1=texto.replace("N","360")
    texto2=texto1.replace("E","90")
    texto3=texto2.replace("S","180")
    texto4=texto3.replace("W","270")
    enp11=open(dircsvenp1,"w")
    enp11.write(texto4)
    enp11.close()
    enp1.close()

    enp1=pd.read_csv(dircsvenp1, index_col=0, header=0)
    #print(enp1)
    enp1['fechaHora']=enp1['Fecha'].map(str)  + ' ' + enp1['Time'].map(str)
    enp1
    #print(enp1)
    enp1.to_csv(dircsvenp1)


    DF=pd.read_csv(dircsvenp1, index_col=0)
    DF['idEstacion']=np.where(DF['Time'] !='[]', 'enp1', ' ', )
    #print(DF)
    DF.to_csv(dircsvenp1)

    enp1=pd.read_csv(dircsvenp1, usecols=(3,4,5,6,7,8,9,10,11,12,13), index_col=0, header=0)
    #print(enp1)
    enp1.to_csv(dircsvenp1)


    # try:
    #     enp1=pd.read_csv(dircsvenp1, index_col=0)
    #     filter= (enp1['fechaHora'] <= fecha_ayer1) & (enp1['fechaHora'] < fecha_hoy1)
    #     filtrado=enp1.loc[filter]
    #     #print(filtrado)
    #     filtrado.to_csv(dircsvenp1)
    #     print("Filtrado")
    # except:
    #     print("No se logro filtrar datos por fecha actual")


    print('Datos de la estación enp1 listos')
except:
    print("No se logro obtener datos de la estación enp1")
    remove(dircsvenp1)

print('enp2')
try:
    print(espacio)
    file1 = dirtxtenp2
    r = urllib.request.urlopen(urlenp2)
    f = open(file1,'wb')
    f.write(r.read())
    f.close()
    #print(file1)
    print('Datos de la estación enp2 obtenidos')

    try:
        with open(dirtxtenp2, 'r') as fr:
            # reading line by line
            lines = fr.readlines()

            # pointer for position
            ptr = 1

            # opening in writing mode
            with open(dirtxtenp2, 'w') as fw:
                for line in lines:

                    # we want to remove 5th line
                    if ptr != 1:
                        fw.write(line)
                    ptr += 1
        print("Deleted")

    except:
        print("Oops! No se pudo eliminar fila")

    try:
        with open(dirtxtenp2, 'r') as fr:
            # reading line by line
            lines = fr.readlines()

            # pointer for position
            ptr = 1

            # opening in writing mode
            with open(dirtxtenp2, 'w') as fw:
                for line in lines:

                    # we want to remove 5th line
                    if ptr != 2:
                        fw.write(line)
                    ptr += 1
        print("Deleted")

    except:
        print("Oops! No se pudo eliminar fila")


    enp2=open(dirtxtenp2)
    texto0=enp2.read()
    texto1=texto0.replace(" ",",")
    texto2=texto1.replace("---","9999")
    texto3=texto2.replace(",,",",")
    texto4=texto3.replace(",,,",",")
    texto5=texto4.replace(",,,,",",")
    texto6=texto5.replace(fecha_ayer0,fecha_ayerc)
    texto7=texto6.replace(fecha_hoy0,fecha_hoyc)
    #print(texto7)
    enp21=open(dirtxtenp2,"w")
    enp21.write(texto7)
    enp21.close()

    enp2=open(dirtxtenp2)
    texto=enp2.read()
    texto0=texto.replace("12:00a","00:00")
    texto1=texto0.replace("12:10a","00:10")
    texto2=texto1.replace("12:20a","00:20")
    texto3=texto2.replace("12:30a","00:30")
    texto4=texto3.replace("12:40a","00:40")
    texto5=texto4.replace("12:50a","00:50")
    texto6=texto5.replace("1:00a","1:00")
    texto7=texto6.replace("1:10a","1:10")
    texto8=texto7.replace("1:20a","1:20")
    texto9=texto8.replace("1:30a","1:30")
    texto10=texto9.replace("1:40a","1:40")
    texto11=texto10.replace("1:50a","1:50")
    texto12=texto11.replace("2:00a","2:00")
    texto13=texto12.replace("2:10a","2:10")
    texto14=texto13.replace("2:20a","2:20")
    texto15=texto14.replace("2:30a","2:30")
    texto16=texto15.replace("2:40a","2:40")
    texto17=texto16.replace("2:50a","2:50")
    texto18=texto17.replace("3:00a","3:00")
    texto19=texto18.replace("3:10a","3:10")
    texto20=texto19.replace("3:20a","3:20")
    texto21=texto20.replace("3:30a","3:30")
    texto22=texto21.replace("3:40a","3:40")
    texto23=texto22.replace("3:50a","3:50")
    texto24=texto23.replace("4:00a","4:00")
    texto25=texto24.replace("4:10a","4:10")
    texto26=texto25.replace("4:20a","4:20")
    texto27=texto26.replace("4:30a","4:30")
    texto28=texto27.replace("4:40a","4:40")
    texto29=texto28.replace("4:50a","4:50")
    texto30=texto29.replace("5:00a","5:00")
    texto31=texto30.replace("5:10a","5:10")
    texto32=texto31.replace("5:20a","5:20")
    texto33=texto32.replace("5:30a","5:30")
    texto34=texto33.replace("5:40a","5:40")
    texto35=texto34.replace("5:50a","5:50")
    texto36=texto35.replace("6:00a","6:00")
    texto37=texto36.replace("6:10a","6:10")
    texto38=texto37.replace("6:20a","6:20")
    texto39=texto38.replace("6:30a","6:30")
    texto40=texto39.replace("6:40a","6:40")
    texto41=texto40.replace("6:50a","6:50")
    texto42=texto41.replace("7:00a","7:00")
    texto43=texto42.replace("7:10a","7:10")
    texto44=texto43.replace("7:20a","7:20")
    texto45=texto44.replace("7:30a","7:30")
    texto46=texto45.replace("7:40a","7:40")
    texto47=texto46.replace("7:50a","7:50")
    texto48=texto47.replace("8:00a","8:00")
    texto49=texto48.replace("8:10a","8:10")
    texto50=texto49.replace("8:20a","8:20")
    texto51=texto50.replace("8:30a","8:30")
    texto52=texto51.replace("8:40a","8:40")
    texto53=texto52.replace("8:50a","8:50")
    texto54=texto53.replace("9:00a","9:00")
    texto55=texto54.replace("9:10a","9:10")
    texto56=texto55.replace("9:20a","9:20")
    texto57=texto56.replace("9:30a","9:30")
    texto58=texto57.replace("9:40a","9:40")
    texto59=texto58.replace("9:50a","9:50")
    texto60=texto59.replace("10:00a","10:00")
    texto61=texto60.replace("10:10a","10:10")
    texto62=texto61.replace("10:20a","10:20")
    texto63=texto62.replace("10:30a","10:30")
    texto64=texto63.replace("10:40a","10:40")
    texto65=texto64.replace("10:50a","10:50")
    texto66=texto65.replace("11:00a","11:00")
    texto67=texto66.replace("11:10a","11:10")
    texto68=texto67.replace("11:20a","11:20")
    texto69=texto68.replace("11:30a","11:30")
    texto70=texto69.replace("11:40a","11:40")
    texto71=texto70.replace("11:50a","11:50")
    texto72=texto71.replace("12:00p","12:00")
    texto73=texto72.replace("12:10p","12:10")
    texto74=texto73.replace("12:20p","12:20")
    texto75=texto74.replace("12:30p","12:30")
    texto76=texto75.replace("12:40p","12:40")
    texto77=texto76.replace("12:50p","12:50")
    texto78=texto77.replace("1:00p","13:00")
    texto79=texto78.replace("1:10p","13:10")
    texto80=texto79.replace("1:20p","13:20")
    texto81=texto80.replace("1:30p","13:30")
    texto82=texto81.replace("1:40p","13:40")
    texto83=texto82.replace("1:50p","13:50")
    texto84=texto83.replace("2:00p","14:00")
    texto85=texto84.replace("2:10p","14:10")
    texto86=texto85.replace("2:20p","14:20")
    texto87=texto86.replace("2:30p","14:30")
    texto88=texto87.replace("2:40p","14:40")
    texto89=texto88.replace("2:50p","14:50")
    texto90=texto89.replace("3:00p","15:00")
    texto91=texto90.replace("3:10p","15:10")
    texto92=texto91.replace("3:20p","15:20")
    texto93=texto92.replace("3:30p","15:30")
    texto94=texto93.replace("3:40p","15:40")
    texto95=texto94.replace("3:50p","15:50")
    texto96=texto95.replace("4:00p","16:00")
    texto97=texto96.replace("4:10p","16:10")
    texto98=texto97.replace("4:20p","16:20")
    texto99=texto98.replace("4:30p","16:30")
    texto100=texto99.replace("4:40p","16:40")
    texto11=texto100.replace("4:50p","16:50")
    texto12=texto11.replace("5:00p","17:00")
    texto13=texto12.replace("5:10p","17:10")
    texto14=texto13.replace("5:20p","17:20")
    texto15=texto14.replace("5:30p","17:30")
    texto16=texto15.replace("5:40p","17:40")
    texto17=texto16.replace("5:50p","17:50")
    texto18=texto17.replace("6:00p","18:00")
    texto19=texto18.replace("6:10p","18:10")
    texto110=texto19.replace("6:20p","18:20")
    texto111=texto110.replace("6:30p","18:30")
    texto112=texto111.replace("6:40p","18:40")
    texto113=texto112.replace("6:50p","18:50")
    texto114=texto113.replace("7:00p","19:00")
    texto115=texto114.replace("7:10p","19:10")
    texto116=texto115.replace("7:20p","19:20")
    texto117=texto116.replace("7:30p","19:30")
    texto118=texto117.replace("7:40p","19:40")
    texto119=texto118.replace("7:50p","19:50")
    texto120=texto119.replace("8:00p","20:00")
    texto121=texto120.replace("8:10p","20:10")
    texto122=texto121.replace("8:20p","20:20")
    texto123=texto122.replace("8:30p","20:30")
    texto124=texto123.replace("8:40p","20:40")
    texto125=texto124.replace("8:50p","20:50")
    texto126=texto125.replace("9:00p","21:00")
    texto127=texto126.replace("9:10p","21:10")
    texto128=texto127.replace("9:20p","21:20")
    texto129=texto128.replace("9:30p","21:30")
    texto130=texto129.replace("9:40p","21:40")
    texto131=texto130.replace("9:50p","21:50")
    texto132=texto131.replace("10:00p","22:00")
    texto133=texto132.replace("10:10p","22:10")
    texto134=texto133.replace("10:20p","22:20")
    texto135=texto134.replace("10:30p","22:30")
    texto136=texto135.replace("10:40p","22:40")
    texto137=texto136.replace("10:50p","22:50")
    texto138=texto137.replace("11:00p","23:00")
    texto139=texto138.replace("11:10p","23:10")
    texto140=texto139.replace("11:20p","23:20")
    texto141=texto140.replace("11:30p","23:30")
    texto142=texto141.replace("11:40p","23:40")
    texto143=texto142.replace("11:50p","23:50")
    texto144=texto143.replace("113:00","23:00")
    texto145=texto144.replace("113:10","23:10")
    texto146=texto145.replace("113:20","23:20")
    texto147=texto146.replace("113:30","23:30")
    texto148=texto147.replace("113:40","23:40")
    texto149=texto148.replace("113:50","23:50")
    enp21=open(dirtxtenp2,"w")
    enp21.write(texto149)
    enp21.close()
    enp2.close()

    enp2=open(dirtxtenp2)
    texto0=enp2.read()
    texto1=texto0.replace(",,",",")
    texto2=texto1.replace(",Date",",Fecha")
    enp21=open(dircsvenp2,"w")
    enp21.write(texto2)
    #print(texto2)
    enp21.close()
    enp2.close()

    enp2=pd.read_csv(dircsvenp2, usecols=(1,2,3,6,7,8,10,11,17,18,23), index_col=0, header=0)
    #print(enp2)
    enp2.to_csv(dircsvenp2)


    enp2=open(dircsvenp2)
    nombrescol=enp2.read()
    texto1=nombrescol.replace("Out","temperatura")
    texto2=texto1.replace("Hum","humedadRelativa")
    texto3=texto2.replace("Pt.","puntoRocio")
    texto4=texto3.replace("Speed.1","velocidadRacha")
    texto5=texto4.replace("Dir.1","direccionRacha")
    texto6=texto5.replace("Speed","velocidadViento")
    texto7=texto6.replace("Dir","direccionViento")
    texto8=texto7.replace("Bar","presionBar")
    texto9=texto8.replace("Rain","lluvia")
    texto10=texto9.replace("Index.3","UV")

    enp21=open(dircsvenp2,"w")
    enp21.write(texto10)
    enp21.close()
    enp2.close()

    enp2=open(dircsvenp2)
    texto=enp2.read()
    texto1=texto.replace("NNE","22.5")
    texto2=texto1.replace("ENE","67.5")
    texto3=texto2.replace("ESE","112.5")
    texto4=texto3.replace("SSE","157.5")
    texto5=texto4.replace("SSW","202.5")
    texto6=texto5.replace("WSW","247.5")
    texto7=texto6.replace("WNW","292.5")
    texto8=texto7.replace("NNW","337.5")
    texto9=texto8.replace("NE","45")
    texto10=texto9.replace("SE","135")
    texto11=texto10.replace("SW","225")
    texto12=texto11.replace("NW","315")
    enp21=open(dircsvenp2,"w")
    enp21.write(texto12)
    enp21.close()
    enp2.close()

    enp2=open(dircsvenp2)
    texto=enp2.read()
    texto1=texto.replace("N","360")
    texto2=texto1.replace("E","90")
    texto3=texto2.replace("S","180")
    texto4=texto3.replace("W","270")
    enp21=open(dircsvenp2,"w")
    enp21.write(texto4)
    enp21.close()
    enp2.close()

    enp2=pd.read_csv(dircsvenp2, index_col=0, header=0)
    #print(enp2)
    enp2['fechaHora']=enp2['Fecha'].map(str)  + ' ' + enp2['Time'].map(str)
    enp2
    #print(enp2)
    enp2.to_csv(dircsvenp2)


    DF=pd.read_csv(dircsvenp2, index_col=0)
    DF['idEstacion']=np.where(DF['Time'] !='[]', 'enp2', ' ', )
    #print(DF)
    DF.to_csv(dircsvenp2)

    enp2=pd.read_csv(dircsvenp2, usecols=(3,4,5,6,7,8,9,10,11,12,13), index_col=0, header=0)
    #print(enp2)
    enp2.to_csv(dircsvenp2)


    # try:
    #     enp2=pd.read_csv(dircsvenp2, index_col=0)
    #     filter= (enp2['fechaHora'] <= fecha_ayer1) & (enp2['fechaHora'] < fecha_hoy1)
    #     filtrado=enp2.loc[filter]
    #     #print(filtrado)
    #     filtrado.to_csv(dircsvenp2)
    #     print("Filtrado")
    # except:
    #     print("No se logro filtrar datos por fecha actual")


    print('Datos de la estación enp2 listos')
except:
    print("No se logro obtener datos de la estación enp2")
    remove(dircsvenp2)

print('enp3')
try:
    print(espacio)
    file1 = dirtxtenp3
    r = urllib.request.urlopen(urlenp3)
    f = open(file1,'wb')
    f.write(r.read())
    f.close()
    #print(file1)
    print('Datos de la estación enp3 obtenidos')

    try:
        with open(dirtxtenp3, 'r') as fr:
            # reading line by line
            lines = fr.readlines()

            # pointer for position
            ptr = 1

            # opening in writing mode
            with open(dirtxtenp3, 'w') as fw:
                for line in lines:

                    # we want to remove 5th line
                    if ptr != 1:
                        fw.write(line)
                    ptr += 1
        print("Deleted")

    except:
        print("Oops! No se pudo eliminar fila")

    try:
        with open(dirtxtenp3, 'r') as fr:
            # reading line by line
            lines = fr.readlines()

            # pointer for position
            ptr = 1

            # opening in writing mode
            with open(dirtxtenp3, 'w') as fw:
                for line in lines:

                    # we want to remove 5th line
                    if ptr != 2:
                        fw.write(line)
                    ptr += 1
        print("Deleted")

    except:
        print("Oops! No se pudo eliminar fila")


    enp3=open(dirtxtenp3)
    texto0=enp3.read()
    texto1=texto0.replace(" ",",")
    texto2=texto1.replace("---","9999")
    texto3=texto2.replace(",,",",")
    texto4=texto3.replace(",,,",",")
    texto5=texto4.replace(",,,,",",")
    texto6=texto5.replace(fecha_ayer0,fecha_ayerc)
    texto7=texto6.replace(fecha_hoy0,fecha_hoyc)
    #print(texto7)
    enp31=open(dirtxtenp3,"w")
    enp31.write(texto7)
    enp31.close()

    enp3=open(dirtxtenp3)
    texto=enp3.read()
    texto0=texto.replace("12:00a","00:00")
    texto1=texto0.replace("12:10a","00:10")
    texto2=texto1.replace("12:20a","00:20")
    texto3=texto2.replace("12:30a","00:30")
    texto4=texto3.replace("12:40a","00:40")
    texto5=texto4.replace("12:50a","00:50")
    texto6=texto5.replace("1:00a","1:00")
    texto7=texto6.replace("1:10a","1:10")
    texto8=texto7.replace("1:20a","1:20")
    texto9=texto8.replace("1:30a","1:30")
    texto10=texto9.replace("1:40a","1:40")
    texto11=texto10.replace("1:50a","1:50")
    texto12=texto11.replace("2:00a","2:00")
    texto13=texto12.replace("2:10a","2:10")
    texto14=texto13.replace("2:20a","2:20")
    texto15=texto14.replace("2:30a","2:30")
    texto16=texto15.replace("2:40a","2:40")
    texto17=texto16.replace("2:50a","2:50")
    texto18=texto17.replace("3:00a","3:00")
    texto19=texto18.replace("3:10a","3:10")
    texto20=texto19.replace("3:20a","3:20")
    texto21=texto20.replace("3:30a","3:30")
    texto22=texto21.replace("3:40a","3:40")
    texto23=texto22.replace("3:50a","3:50")
    texto24=texto23.replace("4:00a","4:00")
    texto25=texto24.replace("4:10a","4:10")
    texto26=texto25.replace("4:20a","4:20")
    texto27=texto26.replace("4:30a","4:30")
    texto28=texto27.replace("4:40a","4:40")
    texto29=texto28.replace("4:50a","4:50")
    texto30=texto29.replace("5:00a","5:00")
    texto31=texto30.replace("5:10a","5:10")
    texto32=texto31.replace("5:20a","5:20")
    texto33=texto32.replace("5:30a","5:30")
    texto34=texto33.replace("5:40a","5:40")
    texto35=texto34.replace("5:50a","5:50")
    texto36=texto35.replace("6:00a","6:00")
    texto37=texto36.replace("6:10a","6:10")
    texto38=texto37.replace("6:20a","6:20")
    texto39=texto38.replace("6:30a","6:30")
    texto40=texto39.replace("6:40a","6:40")
    texto41=texto40.replace("6:50a","6:50")
    texto42=texto41.replace("7:00a","7:00")
    texto43=texto42.replace("7:10a","7:10")
    texto44=texto43.replace("7:20a","7:20")
    texto45=texto44.replace("7:30a","7:30")
    texto46=texto45.replace("7:40a","7:40")
    texto47=texto46.replace("7:50a","7:50")
    texto48=texto47.replace("8:00a","8:00")
    texto49=texto48.replace("8:10a","8:10")
    texto50=texto49.replace("8:20a","8:20")
    texto51=texto50.replace("8:30a","8:30")
    texto52=texto51.replace("8:40a","8:40")
    texto53=texto52.replace("8:50a","8:50")
    texto54=texto53.replace("9:00a","9:00")
    texto55=texto54.replace("9:10a","9:10")
    texto56=texto55.replace("9:20a","9:20")
    texto57=texto56.replace("9:30a","9:30")
    texto58=texto57.replace("9:40a","9:40")
    texto59=texto58.replace("9:50a","9:50")
    texto60=texto59.replace("10:00a","10:00")
    texto61=texto60.replace("10:10a","10:10")
    texto62=texto61.replace("10:20a","10:20")
    texto63=texto62.replace("10:30a","10:30")
    texto64=texto63.replace("10:40a","10:40")
    texto65=texto64.replace("10:50a","10:50")
    texto66=texto65.replace("11:00a","11:00")
    texto67=texto66.replace("11:10a","11:10")
    texto68=texto67.replace("11:20a","11:20")
    texto69=texto68.replace("11:30a","11:30")
    texto70=texto69.replace("11:40a","11:40")
    texto71=texto70.replace("11:50a","11:50")
    texto72=texto71.replace("12:00p","12:00")
    texto73=texto72.replace("12:10p","12:10")
    texto74=texto73.replace("12:20p","12:20")
    texto75=texto74.replace("12:30p","12:30")
    texto76=texto75.replace("12:40p","12:40")
    texto77=texto76.replace("12:50p","12:50")
    texto78=texto77.replace("1:00p","13:00")
    texto79=texto78.replace("1:10p","13:10")
    texto80=texto79.replace("1:20p","13:20")
    texto81=texto80.replace("1:30p","13:30")
    texto82=texto81.replace("1:40p","13:40")
    texto83=texto82.replace("1:50p","13:50")
    texto84=texto83.replace("2:00p","14:00")
    texto85=texto84.replace("2:10p","14:10")
    texto86=texto85.replace("2:20p","14:20")
    texto87=texto86.replace("2:30p","14:30")
    texto88=texto87.replace("2:40p","14:40")
    texto89=texto88.replace("2:50p","14:50")
    texto90=texto89.replace("3:00p","15:00")
    texto91=texto90.replace("3:10p","15:10")
    texto92=texto91.replace("3:20p","15:20")
    texto93=texto92.replace("3:30p","15:30")
    texto94=texto93.replace("3:40p","15:40")
    texto95=texto94.replace("3:50p","15:50")
    texto96=texto95.replace("4:00p","16:00")
    texto97=texto96.replace("4:10p","16:10")
    texto98=texto97.replace("4:20p","16:20")
    texto99=texto98.replace("4:30p","16:30")
    texto100=texto99.replace("4:40p","16:40")
    texto11=texto100.replace("4:50p","16:50")
    texto12=texto11.replace("5:00p","17:00")
    texto13=texto12.replace("5:10p","17:10")
    texto14=texto13.replace("5:20p","17:20")
    texto15=texto14.replace("5:30p","17:30")
    texto16=texto15.replace("5:40p","17:40")
    texto17=texto16.replace("5:50p","17:50")
    texto18=texto17.replace("6:00p","18:00")
    texto19=texto18.replace("6:10p","18:10")
    texto110=texto19.replace("6:20p","18:20")
    texto111=texto110.replace("6:30p","18:30")
    texto112=texto111.replace("6:40p","18:40")
    texto113=texto112.replace("6:50p","18:50")
    texto114=texto113.replace("7:00p","19:00")
    texto115=texto114.replace("7:10p","19:10")
    texto116=texto115.replace("7:20p","19:20")
    texto117=texto116.replace("7:30p","19:30")
    texto118=texto117.replace("7:40p","19:40")
    texto119=texto118.replace("7:50p","19:50")
    texto120=texto119.replace("8:00p","20:00")
    texto121=texto120.replace("8:10p","20:10")
    texto122=texto121.replace("8:20p","20:20")
    texto123=texto122.replace("8:30p","20:30")
    texto124=texto123.replace("8:40p","20:40")
    texto125=texto124.replace("8:50p","20:50")
    texto126=texto125.replace("9:00p","21:00")
    texto127=texto126.replace("9:10p","21:10")
    texto128=texto127.replace("9:20p","21:20")
    texto129=texto128.replace("9:30p","21:30")
    texto130=texto129.replace("9:40p","21:40")
    texto131=texto130.replace("9:50p","21:50")
    texto132=texto131.replace("10:00p","22:00")
    texto133=texto132.replace("10:10p","22:10")
    texto134=texto133.replace("10:20p","22:20")
    texto135=texto134.replace("10:30p","22:30")
    texto136=texto135.replace("10:40p","22:40")
    texto137=texto136.replace("10:50p","22:50")
    texto138=texto137.replace("11:00p","23:00")
    texto139=texto138.replace("11:10p","23:10")
    texto140=texto139.replace("11:20p","23:20")
    texto141=texto140.replace("11:30p","23:30")
    texto142=texto141.replace("11:40p","23:40")
    texto143=texto142.replace("11:50p","23:50")
    texto144=texto143.replace("113:00","23:00")
    texto145=texto144.replace("113:10","23:10")
    texto146=texto145.replace("113:20","23:20")
    texto147=texto146.replace("113:30","23:30")
    texto148=texto147.replace("113:40","23:40")
    texto149=texto148.replace("113:50","23:50")
    enp31=open(dirtxtenp3,"w")
    enp31.write(texto149)
    enp31.close()
    enp3.close()

    enp3=open(dirtxtenp3)
    texto0=enp3.read()
    texto1=texto0.replace(",,",",")
    texto2=texto1.replace(",Date",",Fecha")
    enp31=open(dircsvenp3,"w")
    enp31.write(texto2)
    #print(texto2)
    enp31.close()
    enp3.close()

    enp3=pd.read_csv(dircsvenp3, usecols=(1,2,3,6,7,8,10,11,17,18,23), index_col=0, header=0)
    #print(enp3)
    enp3.to_csv(dircsvenp3)


    enp3=open(dircsvenp3)
    nombrescol=enp3.read()
    texto1=nombrescol.replace("Out","temperatura")
    texto2=texto1.replace("Hum","humedadRelativa")
    texto3=texto2.replace("Pt.","puntoRocio")
    texto4=texto3.replace("Speed.1","velocidadRacha")
    texto5=texto4.replace("Dir.1","direccionRacha")
    texto6=texto5.replace("Speed","velocidadViento")
    texto7=texto6.replace("Dir","direccionViento")
    texto8=texto7.replace("Bar","presionBar")
    texto9=texto8.replace("Rain","lluvia")
    texto10=texto9.replace("Index.3","UV")

    enp31=open(dircsvenp3,"w")
    enp31.write(texto10)
    enp31.close()
    enp3.close()

    enp3=open(dircsvenp3)
    texto=enp3.read()
    texto1=texto.replace("NNE","22.5")
    texto2=texto1.replace("ENE","67.5")
    texto3=texto2.replace("ESE","112.5")
    texto4=texto3.replace("SSE","157.5")
    texto5=texto4.replace("SSW","202.5")
    texto6=texto5.replace("WSW","247.5")
    texto7=texto6.replace("WNW","292.5")
    texto8=texto7.replace("NNW","337.5")
    texto9=texto8.replace("NE","45")
    texto10=texto9.replace("SE","135")
    texto11=texto10.replace("SW","225")
    texto12=texto11.replace("NW","315")
    enp31=open(dircsvenp3,"w")
    enp31.write(texto12)
    enp31.close()
    enp3.close()

    enp3=open(dircsvenp3)
    texto=enp3.read()
    texto1=texto.replace("N","360")
    texto2=texto1.replace("E","90")
    texto3=texto2.replace("S","180")
    texto4=texto3.replace("W","270")
    enp31=open(dircsvenp3,"w")
    enp31.write(texto4)
    enp31.close()
    enp3.close()

    enp3=pd.read_csv(dircsvenp3, index_col=0, header=0)
    #print(enp3)
    enp3['fechaHora']=enp3['Fecha'].map(str)  + ' ' + enp3['Time'].map(str)
    enp3
    #print(enp3)
    enp3.to_csv(dircsvenp3)


    DF=pd.read_csv(dircsvenp3, index_col=0)
    DF['idEstacion']=np.where(DF['Time'] !='[]', 'enp3', ' ', )
    #print(DF)
    DF.to_csv(dircsvenp3)

    enp3=pd.read_csv(dircsvenp3, usecols=(3,4,5,6,7,8,9,10,11,12,13), index_col=0, header=0)
    #print(enp3)
    enp3.to_csv(dircsvenp3)


    # try:
    #     enp3=pd.read_csv(dircsvenp3, index_col=0)
    #     filter= (enp3['fechaHora'] <= fecha_ayer1) & (enp3['fechaHora'] < fecha_hoy1)
    #     filtrado=enp3.loc[filter]
    #     #print(filtrado)
    #     filtrado.to_csv(dircsvenp3)
    #     print("Filtrado")
    # except:
    #     print("No se logro filtrar datos por fecha actual")


    print('Datos de la estación enp3 listos')
except:
    print("No se logro obtener datos de la estación enp3")
    remove(dircsvenp3)

print('enp4')
try:
    print(espacio)
    file1 = dirtxtenp4
    r = urllib.request.urlopen(urlenp4)
    f = open(file1,'wb')
    f.write(r.read())
    f.close()
    #print(file1)
    print('Datos de la estación enp4 obtenidos')

    try:
        with open(dirtxtenp4, 'r') as fr:
            # reading line by line
            lines = fr.readlines()

            # pointer for position
            ptr = 1

            # opening in writing mode
            with open(dirtxtenp4, 'w') as fw:
                for line in lines:

                    # we want to remove 5th line
                    if ptr != 1:
                        fw.write(line)
                    ptr += 1
        print("Deleted")

    except:
        print("Oops! No se pudo eliminar fila")

    try:
        with open(dirtxtenp4, 'r') as fr:
            # reading line by line
            lines = fr.readlines()

            # pointer for position
            ptr = 1

            # opening in writing mode
            with open(dirtxtenp4, 'w') as fw:
                for line in lines:

                    # we want to remove 5th line
                    if ptr != 2:
                        fw.write(line)
                    ptr += 1
        print("Deleted")

    except:
        print("Oops! No se pudo eliminar fila")


    enp4=open(dirtxtenp4)
    texto0=enp4.read()
    texto1=texto0.replace(" ",",")
    texto2=texto1.replace("---","9999")
    texto3=texto2.replace(",,",",")
    texto4=texto3.replace(",,,",",")
    texto5=texto4.replace(",,,,",",")
    texto6=texto5.replace(fecha_ayer0,fecha_ayerc)
    texto7=texto6.replace(fecha_hoy0,fecha_hoyc)
    #print(texto7)
    enp41=open(dirtxtenp4,"w")
    enp41.write(texto7)
    enp41.close()

    enp4=open(dirtxtenp4)
    texto=enp4.read()
    texto0=texto.replace("12:00a","00:00")
    texto1=texto0.replace("12:10a","00:10")
    texto2=texto1.replace("12:20a","00:20")
    texto3=texto2.replace("12:30a","00:30")
    texto4=texto3.replace("12:40a","00:40")
    texto5=texto4.replace("12:50a","00:50")
    texto6=texto5.replace("1:00a","1:00")
    texto7=texto6.replace("1:10a","1:10")
    texto8=texto7.replace("1:20a","1:20")
    texto9=texto8.replace("1:30a","1:30")
    texto10=texto9.replace("1:40a","1:40")
    texto11=texto10.replace("1:50a","1:50")
    texto12=texto11.replace("2:00a","2:00")
    texto13=texto12.replace("2:10a","2:10")
    texto14=texto13.replace("2:20a","2:20")
    texto15=texto14.replace("2:30a","2:30")
    texto16=texto15.replace("2:40a","2:40")
    texto17=texto16.replace("2:50a","2:50")
    texto18=texto17.replace("3:00a","3:00")
    texto19=texto18.replace("3:10a","3:10")
    texto20=texto19.replace("3:20a","3:20")
    texto21=texto20.replace("3:30a","3:30")
    texto22=texto21.replace("3:40a","3:40")
    texto23=texto22.replace("3:50a","3:50")
    texto24=texto23.replace("4:00a","4:00")
    texto25=texto24.replace("4:10a","4:10")
    texto26=texto25.replace("4:20a","4:20")
    texto27=texto26.replace("4:30a","4:30")
    texto28=texto27.replace("4:40a","4:40")
    texto29=texto28.replace("4:50a","4:50")
    texto30=texto29.replace("5:00a","5:00")
    texto31=texto30.replace("5:10a","5:10")
    texto32=texto31.replace("5:20a","5:20")
    texto33=texto32.replace("5:30a","5:30")
    texto34=texto33.replace("5:40a","5:40")
    texto35=texto34.replace("5:50a","5:50")
    texto36=texto35.replace("6:00a","6:00")
    texto37=texto36.replace("6:10a","6:10")
    texto38=texto37.replace("6:20a","6:20")
    texto39=texto38.replace("6:30a","6:30")
    texto40=texto39.replace("6:40a","6:40")
    texto41=texto40.replace("6:50a","6:50")
    texto42=texto41.replace("7:00a","7:00")
    texto43=texto42.replace("7:10a","7:10")
    texto44=texto43.replace("7:20a","7:20")
    texto45=texto44.replace("7:30a","7:30")
    texto46=texto45.replace("7:40a","7:40")
    texto47=texto46.replace("7:50a","7:50")
    texto48=texto47.replace("8:00a","8:00")
    texto49=texto48.replace("8:10a","8:10")
    texto50=texto49.replace("8:20a","8:20")
    texto51=texto50.replace("8:30a","8:30")
    texto52=texto51.replace("8:40a","8:40")
    texto53=texto52.replace("8:50a","8:50")
    texto54=texto53.replace("9:00a","9:00")
    texto55=texto54.replace("9:10a","9:10")
    texto56=texto55.replace("9:20a","9:20")
    texto57=texto56.replace("9:30a","9:30")
    texto58=texto57.replace("9:40a","9:40")
    texto59=texto58.replace("9:50a","9:50")
    texto60=texto59.replace("10:00a","10:00")
    texto61=texto60.replace("10:10a","10:10")
    texto62=texto61.replace("10:20a","10:20")
    texto63=texto62.replace("10:30a","10:30")
    texto64=texto63.replace("10:40a","10:40")
    texto65=texto64.replace("10:50a","10:50")
    texto66=texto65.replace("11:00a","11:00")
    texto67=texto66.replace("11:10a","11:10")
    texto68=texto67.replace("11:20a","11:20")
    texto69=texto68.replace("11:30a","11:30")
    texto70=texto69.replace("11:40a","11:40")
    texto71=texto70.replace("11:50a","11:50")
    texto72=texto71.replace("12:00p","12:00")
    texto73=texto72.replace("12:10p","12:10")
    texto74=texto73.replace("12:20p","12:20")
    texto75=texto74.replace("12:30p","12:30")
    texto76=texto75.replace("12:40p","12:40")
    texto77=texto76.replace("12:50p","12:50")
    texto78=texto77.replace("1:00p","13:00")
    texto79=texto78.replace("1:10p","13:10")
    texto80=texto79.replace("1:20p","13:20")
    texto81=texto80.replace("1:30p","13:30")
    texto82=texto81.replace("1:40p","13:40")
    texto83=texto82.replace("1:50p","13:50")
    texto84=texto83.replace("2:00p","14:00")
    texto85=texto84.replace("2:10p","14:10")
    texto86=texto85.replace("2:20p","14:20")
    texto87=texto86.replace("2:30p","14:30")
    texto88=texto87.replace("2:40p","14:40")
    texto89=texto88.replace("2:50p","14:50")
    texto90=texto89.replace("3:00p","15:00")
    texto91=texto90.replace("3:10p","15:10")
    texto92=texto91.replace("3:20p","15:20")
    texto93=texto92.replace("3:30p","15:30")
    texto94=texto93.replace("3:40p","15:40")
    texto95=texto94.replace("3:50p","15:50")
    texto96=texto95.replace("4:00p","16:00")
    texto97=texto96.replace("4:10p","16:10")
    texto98=texto97.replace("4:20p","16:20")
    texto99=texto98.replace("4:30p","16:30")
    texto100=texto99.replace("4:40p","16:40")
    texto11=texto100.replace("4:50p","16:50")
    texto12=texto11.replace("5:00p","17:00")
    texto13=texto12.replace("5:10p","17:10")
    texto14=texto13.replace("5:20p","17:20")
    texto15=texto14.replace("5:30p","17:30")
    texto16=texto15.replace("5:40p","17:40")
    texto17=texto16.replace("5:50p","17:50")
    texto18=texto17.replace("6:00p","18:00")
    texto19=texto18.replace("6:10p","18:10")
    texto110=texto19.replace("6:20p","18:20")
    texto111=texto110.replace("6:30p","18:30")
    texto112=texto111.replace("6:40p","18:40")
    texto113=texto112.replace("6:50p","18:50")
    texto114=texto113.replace("7:00p","19:00")
    texto115=texto114.replace("7:10p","19:10")
    texto116=texto115.replace("7:20p","19:20")
    texto117=texto116.replace("7:30p","19:30")
    texto118=texto117.replace("7:40p","19:40")
    texto119=texto118.replace("7:50p","19:50")
    texto120=texto119.replace("8:00p","20:00")
    texto121=texto120.replace("8:10p","20:10")
    texto122=texto121.replace("8:20p","20:20")
    texto123=texto122.replace("8:30p","20:30")
    texto124=texto123.replace("8:40p","20:40")
    texto125=texto124.replace("8:50p","20:50")
    texto126=texto125.replace("9:00p","21:00")
    texto127=texto126.replace("9:10p","21:10")
    texto128=texto127.replace("9:20p","21:20")
    texto129=texto128.replace("9:30p","21:30")
    texto130=texto129.replace("9:40p","21:40")
    texto131=texto130.replace("9:50p","21:50")
    texto132=texto131.replace("10:00p","22:00")
    texto133=texto132.replace("10:10p","22:10")
    texto134=texto133.replace("10:20p","22:20")
    texto135=texto134.replace("10:30p","22:30")
    texto136=texto135.replace("10:40p","22:40")
    texto137=texto136.replace("10:50p","22:50")
    texto138=texto137.replace("11:00p","23:00")
    texto139=texto138.replace("11:10p","23:10")
    texto140=texto139.replace("11:20p","23:20")
    texto141=texto140.replace("11:30p","23:30")
    texto142=texto141.replace("11:40p","23:40")
    texto143=texto142.replace("11:50p","23:50")
    texto144=texto143.replace("113:00","23:00")
    texto145=texto144.replace("113:10","23:10")
    texto146=texto145.replace("113:20","23:20")
    texto147=texto146.replace("113:30","23:30")
    texto148=texto147.replace("113:40","23:40")
    texto149=texto148.replace("113:50","23:50")
    enp41=open(dirtxtenp4,"w")
    enp41.write(texto149)
    enp41.close()
    enp4.close()

    enp4=open(dirtxtenp4)
    texto0=enp4.read()
    texto1=texto0.replace(",,",",")
    texto2=texto1.replace(",Date",",Fecha")
    enp41=open(dircsvenp4,"w")
    enp41.write(texto2)
    #print(texto2)
    enp41.close()
    enp4.close()

    enp4=pd.read_csv(dircsvenp4, usecols=(1,2,3,6,7,8,10,11,17,18,23), index_col=0, header=0)
    #print(enp4)
    enp4.to_csv(dircsvenp4)


    enp4=open(dircsvenp4)
    nombrescol=enp4.read()
    texto1=nombrescol.replace("Out","temperatura")
    texto2=texto1.replace("Hum","humedadRelativa")
    texto3=texto2.replace("Pt.","puntoRocio")
    texto4=texto3.replace("Speed.1","velocidadRacha")
    texto5=texto4.replace("Dir.1","direccionRacha")
    texto6=texto5.replace("Speed","velocidadViento")
    texto7=texto6.replace("Dir","direccionViento")
    texto8=texto7.replace("Bar","presionBar")
    texto9=texto8.replace("Rain","lluvia")
    texto10=texto9.replace("Index.3","UV")

    enp41=open(dircsvenp4,"w")
    enp41.write(texto10)
    enp41.close()
    enp4.close()

    enp4=open(dircsvenp4)
    texto=enp4.read()
    texto1=texto.replace("NNE","22.5")
    texto2=texto1.replace("ENE","67.5")
    texto3=texto2.replace("ESE","112.5")
    texto4=texto3.replace("SSE","157.5")
    texto5=texto4.replace("SSW","202.5")
    texto6=texto5.replace("WSW","247.5")
    texto7=texto6.replace("WNW","292.5")
    texto8=texto7.replace("NNW","337.5")
    texto9=texto8.replace("NE","45")
    texto10=texto9.replace("SE","135")
    texto11=texto10.replace("SW","225")
    texto12=texto11.replace("NW","315")
    enp41=open(dircsvenp4,"w")
    enp41.write(texto12)
    enp41.close()
    enp4.close()

    enp4=open(dircsvenp4)
    texto=enp4.read()
    texto1=texto.replace("N","360")
    texto2=texto1.replace("E","90")
    texto3=texto2.replace("S","180")
    texto4=texto3.replace("W","270")
    enp41=open(dircsvenp4,"w")
    enp41.write(texto4)
    enp41.close()
    enp4.close()

    enp4=pd.read_csv(dircsvenp4, index_col=0, header=0)
    #print(enp4)
    enp4['fechaHora']=enp4['Fecha'].map(str)  + ' ' + enp4['Time'].map(str)
    enp4
    #print(enp4)
    enp4.to_csv(dircsvenp4)


    DF=pd.read_csv(dircsvenp4, index_col=0)
    DF['idEstacion']=np.where(DF['Time'] !='[]', 'enp4', ' ', )
    #print(DF)
    DF.to_csv(dircsvenp4)

    enp4=pd.read_csv(dircsvenp4, usecols=(3,4,5,6,7,8,9,10,11,12,13), index_col=0, header=0)
    #print(enp4)
    enp4.to_csv(dircsvenp4)


    # try:
    #     enp4=pd.read_csv(dircsvenp4, index_col=0)
    #     filter= (enp4['fechaHora'] <= fecha_ayer1) & (enp4['fechaHora'] < fecha_hoy1)
    #     filtrado=enp4.loc[filter]
    #     #print(filtrado)
    #     filtrado.to_csv(dircsvenp4)
    #     print("Filtrado")
    # except:
    #     print("No se logro filtrar datos por fecha actual")


    print('Datos de la estación enp4 listos')
except:
    print("No se logro obtener datos de la estación enp4")
    remove(dircsvenp4)

print('enp5')
try:
    print(espacio)
    file1 = dirtxtenp5
    r = urllib.request.urlopen(urlenp5)
    f = open(file1,'wb')
    f.write(r.read())
    f.close()
    #print(file1)
    print('Datos de la estación enp5 obtenidos')

    try:
        with open(dirtxtenp5, 'r') as fr:
            # reading line by line
            lines = fr.readlines()

            # pointer for position
            ptr = 1

            # opening in writing mode
            with open(dirtxtenp5, 'w') as fw:
                for line in lines:

                    # we want to remove 5th line
                    if ptr != 1:
                        fw.write(line)
                    ptr += 1
        print("Deleted")

    except:
        print("Oops! No se pudo eliminar fila")

    try:
        with open(dirtxtenp5, 'r') as fr:
            # reading line by line
            lines = fr.readlines()

            # pointer for position
            ptr = 1

            # opening in writing mode
            with open(dirtxtenp5, 'w') as fw:
                for line in lines:

                    # we want to remove 5th line
                    if ptr != 2:
                        fw.write(line)
                    ptr += 1
        print("Deleted")

    except:
        print("Oops! No se pudo eliminar fila")


    enp5=open(dirtxtenp5)
    texto0=enp5.read()
    texto1=texto0.replace(" ",",")
    texto2=texto1.replace("---","9999")
    texto3=texto2.replace(",,",",")
    texto4=texto3.replace(",,,",",")
    texto5=texto4.replace(",,,,",",")
    texto6=texto5.replace(fecha_ayer0,fecha_ayerc)
    texto7=texto6.replace(fecha_hoy0,fecha_hoyc)
    #print(texto7)
    enp51=open(dirtxtenp5,"w")
    enp51.write(texto7)
    enp51.close()

    enp5=open(dirtxtenp5)
    texto=enp5.read()
    texto0=texto.replace("12:00a","00:00")
    texto1=texto0.replace("12:10a","00:10")
    texto2=texto1.replace("12:20a","00:20")
    texto3=texto2.replace("12:30a","00:30")
    texto4=texto3.replace("12:40a","00:40")
    texto5=texto4.replace("12:50a","00:50")
    texto6=texto5.replace("1:00a","1:00")
    texto7=texto6.replace("1:10a","1:10")
    texto8=texto7.replace("1:20a","1:20")
    texto9=texto8.replace("1:30a","1:30")
    texto10=texto9.replace("1:40a","1:40")
    texto11=texto10.replace("1:50a","1:50")
    texto12=texto11.replace("2:00a","2:00")
    texto13=texto12.replace("2:10a","2:10")
    texto14=texto13.replace("2:20a","2:20")
    texto15=texto14.replace("2:30a","2:30")
    texto16=texto15.replace("2:40a","2:40")
    texto17=texto16.replace("2:50a","2:50")
    texto18=texto17.replace("3:00a","3:00")
    texto19=texto18.replace("3:10a","3:10")
    texto20=texto19.replace("3:20a","3:20")
    texto21=texto20.replace("3:30a","3:30")
    texto22=texto21.replace("3:40a","3:40")
    texto23=texto22.replace("3:50a","3:50")
    texto24=texto23.replace("4:00a","4:00")
    texto25=texto24.replace("4:10a","4:10")
    texto26=texto25.replace("4:20a","4:20")
    texto27=texto26.replace("4:30a","4:30")
    texto28=texto27.replace("4:40a","4:40")
    texto29=texto28.replace("4:50a","4:50")
    texto30=texto29.replace("5:00a","5:00")
    texto31=texto30.replace("5:10a","5:10")
    texto32=texto31.replace("5:20a","5:20")
    texto33=texto32.replace("5:30a","5:30")
    texto34=texto33.replace("5:40a","5:40")
    texto35=texto34.replace("5:50a","5:50")
    texto36=texto35.replace("6:00a","6:00")
    texto37=texto36.replace("6:10a","6:10")
    texto38=texto37.replace("6:20a","6:20")
    texto39=texto38.replace("6:30a","6:30")
    texto40=texto39.replace("6:40a","6:40")
    texto41=texto40.replace("6:50a","6:50")
    texto42=texto41.replace("7:00a","7:00")
    texto43=texto42.replace("7:10a","7:10")
    texto44=texto43.replace("7:20a","7:20")
    texto45=texto44.replace("7:30a","7:30")
    texto46=texto45.replace("7:40a","7:40")
    texto47=texto46.replace("7:50a","7:50")
    texto48=texto47.replace("8:00a","8:00")
    texto49=texto48.replace("8:10a","8:10")
    texto50=texto49.replace("8:20a","8:20")
    texto51=texto50.replace("8:30a","8:30")
    texto52=texto51.replace("8:40a","8:40")
    texto53=texto52.replace("8:50a","8:50")
    texto54=texto53.replace("9:00a","9:00")
    texto55=texto54.replace("9:10a","9:10")
    texto56=texto55.replace("9:20a","9:20")
    texto57=texto56.replace("9:30a","9:30")
    texto58=texto57.replace("9:40a","9:40")
    texto59=texto58.replace("9:50a","9:50")
    texto60=texto59.replace("10:00a","10:00")
    texto61=texto60.replace("10:10a","10:10")
    texto62=texto61.replace("10:20a","10:20")
    texto63=texto62.replace("10:30a","10:30")
    texto64=texto63.replace("10:40a","10:40")
    texto65=texto64.replace("10:50a","10:50")
    texto66=texto65.replace("11:00a","11:00")
    texto67=texto66.replace("11:10a","11:10")
    texto68=texto67.replace("11:20a","11:20")
    texto69=texto68.replace("11:30a","11:30")
    texto70=texto69.replace("11:40a","11:40")
    texto71=texto70.replace("11:50a","11:50")
    texto72=texto71.replace("12:00p","12:00")
    texto73=texto72.replace("12:10p","12:10")
    texto74=texto73.replace("12:20p","12:20")
    texto75=texto74.replace("12:30p","12:30")
    texto76=texto75.replace("12:40p","12:40")
    texto77=texto76.replace("12:50p","12:50")
    texto78=texto77.replace("1:00p","13:00")
    texto79=texto78.replace("1:10p","13:10")
    texto80=texto79.replace("1:20p","13:20")
    texto81=texto80.replace("1:30p","13:30")
    texto82=texto81.replace("1:40p","13:40")
    texto83=texto82.replace("1:50p","13:50")
    texto84=texto83.replace("2:00p","14:00")
    texto85=texto84.replace("2:10p","14:10")
    texto86=texto85.replace("2:20p","14:20")
    texto87=texto86.replace("2:30p","14:30")
    texto88=texto87.replace("2:40p","14:40")
    texto89=texto88.replace("2:50p","14:50")
    texto90=texto89.replace("3:00p","15:00")
    texto91=texto90.replace("3:10p","15:10")
    texto92=texto91.replace("3:20p","15:20")
    texto93=texto92.replace("3:30p","15:30")
    texto94=texto93.replace("3:40p","15:40")
    texto95=texto94.replace("3:50p","15:50")
    texto96=texto95.replace("4:00p","16:00")
    texto97=texto96.replace("4:10p","16:10")
    texto98=texto97.replace("4:20p","16:20")
    texto99=texto98.replace("4:30p","16:30")
    texto100=texto99.replace("4:40p","16:40")
    texto11=texto100.replace("4:50p","16:50")
    texto12=texto11.replace("5:00p","17:00")
    texto13=texto12.replace("5:10p","17:10")
    texto14=texto13.replace("5:20p","17:20")
    texto15=texto14.replace("5:30p","17:30")
    texto16=texto15.replace("5:40p","17:40")
    texto17=texto16.replace("5:50p","17:50")
    texto18=texto17.replace("6:00p","18:00")
    texto19=texto18.replace("6:10p","18:10")
    texto110=texto19.replace("6:20p","18:20")
    texto111=texto110.replace("6:30p","18:30")
    texto112=texto111.replace("6:40p","18:40")
    texto113=texto112.replace("6:50p","18:50")
    texto114=texto113.replace("7:00p","19:00")
    texto115=texto114.replace("7:10p","19:10")
    texto116=texto115.replace("7:20p","19:20")
    texto117=texto116.replace("7:30p","19:30")
    texto118=texto117.replace("7:40p","19:40")
    texto119=texto118.replace("7:50p","19:50")
    texto120=texto119.replace("8:00p","20:00")
    texto121=texto120.replace("8:10p","20:10")
    texto122=texto121.replace("8:20p","20:20")
    texto123=texto122.replace("8:30p","20:30")
    texto124=texto123.replace("8:40p","20:40")
    texto125=texto124.replace("8:50p","20:50")
    texto126=texto125.replace("9:00p","21:00")
    texto127=texto126.replace("9:10p","21:10")
    texto128=texto127.replace("9:20p","21:20")
    texto129=texto128.replace("9:30p","21:30")
    texto130=texto129.replace("9:40p","21:40")
    texto131=texto130.replace("9:50p","21:50")
    texto132=texto131.replace("10:00p","22:00")
    texto133=texto132.replace("10:10p","22:10")
    texto134=texto133.replace("10:20p","22:20")
    texto135=texto134.replace("10:30p","22:30")
    texto136=texto135.replace("10:40p","22:40")
    texto137=texto136.replace("10:50p","22:50")
    texto138=texto137.replace("11:00p","23:00")
    texto139=texto138.replace("11:10p","23:10")
    texto140=texto139.replace("11:20p","23:20")
    texto141=texto140.replace("11:30p","23:30")
    texto142=texto141.replace("11:40p","23:40")
    texto143=texto142.replace("11:50p","23:50")
    texto144=texto143.replace("113:00","23:00")
    texto145=texto144.replace("113:10","23:10")
    texto146=texto145.replace("113:20","23:20")
    texto147=texto146.replace("113:30","23:30")
    texto148=texto147.replace("113:40","23:40")
    texto149=texto148.replace("113:50","23:50")
    enp51=open(dirtxtenp5,"w")
    enp51.write(texto149)
    enp51.close()
    enp5.close()

    enp5=open(dirtxtenp5)
    texto0=enp5.read()
    texto1=texto0.replace(",,",",")
    texto2=texto1.replace(",Date",",Fecha")
    enp51=open(dircsvenp5,"w")
    enp51.write(texto2)
    #print(texto2)
    enp51.close()
    enp5.close()

    enp5=pd.read_csv(dircsvenp5, usecols=(1,2,3,6,7,8,10,11,17,18,23), index_col=0, header=0)
    #print(enp5)
    enp5.to_csv(dircsvenp5)


    enp5=open(dircsvenp5)
    nombrescol=enp5.read()
    texto1=nombrescol.replace("Out","temperatura")
    texto2=texto1.replace("Hum","humedadRelativa")
    texto3=texto2.replace("Pt.","puntoRocio")
    texto4=texto3.replace("Speed.1","velocidadRacha")
    texto5=texto4.replace("Dir.1","direccionRacha")
    texto6=texto5.replace("Speed","velocidadViento")
    texto7=texto6.replace("Dir","direccionViento")
    texto8=texto7.replace("Bar","presionBar")
    texto9=texto8.replace("Rain","lluvia")
    texto10=texto9.replace("Index.3","UV")

    enp51=open(dircsvenp5,"w")
    enp51.write(texto10)
    enp51.close()
    enp5.close()

    enp5=open(dircsvenp5)
    texto=enp5.read()
    texto1=texto.replace("NNE","22.5")
    texto2=texto1.replace("ENE","67.5")
    texto3=texto2.replace("ESE","112.5")
    texto4=texto3.replace("SSE","157.5")
    texto5=texto4.replace("SSW","202.5")
    texto6=texto5.replace("WSW","247.5")
    texto7=texto6.replace("WNW","292.5")
    texto8=texto7.replace("NNW","337.5")
    texto9=texto8.replace("NE","45")
    texto10=texto9.replace("SE","135")
    texto11=texto10.replace("SW","225")
    texto12=texto11.replace("NW","315")
    enp51=open(dircsvenp5,"w")
    enp51.write(texto12)
    enp51.close()
    enp5.close()

    enp5=open(dircsvenp5)
    texto=enp5.read()
    texto1=texto.replace("N","360")
    texto2=texto1.replace("E","90")
    texto3=texto2.replace("S","180")
    texto4=texto3.replace("W","270")
    enp51=open(dircsvenp5,"w")
    enp51.write(texto4)
    enp51.close()
    enp5.close()

    enp5=pd.read_csv(dircsvenp5, index_col=0, header=0)
    #print(enp5)
    enp5['fechaHora']=enp5['Fecha'].map(str)  + ' ' + enp5['Time'].map(str)
    enp5
    #print(enp5)
    enp5.to_csv(dircsvenp5)


    DF=pd.read_csv(dircsvenp5, index_col=0)
    DF['idEstacion']=np.where(DF['Time'] !='[]', 'enp5', ' ', )
    #print(DF)
    DF.to_csv(dircsvenp5)

    enp5=pd.read_csv(dircsvenp5, usecols=(3,4,5,6,7,8,9,10,11,12,13), index_col=0, header=0)
    #print(enp5)
    enp5.to_csv(dircsvenp5)


    # try:
    #     enp5=pd.read_csv(dircsvenp5, index_col=0)
    #     filter= (enp5['fechaHora'] <= fecha_ayer1) & (enp5['fechaHora'] < fecha_hoy1)
    #     filtrado=enp5.loc[filter]
    #     #print(filtrado)
    #     filtrado.to_csv(dircsvenp5)
    #     print("Filtrado")
    # except:
    #     print("No se logro filtrar datos por fecha actual")


    print('Datos de la estación enp5 listos')
except:
    print("No se logro obtener datos de la estación enp5")
    remove(dircsvenp5)
print('enp6')

try:
    print(espacio)
    file1 = dirtxtenp6
    r = urllib.request.urlopen(urlenp6)
    f = open(file1,'wb')
    f.write(r.read())
    f.close()
    #print(file1)
    print('Datos de la estación enp6 obtenidos')

    try:
        with open(dirtxtenp6, 'r') as fr:
            # reading line by line
            lines = fr.readlines()

            # pointer for position
            ptr = 1

            # opening in writing mode
            with open(dirtxtenp6, 'w') as fw:
                for line in lines:

                    # we want to remove 5th line
                    if ptr != 1:
                        fw.write(line)
                    ptr += 1
        print("Deleted")

    except:
        print("Oops! No se pudo eliminar fila")

    try:
        with open(dirtxtenp6, 'r') as fr:
            # reading line by line
            lines = fr.readlines()

            # pointer for position
            ptr = 1

            # opening in writing mode
            with open(dirtxtenp6, 'w') as fw:
                for line in lines:

                    # we want to remove 5th line
                    if ptr != 2:
                        fw.write(line)
                    ptr += 1
        print("Deleted")

    except:
        print("Oops! No se pudo eliminar fila")


    enp6=open(dirtxtenp6)
    texto0=enp6.read()
    texto1=texto0.replace(" ",",")
    texto2=texto1.replace("---","9999")
    texto3=texto2.replace(",,",",")
    texto4=texto3.replace(",,,",",")
    texto5=texto4.replace(",,,,",",")
    texto6=texto5.replace(fecha_ayer0,fecha_ayerc)
    texto7=texto6.replace(fecha_hoy0,fecha_hoyc)
    #print(texto7)
    enp61=open(dirtxtenp6,"w")
    enp61.write(texto7)
    enp61.close()

    enp6=open(dirtxtenp6)
    texto=enp6.read()
    texto0=texto.replace("12:00a","00:00")
    texto1=texto0.replace("12:10a","00:10")
    texto2=texto1.replace("12:20a","00:20")
    texto3=texto2.replace("12:30a","00:30")
    texto4=texto3.replace("12:40a","00:40")
    texto5=texto4.replace("12:50a","00:50")
    texto6=texto5.replace("1:00a","1:00")
    texto7=texto6.replace("1:10a","1:10")
    texto8=texto7.replace("1:20a","1:20")
    texto9=texto8.replace("1:30a","1:30")
    texto10=texto9.replace("1:40a","1:40")
    texto11=texto10.replace("1:50a","1:50")
    texto12=texto11.replace("2:00a","2:00")
    texto13=texto12.replace("2:10a","2:10")
    texto14=texto13.replace("2:20a","2:20")
    texto15=texto14.replace("2:30a","2:30")
    texto16=texto15.replace("2:40a","2:40")
    texto17=texto16.replace("2:50a","2:50")
    texto18=texto17.replace("3:00a","3:00")
    texto19=texto18.replace("3:10a","3:10")
    texto20=texto19.replace("3:20a","3:20")
    texto21=texto20.replace("3:30a","3:30")
    texto22=texto21.replace("3:40a","3:40")
    texto23=texto22.replace("3:50a","3:50")
    texto24=texto23.replace("4:00a","4:00")
    texto25=texto24.replace("4:10a","4:10")
    texto26=texto25.replace("4:20a","4:20")
    texto27=texto26.replace("4:30a","4:30")
    texto28=texto27.replace("4:40a","4:40")
    texto29=texto28.replace("4:50a","4:50")
    texto30=texto29.replace("5:00a","5:00")
    texto31=texto30.replace("5:10a","5:10")
    texto32=texto31.replace("5:20a","5:20")
    texto33=texto32.replace("5:30a","5:30")
    texto34=texto33.replace("5:40a","5:40")
    texto35=texto34.replace("5:50a","5:50")
    texto36=texto35.replace("6:00a","6:00")
    texto37=texto36.replace("6:10a","6:10")
    texto38=texto37.replace("6:20a","6:20")
    texto39=texto38.replace("6:30a","6:30")
    texto40=texto39.replace("6:40a","6:40")
    texto41=texto40.replace("6:50a","6:50")
    texto42=texto41.replace("7:00a","7:00")
    texto43=texto42.replace("7:10a","7:10")
    texto44=texto43.replace("7:20a","7:20")
    texto45=texto44.replace("7:30a","7:30")
    texto46=texto45.replace("7:40a","7:40")
    texto47=texto46.replace("7:50a","7:50")
    texto48=texto47.replace("8:00a","8:00")
    texto49=texto48.replace("8:10a","8:10")
    texto50=texto49.replace("8:20a","8:20")
    texto51=texto50.replace("8:30a","8:30")
    texto52=texto51.replace("8:40a","8:40")
    texto53=texto52.replace("8:50a","8:50")
    texto54=texto53.replace("9:00a","9:00")
    texto55=texto54.replace("9:10a","9:10")
    texto56=texto55.replace("9:20a","9:20")
    texto57=texto56.replace("9:30a","9:30")
    texto58=texto57.replace("9:40a","9:40")
    texto59=texto58.replace("9:50a","9:50")
    texto60=texto59.replace("10:00a","10:00")
    texto61=texto60.replace("10:10a","10:10")
    texto62=texto61.replace("10:20a","10:20")
    texto63=texto62.replace("10:30a","10:30")
    texto64=texto63.replace("10:40a","10:40")
    texto65=texto64.replace("10:50a","10:50")
    texto66=texto65.replace("11:00a","11:00")
    texto67=texto66.replace("11:10a","11:10")
    texto68=texto67.replace("11:20a","11:20")
    texto69=texto68.replace("11:30a","11:30")
    texto70=texto69.replace("11:40a","11:40")
    texto71=texto70.replace("11:50a","11:50")
    texto72=texto71.replace("12:00p","12:00")
    texto73=texto72.replace("12:10p","12:10")
    texto74=texto73.replace("12:20p","12:20")
    texto75=texto74.replace("12:30p","12:30")
    texto76=texto75.replace("12:40p","12:40")
    texto77=texto76.replace("12:50p","12:50")
    texto78=texto77.replace("1:00p","13:00")
    texto79=texto78.replace("1:10p","13:10")
    texto80=texto79.replace("1:20p","13:20")
    texto81=texto80.replace("1:30p","13:30")
    texto82=texto81.replace("1:40p","13:40")
    texto83=texto82.replace("1:50p","13:50")
    texto84=texto83.replace("2:00p","14:00")
    texto85=texto84.replace("2:10p","14:10")
    texto86=texto85.replace("2:20p","14:20")
    texto87=texto86.replace("2:30p","14:30")
    texto88=texto87.replace("2:40p","14:40")
    texto89=texto88.replace("2:50p","14:50")
    texto90=texto89.replace("3:00p","15:00")
    texto91=texto90.replace("3:10p","15:10")
    texto92=texto91.replace("3:20p","15:20")
    texto93=texto92.replace("3:30p","15:30")
    texto94=texto93.replace("3:40p","15:40")
    texto95=texto94.replace("3:50p","15:50")
    texto96=texto95.replace("4:00p","16:00")
    texto97=texto96.replace("4:10p","16:10")
    texto98=texto97.replace("4:20p","16:20")
    texto99=texto98.replace("4:30p","16:30")
    texto100=texto99.replace("4:40p","16:40")
    texto11=texto100.replace("4:50p","16:50")
    texto12=texto11.replace("5:00p","17:00")
    texto13=texto12.replace("5:10p","17:10")
    texto14=texto13.replace("5:20p","17:20")
    texto15=texto14.replace("5:30p","17:30")
    texto16=texto15.replace("5:40p","17:40")
    texto17=texto16.replace("5:50p","17:50")
    texto18=texto17.replace("6:00p","18:00")
    texto19=texto18.replace("6:10p","18:10")
    texto110=texto19.replace("6:20p","18:20")
    texto111=texto110.replace("6:30p","18:30")
    texto112=texto111.replace("6:40p","18:40")
    texto113=texto112.replace("6:50p","18:50")
    texto114=texto113.replace("7:00p","19:00")
    texto115=texto114.replace("7:10p","19:10")
    texto116=texto115.replace("7:20p","19:20")
    texto117=texto116.replace("7:30p","19:30")
    texto118=texto117.replace("7:40p","19:40")
    texto119=texto118.replace("7:50p","19:50")
    texto120=texto119.replace("8:00p","20:00")
    texto121=texto120.replace("8:10p","20:10")
    texto122=texto121.replace("8:20p","20:20")
    texto123=texto122.replace("8:30p","20:30")
    texto124=texto123.replace("8:40p","20:40")
    texto125=texto124.replace("8:50p","20:50")
    texto126=texto125.replace("9:00p","21:00")
    texto127=texto126.replace("9:10p","21:10")
    texto128=texto127.replace("9:20p","21:20")
    texto129=texto128.replace("9:30p","21:30")
    texto130=texto129.replace("9:40p","21:40")
    texto131=texto130.replace("9:50p","21:50")
    texto132=texto131.replace("10:00p","22:00")
    texto133=texto132.replace("10:10p","22:10")
    texto134=texto133.replace("10:20p","22:20")
    texto135=texto134.replace("10:30p","22:30")
    texto136=texto135.replace("10:40p","22:40")
    texto137=texto136.replace("10:50p","22:50")
    texto138=texto137.replace("11:00p","23:00")
    texto139=texto138.replace("11:10p","23:10")
    texto140=texto139.replace("11:20p","23:20")
    texto141=texto140.replace("11:30p","23:30")
    texto142=texto141.replace("11:40p","23:40")
    texto143=texto142.replace("11:50p","23:50")
    texto144=texto143.replace("113:00","23:00")
    texto145=texto144.replace("113:10","23:10")
    texto146=texto145.replace("113:20","23:20")
    texto147=texto146.replace("113:30","23:30")
    texto148=texto147.replace("113:40","23:40")
    texto149=texto148.replace("113:50","23:50")
    enp61=open(dirtxtenp6,"w")
    enp61.write(texto149)
    enp61.close()
    enp6.close()

    enp6=open(dirtxtenp6)
    texto0=enp6.read()
    texto1=texto0.replace(",,",",")
    texto2=texto1.replace(",Date",",Fecha")
    enp61=open(dircsvenp6,"w")
    enp61.write(texto2)
    #print(texto2)
    enp61.close()
    enp6.close()

    enp6=pd.read_csv(dircsvenp6, usecols=(1,2,3,6,7,8,10,11,17,18,23), index_col=0, header=0)
    #print(enp6)
    enp6.to_csv(dircsvenp6)


    enp6=open(dircsvenp6)
    nombrescol=enp6.read()
    texto1=nombrescol.replace("Out","temperatura")
    texto2=texto1.replace("Hum","humedadRelativa")
    texto3=texto2.replace("Pt.","puntoRocio")
    texto4=texto3.replace("Speed.1","velocidadRacha")
    texto5=texto4.replace("Dir.1","direccionRacha")
    texto6=texto5.replace("Speed","velocidadViento")
    texto7=texto6.replace("Dir","direccionViento")
    texto8=texto7.replace("Bar","presionBar")
    texto9=texto8.replace("Rain","lluvia")
    texto10=texto9.replace("Index.3","UV")

    enp61=open(dircsvenp6,"w")
    enp61.write(texto10)
    enp61.close()
    enp6.close()

    enp6=open(dircsvenp6)
    texto=enp6.read()
    texto1=texto.replace("NNE","22.5")
    texto2=texto1.replace("ENE","67.5")
    texto3=texto2.replace("ESE","112.5")
    texto4=texto3.replace("SSE","157.5")
    texto5=texto4.replace("SSW","202.5")
    texto6=texto5.replace("WSW","247.5")
    texto7=texto6.replace("WNW","292.5")
    texto8=texto7.replace("NNW","337.5")
    texto9=texto8.replace("NE","45")
    texto10=texto9.replace("SE","135")
    texto11=texto10.replace("SW","225")
    texto12=texto11.replace("NW","315")
    enp61=open(dircsvenp6,"w")
    enp61.write(texto12)
    enp61.close()
    enp6.close()

    enp6=open(dircsvenp6)
    texto=enp6.read()
    texto1=texto.replace("N","360")
    texto2=texto1.replace("E","90")
    texto3=texto2.replace("S","180")
    texto4=texto3.replace("W","270")
    enp61=open(dircsvenp6,"w")
    enp61.write(texto4)
    enp61.close()
    enp6.close()

    enp6=pd.read_csv(dircsvenp6, index_col=0, header=0)
    #print(enp6)
    enp6['fechaHora']=enp6['Fecha'].map(str)  + ' ' + enp6['Time'].map(str)
    enp6
    #print(enp6)
    enp6.to_csv(dircsvenp6)


    DF=pd.read_csv(dircsvenp6, index_col=0)
    DF['idEstacion']=np.where(DF['Time'] !='[]', 'enp6', ' ', )
    #print(DF)
    DF.to_csv(dircsvenp6)

    enp6=pd.read_csv(dircsvenp6, usecols=(3,4,5,6,7,8,9,10,11,12,13), index_col=0, header=0)
    #print(enp6)
    enp6.to_csv(dircsvenp6)


    # try:
    #     enp6=pd.read_csv(dircsvenp6, index_col=0)
    #     filter= (enp6['fechaHora'] <= fecha_ayer1) & (enp6['fechaHora'] < fecha_hoy1)
    #     filtrado=enp6.loc[filter]
    #     #print(filtrado)
    #     filtrado.to_csv(dircsvenp6)
    #     print("Filtrado")
    # except:
    #     print("No se logro filtrar datos por fecha actual")


    print('Datos de la estación enp6 listos')
except:
    print("No se logro obtener datos de la estación enp6")
    remove(dircsvenp6)


print('enp7')
try:
    print(espacio)
    file1 = dirtxtenp7
    r = urllib.request.urlopen(urlenp7)
    f = open(file1,'wb')
    f.write(r.read())
    f.close()
    #print(file1)
    print('Datos de la estación enp7 obtenidos')

    try:
        with open(dirtxtenp7, 'r') as fr:
            # reading line by line
            lines = fr.readlines()

            # pointer for position
            ptr = 1

            # opening in writing mode
            with open(dirtxtenp7, 'w') as fw:
                for line in lines:

                    # we want to remove 5th line
                    if ptr != 1:
                        fw.write(line)
                    ptr += 1
        print("Deleted")

    except:
        print("Oops! No se pudo eliminar fila")

    try:
        with open(dirtxtenp7, 'r') as fr:
            # reading line by line
            lines = fr.readlines()

            # pointer for position
            ptr = 1

            # opening in writing mode
            with open(dirtxtenp7, 'w') as fw:
                for line in lines:

                    # we want to remove 5th line
                    if ptr != 2:
                        fw.write(line)
                    ptr += 1
        print("Deleted")

    except:
        print("Oops! No se pudo eliminar fila")


    enp7=open(dirtxtenp7)
    texto0=enp7.read()
    texto1=texto0.replace(" ",",")
    texto2=texto1.replace("---","9999")
    texto3=texto2.replace(",,",",")
    texto4=texto3.replace(",,,",",")
    texto5=texto4.replace(",,,,",",")
    texto6=texto5.replace(fecha_ayer0,fecha_ayerc)
    texto7=texto6.replace(fecha_hoy0,fecha_hoyc)
    #print(texto7)
    enp71=open(dirtxtenp7,"w")
    enp71.write(texto7)
    enp71.close()

    enp7=open(dirtxtenp7)
    texto=enp7.read()
    texto0=texto.replace("12:00a","00:00")
    texto1=texto0.replace("12:10a","00:10")
    texto2=texto1.replace("12:20a","00:20")
    texto3=texto2.replace("12:30a","00:30")
    texto4=texto3.replace("12:40a","00:40")
    texto5=texto4.replace("12:50a","00:50")
    texto6=texto5.replace("1:00a","1:00")
    texto7=texto6.replace("1:10a","1:10")
    texto8=texto7.replace("1:20a","1:20")
    texto9=texto8.replace("1:30a","1:30")
    texto10=texto9.replace("1:40a","1:40")
    texto11=texto10.replace("1:50a","1:50")
    texto12=texto11.replace("2:00a","2:00")
    texto13=texto12.replace("2:10a","2:10")
    texto14=texto13.replace("2:20a","2:20")
    texto15=texto14.replace("2:30a","2:30")
    texto16=texto15.replace("2:40a","2:40")
    texto17=texto16.replace("2:50a","2:50")
    texto18=texto17.replace("3:00a","3:00")
    texto19=texto18.replace("3:10a","3:10")
    texto20=texto19.replace("3:20a","3:20")
    texto21=texto20.replace("3:30a","3:30")
    texto22=texto21.replace("3:40a","3:40")
    texto23=texto22.replace("3:50a","3:50")
    texto24=texto23.replace("4:00a","4:00")
    texto25=texto24.replace("4:10a","4:10")
    texto26=texto25.replace("4:20a","4:20")
    texto27=texto26.replace("4:30a","4:30")
    texto28=texto27.replace("4:40a","4:40")
    texto29=texto28.replace("4:50a","4:50")
    texto30=texto29.replace("5:00a","5:00")
    texto31=texto30.replace("5:10a","5:10")
    texto32=texto31.replace("5:20a","5:20")
    texto33=texto32.replace("5:30a","5:30")
    texto34=texto33.replace("5:40a","5:40")
    texto35=texto34.replace("5:50a","5:50")
    texto36=texto35.replace("6:00a","6:00")
    texto37=texto36.replace("6:10a","6:10")
    texto38=texto37.replace("6:20a","6:20")
    texto39=texto38.replace("6:30a","6:30")
    texto40=texto39.replace("6:40a","6:40")
    texto41=texto40.replace("6:50a","6:50")
    texto42=texto41.replace("7:00a","7:00")
    texto43=texto42.replace("7:10a","7:10")
    texto44=texto43.replace("7:20a","7:20")
    texto45=texto44.replace("7:30a","7:30")
    texto46=texto45.replace("7:40a","7:40")
    texto47=texto46.replace("7:50a","7:50")
    texto48=texto47.replace("8:00a","8:00")
    texto49=texto48.replace("8:10a","8:10")
    texto50=texto49.replace("8:20a","8:20")
    texto51=texto50.replace("8:30a","8:30")
    texto52=texto51.replace("8:40a","8:40")
    texto53=texto52.replace("8:50a","8:50")
    texto54=texto53.replace("9:00a","9:00")
    texto55=texto54.replace("9:10a","9:10")
    texto56=texto55.replace("9:20a","9:20")
    texto57=texto56.replace("9:30a","9:30")
    texto58=texto57.replace("9:40a","9:40")
    texto59=texto58.replace("9:50a","9:50")
    texto60=texto59.replace("10:00a","10:00")
    texto61=texto60.replace("10:10a","10:10")
    texto62=texto61.replace("10:20a","10:20")
    texto63=texto62.replace("10:30a","10:30")
    texto64=texto63.replace("10:40a","10:40")
    texto65=texto64.replace("10:50a","10:50")
    texto66=texto65.replace("11:00a","11:00")
    texto67=texto66.replace("11:10a","11:10")
    texto68=texto67.replace("11:20a","11:20")
    texto69=texto68.replace("11:30a","11:30")
    texto70=texto69.replace("11:40a","11:40")
    texto71=texto70.replace("11:50a","11:50")
    texto72=texto71.replace("12:00p","12:00")
    texto73=texto72.replace("12:10p","12:10")
    texto74=texto73.replace("12:20p","12:20")
    texto75=texto74.replace("12:30p","12:30")
    texto76=texto75.replace("12:40p","12:40")
    texto77=texto76.replace("12:50p","12:50")
    texto78=texto77.replace("1:00p","13:00")
    texto79=texto78.replace("1:10p","13:10")
    texto80=texto79.replace("1:20p","13:20")
    texto81=texto80.replace("1:30p","13:30")
    texto82=texto81.replace("1:40p","13:40")
    texto83=texto82.replace("1:50p","13:50")
    texto84=texto83.replace("2:00p","14:00")
    texto85=texto84.replace("2:10p","14:10")
    texto86=texto85.replace("2:20p","14:20")
    texto87=texto86.replace("2:30p","14:30")
    texto88=texto87.replace("2:40p","14:40")
    texto89=texto88.replace("2:50p","14:50")
    texto90=texto89.replace("3:00p","15:00")
    texto91=texto90.replace("3:10p","15:10")
    texto92=texto91.replace("3:20p","15:20")
    texto93=texto92.replace("3:30p","15:30")
    texto94=texto93.replace("3:40p","15:40")
    texto95=texto94.replace("3:50p","15:50")
    texto96=texto95.replace("4:00p","16:00")
    texto97=texto96.replace("4:10p","16:10")
    texto98=texto97.replace("4:20p","16:20")
    texto99=texto98.replace("4:30p","16:30")
    texto100=texto99.replace("4:40p","16:40")
    texto11=texto100.replace("4:50p","16:50")
    texto12=texto11.replace("5:00p","17:00")
    texto13=texto12.replace("5:10p","17:10")
    texto14=texto13.replace("5:20p","17:20")
    texto15=texto14.replace("5:30p","17:30")
    texto16=texto15.replace("5:40p","17:40")
    texto17=texto16.replace("5:50p","17:50")
    texto18=texto17.replace("6:00p","18:00")
    texto19=texto18.replace("6:10p","18:10")
    texto110=texto19.replace("6:20p","18:20")
    texto111=texto110.replace("6:30p","18:30")
    texto112=texto111.replace("6:40p","18:40")
    texto113=texto112.replace("6:50p","18:50")
    texto114=texto113.replace("7:00p","19:00")
    texto115=texto114.replace("7:10p","19:10")
    texto116=texto115.replace("7:20p","19:20")
    texto117=texto116.replace("7:30p","19:30")
    texto118=texto117.replace("7:40p","19:40")
    texto119=texto118.replace("7:50p","19:50")
    texto120=texto119.replace("8:00p","20:00")
    texto121=texto120.replace("8:10p","20:10")
    texto122=texto121.replace("8:20p","20:20")
    texto123=texto122.replace("8:30p","20:30")
    texto124=texto123.replace("8:40p","20:40")
    texto125=texto124.replace("8:50p","20:50")
    texto126=texto125.replace("9:00p","21:00")
    texto127=texto126.replace("9:10p","21:10")
    texto128=texto127.replace("9:20p","21:20")
    texto129=texto128.replace("9:30p","21:30")
    texto130=texto129.replace("9:40p","21:40")
    texto131=texto130.replace("9:50p","21:50")
    texto132=texto131.replace("10:00p","22:00")
    texto133=texto132.replace("10:10p","22:10")
    texto134=texto133.replace("10:20p","22:20")
    texto135=texto134.replace("10:30p","22:30")
    texto136=texto135.replace("10:40p","22:40")
    texto137=texto136.replace("10:50p","22:50")
    texto138=texto137.replace("11:00p","23:00")
    texto139=texto138.replace("11:10p","23:10")
    texto140=texto139.replace("11:20p","23:20")
    texto141=texto140.replace("11:30p","23:30")
    texto142=texto141.replace("11:40p","23:40")
    texto143=texto142.replace("11:50p","23:50")
    texto144=texto143.replace("113:00","23:00")
    texto145=texto144.replace("113:10","23:10")
    texto146=texto145.replace("113:20","23:20")
    texto147=texto146.replace("113:30","23:30")
    texto148=texto147.replace("113:40","23:40")
    texto149=texto148.replace("113:50","23:50")
    enp71=open(dirtxtenp7,"w")
    enp71.write(texto149)
    enp71.close()
    enp7.close()

    enp7=open(dirtxtenp7)
    texto0=enp7.read()
    texto1=texto0.replace(",,",",")
    texto2=texto1.replace(",Date",",Fecha")
    enp71=open(dircsvenp7,"w")
    enp71.write(texto2)
    #print(texto2)
    enp71.close()
    enp7.close()

    enp7=pd.read_csv(dircsvenp7, usecols=(1,2,3,6,7,8,10,11,17,18,23), index_col=0, header=0)
    #print(enp7)
    enp7.to_csv(dircsvenp7)


    enp7=open(dircsvenp7)
    nombrescol=enp7.read()
    texto1=nombrescol.replace("Out","temperatura")
    texto2=texto1.replace("Hum","humedadRelativa")
    texto3=texto2.replace("Pt.","puntoRocio")
    texto4=texto3.replace("Speed.1","velocidadRacha")
    texto5=texto4.replace("Dir.1","direccionRacha")
    texto6=texto5.replace("Speed","velocidadViento")
    texto7=texto6.replace("Dir","direccionViento")
    texto8=texto7.replace("Bar","presionBar")
    texto9=texto8.replace("Rain","lluvia")
    texto10=texto9.replace("Index.3","UV")

    enp71=open(dircsvenp7,"w")
    enp71.write(texto10)
    enp71.close()
    enp7.close()

    enp7=open(dircsvenp7)
    texto=enp7.read()
    texto1=texto.replace("NNE","22.5")
    texto2=texto1.replace("ENE","67.5")
    texto3=texto2.replace("ESE","112.5")
    texto4=texto3.replace("SSE","157.5")
    texto5=texto4.replace("SSW","202.5")
    texto6=texto5.replace("WSW","247.5")
    texto7=texto6.replace("WNW","292.5")
    texto8=texto7.replace("NNW","337.5")
    texto9=texto8.replace("NE","45")
    texto10=texto9.replace("SE","135")
    texto11=texto10.replace("SW","225")
    texto12=texto11.replace("NW","315")
    enp71=open(dircsvenp7,"w")
    enp71.write(texto12)
    enp71.close()
    enp7.close()

    enp7=open(dircsvenp7)
    texto=enp7.read()
    texto1=texto.replace("N","360")
    texto2=texto1.replace("E","90")
    texto3=texto2.replace("S","180")
    texto4=texto3.replace("W","270")
    enp71=open(dircsvenp7,"w")
    enp71.write(texto4)
    enp71.close()
    enp7.close()

    enp7=pd.read_csv(dircsvenp7, index_col=0, header=0)
    #print(enp7)
    enp7['fechaHora']=enp7['Fecha'].map(str)  + ' ' + enp7['Time'].map(str)
    enp7
    #print(enp7)
    enp7.to_csv(dircsvenp7)


    DF=pd.read_csv(dircsvenp7, index_col=0)
    DF['idEstacion']=np.where(DF['Time'] !='[]', 'enp7', ' ', )
    #print(DF)
    DF.to_csv(dircsvenp7)

    enp7=pd.read_csv(dircsvenp7, usecols=(3,4,5,6,7,8,9,10,11,12,13), index_col=0, header=0)
    #print(enp7)
    enp7.to_csv(dircsvenp7)


    # try:
    #     enp7=pd.read_csv(dircsvenp7, index_col=0)
    #     filter= (enp7['fechaHora'] <= fecha_ayer1) & (enp7['fechaHora'] < fecha_hoy1)
    #     filtrado=enp7.loc[filter]
    #     #print(filtrado)
    #     filtrado.to_csv(dircsvenp7)
    #     print("Filtrado")
    # except:
    #     print("No se logro filtrar datos por fecha actual")


    print('Datos de la estación enp7 listos')
except:
    print("No se logro obtener datos de la estación enp7")
    remove(dircsvenp7)

print('enp8')
try:
    print(espacio)
    file1 = dirtxtenp8
    r = urllib.request.urlopen(urlenp8)
    f = open(file1,'wb')
    f.write(r.read())
    f.close()
    #print(file1)
    print('Datos de la estación enp8 obtenidos')

    try:
        with open(dirtxtenp8, 'r') as fr:
            # reading line by line
            lines = fr.readlines()

            # pointer for position
            ptr = 1

            # opening in writing mode
            with open(dirtxtenp8, 'w') as fw:
                for line in lines:

                    # we want to remove 5th line
                    if ptr != 1:
                        fw.write(line)
                    ptr += 1
        print("Deleted")

    except:
        print("Oops! No se pudo eliminar fila")

    try:
        with open(dirtxtenp8, 'r') as fr:
            # reading line by line
            lines = fr.readlines()

            # pointer for position
            ptr = 1

            # opening in writing mode
            with open(dirtxtenp8, 'w') as fw:
                for line in lines:

                    # we want to remove 5th line
                    if ptr != 2:
                        fw.write(line)
                    ptr += 1
        print("Deleted")

    except:
        print("Oops! No se pudo eliminar fila")


    enp8=open(dirtxtenp8)
    texto0=enp8.read()
    texto1=texto0.replace(" ",",")
    texto2=texto1.replace("---","9999")
    texto3=texto2.replace(",,",",")
    texto4=texto3.replace(",,,",",")
    texto5=texto4.replace(",,,,",",")
    texto6=texto5.replace(fecha_ayer0,fecha_ayerc)
    texto7=texto6.replace(fecha_hoy0,fecha_hoyc)
    #print(texto7)
    enp81=open(dirtxtenp8,"w")
    enp81.write(texto7)
    enp81.close()

    enp8=open(dirtxtenp8)
    texto=enp8.read()
    texto0=texto.replace("12:00a","00:00")
    texto1=texto0.replace("12:10a","00:10")
    texto2=texto1.replace("12:20a","00:20")
    texto3=texto2.replace("12:30a","00:30")
    texto4=texto3.replace("12:40a","00:40")
    texto5=texto4.replace("12:50a","00:50")
    texto6=texto5.replace("1:00a","1:00")
    texto7=texto6.replace("1:10a","1:10")
    texto8=texto7.replace("1:20a","1:20")
    texto9=texto8.replace("1:30a","1:30")
    texto10=texto9.replace("1:40a","1:40")
    texto11=texto10.replace("1:50a","1:50")
    texto12=texto11.replace("2:00a","2:00")
    texto13=texto12.replace("2:10a","2:10")
    texto14=texto13.replace("2:20a","2:20")
    texto15=texto14.replace("2:30a","2:30")
    texto16=texto15.replace("2:40a","2:40")
    texto17=texto16.replace("2:50a","2:50")
    texto18=texto17.replace("3:00a","3:00")
    texto19=texto18.replace("3:10a","3:10")
    texto20=texto19.replace("3:20a","3:20")
    texto21=texto20.replace("3:30a","3:30")
    texto22=texto21.replace("3:40a","3:40")
    texto23=texto22.replace("3:50a","3:50")
    texto24=texto23.replace("4:00a","4:00")
    texto25=texto24.replace("4:10a","4:10")
    texto26=texto25.replace("4:20a","4:20")
    texto27=texto26.replace("4:30a","4:30")
    texto28=texto27.replace("4:40a","4:40")
    texto29=texto28.replace("4:50a","4:50")
    texto30=texto29.replace("5:00a","5:00")
    texto31=texto30.replace("5:10a","5:10")
    texto32=texto31.replace("5:20a","5:20")
    texto33=texto32.replace("5:30a","5:30")
    texto34=texto33.replace("5:40a","5:40")
    texto35=texto34.replace("5:50a","5:50")
    texto36=texto35.replace("6:00a","6:00")
    texto37=texto36.replace("6:10a","6:10")
    texto38=texto37.replace("6:20a","6:20")
    texto39=texto38.replace("6:30a","6:30")
    texto40=texto39.replace("6:40a","6:40")
    texto41=texto40.replace("6:50a","6:50")
    texto42=texto41.replace("7:00a","7:00")
    texto43=texto42.replace("7:10a","7:10")
    texto44=texto43.replace("7:20a","7:20")
    texto45=texto44.replace("7:30a","7:30")
    texto46=texto45.replace("7:40a","7:40")
    texto47=texto46.replace("7:50a","7:50")
    texto48=texto47.replace("8:00a","8:00")
    texto49=texto48.replace("8:10a","8:10")
    texto50=texto49.replace("8:20a","8:20")
    texto51=texto50.replace("8:30a","8:30")
    texto52=texto51.replace("8:40a","8:40")
    texto53=texto52.replace("8:50a","8:50")
    texto54=texto53.replace("9:00a","9:00")
    texto55=texto54.replace("9:10a","9:10")
    texto56=texto55.replace("9:20a","9:20")
    texto57=texto56.replace("9:30a","9:30")
    texto58=texto57.replace("9:40a","9:40")
    texto59=texto58.replace("9:50a","9:50")
    texto60=texto59.replace("10:00a","10:00")
    texto61=texto60.replace("10:10a","10:10")
    texto62=texto61.replace("10:20a","10:20")
    texto63=texto62.replace("10:30a","10:30")
    texto64=texto63.replace("10:40a","10:40")
    texto65=texto64.replace("10:50a","10:50")
    texto66=texto65.replace("11:00a","11:00")
    texto67=texto66.replace("11:10a","11:10")
    texto68=texto67.replace("11:20a","11:20")
    texto69=texto68.replace("11:30a","11:30")
    texto70=texto69.replace("11:40a","11:40")
    texto71=texto70.replace("11:50a","11:50")
    texto72=texto71.replace("12:00p","12:00")
    texto73=texto72.replace("12:10p","12:10")
    texto74=texto73.replace("12:20p","12:20")
    texto75=texto74.replace("12:30p","12:30")
    texto76=texto75.replace("12:40p","12:40")
    texto77=texto76.replace("12:50p","12:50")
    texto78=texto77.replace("1:00p","13:00")
    texto79=texto78.replace("1:10p","13:10")
    texto80=texto79.replace("1:20p","13:20")
    texto81=texto80.replace("1:30p","13:30")
    texto82=texto81.replace("1:40p","13:40")
    texto83=texto82.replace("1:50p","13:50")
    texto84=texto83.replace("2:00p","14:00")
    texto85=texto84.replace("2:10p","14:10")
    texto86=texto85.replace("2:20p","14:20")
    texto87=texto86.replace("2:30p","14:30")
    texto88=texto87.replace("2:40p","14:40")
    texto89=texto88.replace("2:50p","14:50")
    texto90=texto89.replace("3:00p","15:00")
    texto91=texto90.replace("3:10p","15:10")
    texto92=texto91.replace("3:20p","15:20")
    texto93=texto92.replace("3:30p","15:30")
    texto94=texto93.replace("3:40p","15:40")
    texto95=texto94.replace("3:50p","15:50")
    texto96=texto95.replace("4:00p","16:00")
    texto97=texto96.replace("4:10p","16:10")
    texto98=texto97.replace("4:20p","16:20")
    texto99=texto98.replace("4:30p","16:30")
    texto100=texto99.replace("4:40p","16:40")
    texto11=texto100.replace("4:50p","16:50")
    texto12=texto11.replace("5:00p","17:00")
    texto13=texto12.replace("5:10p","17:10")
    texto14=texto13.replace("5:20p","17:20")
    texto15=texto14.replace("5:30p","17:30")
    texto16=texto15.replace("5:40p","17:40")
    texto17=texto16.replace("5:50p","17:50")
    texto18=texto17.replace("6:00p","18:00")
    texto19=texto18.replace("6:10p","18:10")
    texto110=texto19.replace("6:20p","18:20")
    texto111=texto110.replace("6:30p","18:30")
    texto112=texto111.replace("6:40p","18:40")
    texto113=texto112.replace("6:50p","18:50")
    texto114=texto113.replace("7:00p","19:00")
    texto115=texto114.replace("7:10p","19:10")
    texto116=texto115.replace("7:20p","19:20")
    texto117=texto116.replace("7:30p","19:30")
    texto118=texto117.replace("7:40p","19:40")
    texto119=texto118.replace("7:50p","19:50")
    texto120=texto119.replace("8:00p","20:00")
    texto121=texto120.replace("8:10p","20:10")
    texto122=texto121.replace("8:20p","20:20")
    texto123=texto122.replace("8:30p","20:30")
    texto124=texto123.replace("8:40p","20:40")
    texto125=texto124.replace("8:50p","20:50")
    texto126=texto125.replace("9:00p","21:00")
    texto127=texto126.replace("9:10p","21:10")
    texto128=texto127.replace("9:20p","21:20")
    texto129=texto128.replace("9:30p","21:30")
    texto130=texto129.replace("9:40p","21:40")
    texto131=texto130.replace("9:50p","21:50")
    texto132=texto131.replace("10:00p","22:00")
    texto133=texto132.replace("10:10p","22:10")
    texto134=texto133.replace("10:20p","22:20")
    texto135=texto134.replace("10:30p","22:30")
    texto136=texto135.replace("10:40p","22:40")
    texto137=texto136.replace("10:50p","22:50")
    texto138=texto137.replace("11:00p","23:00")
    texto139=texto138.replace("11:10p","23:10")
    texto140=texto139.replace("11:20p","23:20")
    texto141=texto140.replace("11:30p","23:30")
    texto142=texto141.replace("11:40p","23:40")
    texto143=texto142.replace("11:50p","23:50")
    texto144=texto143.replace("113:00","23:00")
    texto145=texto144.replace("113:10","23:10")
    texto146=texto145.replace("113:20","23:20")
    texto147=texto146.replace("113:30","23:30")
    texto148=texto147.replace("113:40","23:40")
    texto149=texto148.replace("113:50","23:50")
    enp81=open(dirtxtenp8,"w")
    enp81.write(texto149)
    enp81.close()
    enp8.close()

    enp8=open(dirtxtenp8)
    texto0=enp8.read()
    texto1=texto0.replace(",,",",")
    texto2=texto1.replace(",Date",",Fecha")
    enp81=open(dircsvenp8,"w")
    enp81.write(texto2)
    #print(texto2)
    enp81.close()
    enp8.close()

    enp8=pd.read_csv(dircsvenp8, usecols=(1,2,3,6,7,8,10,11,17,18,23), index_col=0, header=0)
    #print(enp8)
    enp8.to_csv(dircsvenp8)


    enp8=open(dircsvenp8)
    nombrescol=enp8.read()
    texto1=nombrescol.replace("Out","temperatura")
    texto2=texto1.replace("Hum","humedadRelativa")
    texto3=texto2.replace("Pt.","puntoRocio")
    texto4=texto3.replace("Speed.1","velocidadRacha")
    texto5=texto4.replace("Dir.1","direccionRacha")
    texto6=texto5.replace("Speed","velocidadViento")
    texto7=texto6.replace("Dir","direccionViento")
    texto8=texto7.replace("Bar","presionBar")
    texto9=texto8.replace("Rain","lluvia")
    texto10=texto9.replace("Index.3","UV")

    enp81=open(dircsvenp8,"w")
    enp81.write(texto10)
    enp81.close()
    enp8.close()

    enp8=open(dircsvenp8)
    texto=enp8.read()
    texto1=texto.replace("NNE","22.5")
    texto2=texto1.replace("ENE","67.5")
    texto3=texto2.replace("ESE","112.5")
    texto4=texto3.replace("SSE","157.5")
    texto5=texto4.replace("SSW","202.5")
    texto6=texto5.replace("WSW","247.5")
    texto7=texto6.replace("WNW","292.5")
    texto8=texto7.replace("NNW","337.5")
    texto9=texto8.replace("NE","45")
    texto10=texto9.replace("SE","135")
    texto11=texto10.replace("SW","225")
    texto12=texto11.replace("NW","315")
    enp81=open(dircsvenp8,"w")
    enp81.write(texto12)
    enp81.close()
    enp8.close()

    enp8=open(dircsvenp8)
    texto=enp8.read()
    texto1=texto.replace("N","360")
    texto2=texto1.replace("E","90")
    texto3=texto2.replace("S","180")
    texto4=texto3.replace("W","270")
    enp81=open(dircsvenp8,"w")
    enp81.write(texto4)
    enp81.close()
    enp8.close()

    enp8=pd.read_csv(dircsvenp8, index_col=0, header=0)
    #print(enp8)
    enp8['fechaHora']=enp8['Fecha'].map(str)  + ' ' + enp8['Time'].map(str)
    enp8
    #print(enp8)
    enp8.to_csv(dircsvenp8)


    DF=pd.read_csv(dircsvenp8, index_col=0)
    DF['idEstacion']=np.where(DF['Time'] !='[]', 'enp8', ' ', )
    #print(DF)
    DF.to_csv(dircsvenp8)

    enp8=pd.read_csv(dircsvenp8, usecols=(3,4,5,6,7,8,9,10,11,12,13), index_col=0, header=0)
    #print(enp8)
    enp8.to_csv(dircsvenp8)


    # try:
    #     enp8=pd.read_csv(dircsvenp8, index_col=0)
    #     filter= (enp8['fechaHora'] <= fecha_ayer1) & (enp8['fechaHora'] < fecha_hoy1)
    #     filtrado=enp8.loc[filter]
    #     #print(filtrado)
    #     filtrado.to_csv(dircsvenp8)
    #     print("Filtrado")
    # except:
    #     print("No se logro filtrar datos por fecha actual")


    print('Datos de la estación enp8 listos')
except:
    print("No se logro obtener datos de la estación enp8")
    remove(dircsvenp8)

print('enp9')
try:
    print(espacio)
    file1 = dirtxtenp9
    r = urllib.request.urlopen(urlenp9)
    f = open(file1,'wb')
    f.write(r.read())
    f.close()
    #print(file1)
    print('Datos de la estación enp9 obtenidos')

    try:
        with open(dirtxtenp9, 'r') as fr:
            # reading line by line
            lines = fr.readlines()

            # pointer for position
            ptr = 1

            # opening in writing mode
            with open(dirtxtenp9, 'w') as fw:
                for line in lines:

                    # we want to remove 5th line
                    if ptr != 1:
                        fw.write(line)
                    ptr += 1
        print("Deleted")

    except:
        print("Oops! No se pudo eliminar fila")

    try:
        with open(dirtxtenp9, 'r') as fr:
            # reading line by line
            lines = fr.readlines()

            # pointer for position
            ptr = 1

            # opening in writing mode
            with open(dirtxtenp9, 'w') as fw:
                for line in lines:

                    # we want to remove 5th line
                    if ptr != 2:
                        fw.write(line)
                    ptr += 1
        print("Deleted")

    except:
        print("Oops! No se pudo eliminar fila")


    enp9=open(dirtxtenp9)
    texto0=enp9.read()
    texto1=texto0.replace(" ",",")
    texto2=texto1.replace("---","9999")
    texto3=texto2.replace(",,",",")
    texto4=texto3.replace(",,,",",")
    texto5=texto4.replace(",,,,",",")
    texto6=texto5.replace(fecha_ayer0,fecha_ayerc)
    texto7=texto6.replace(fecha_hoy0,fecha_hoyc)
    #print(texto7)
    enp91=open(dirtxtenp9,"w")
    enp91.write(texto7)
    enp91.close()

    enp9=open(dirtxtenp9)
    texto=enp9.read()
    texto0=texto.replace("12:00a","00:00")
    texto1=texto0.replace("12:10a","00:10")
    texto2=texto1.replace("12:20a","00:20")
    texto3=texto2.replace("12:30a","00:30")
    texto4=texto3.replace("12:40a","00:40")
    texto5=texto4.replace("12:50a","00:50")
    texto6=texto5.replace("1:00a","1:00")
    texto7=texto6.replace("1:10a","1:10")
    texto8=texto7.replace("1:20a","1:20")
    texto9=texto8.replace("1:30a","1:30")
    texto10=texto9.replace("1:40a","1:40")
    texto11=texto10.replace("1:50a","1:50")
    texto12=texto11.replace("2:00a","2:00")
    texto13=texto12.replace("2:10a","2:10")
    texto14=texto13.replace("2:20a","2:20")
    texto15=texto14.replace("2:30a","2:30")
    texto16=texto15.replace("2:40a","2:40")
    texto17=texto16.replace("2:50a","2:50")
    texto18=texto17.replace("3:00a","3:00")
    texto19=texto18.replace("3:10a","3:10")
    texto20=texto19.replace("3:20a","3:20")
    texto21=texto20.replace("3:30a","3:30")
    texto22=texto21.replace("3:40a","3:40")
    texto23=texto22.replace("3:50a","3:50")
    texto24=texto23.replace("4:00a","4:00")
    texto25=texto24.replace("4:10a","4:10")
    texto26=texto25.replace("4:20a","4:20")
    texto27=texto26.replace("4:30a","4:30")
    texto28=texto27.replace("4:40a","4:40")
    texto29=texto28.replace("4:50a","4:50")
    texto30=texto29.replace("5:00a","5:00")
    texto31=texto30.replace("5:10a","5:10")
    texto32=texto31.replace("5:20a","5:20")
    texto33=texto32.replace("5:30a","5:30")
    texto34=texto33.replace("5:40a","5:40")
    texto35=texto34.replace("5:50a","5:50")
    texto36=texto35.replace("6:00a","6:00")
    texto37=texto36.replace("6:10a","6:10")
    texto38=texto37.replace("6:20a","6:20")
    texto39=texto38.replace("6:30a","6:30")
    texto40=texto39.replace("6:40a","6:40")
    texto41=texto40.replace("6:50a","6:50")
    texto42=texto41.replace("7:00a","7:00")
    texto43=texto42.replace("7:10a","7:10")
    texto44=texto43.replace("7:20a","7:20")
    texto45=texto44.replace("7:30a","7:30")
    texto46=texto45.replace("7:40a","7:40")
    texto47=texto46.replace("7:50a","7:50")
    texto48=texto47.replace("8:00a","8:00")
    texto49=texto48.replace("8:10a","8:10")
    texto50=texto49.replace("8:20a","8:20")
    texto51=texto50.replace("8:30a","8:30")
    texto52=texto51.replace("8:40a","8:40")
    texto53=texto52.replace("8:50a","8:50")
    texto54=texto53.replace("9:00a","9:00")
    texto55=texto54.replace("9:10a","9:10")
    texto56=texto55.replace("9:20a","9:20")
    texto57=texto56.replace("9:30a","9:30")
    texto58=texto57.replace("9:40a","9:40")
    texto59=texto58.replace("9:50a","9:50")
    texto60=texto59.replace("10:00a","10:00")
    texto61=texto60.replace("10:10a","10:10")
    texto62=texto61.replace("10:20a","10:20")
    texto63=texto62.replace("10:30a","10:30")
    texto64=texto63.replace("10:40a","10:40")
    texto65=texto64.replace("10:50a","10:50")
    texto66=texto65.replace("11:00a","11:00")
    texto67=texto66.replace("11:10a","11:10")
    texto68=texto67.replace("11:20a","11:20")
    texto69=texto68.replace("11:30a","11:30")
    texto70=texto69.replace("11:40a","11:40")
    texto71=texto70.replace("11:50a","11:50")
    texto72=texto71.replace("12:00p","12:00")
    texto73=texto72.replace("12:10p","12:10")
    texto74=texto73.replace("12:20p","12:20")
    texto75=texto74.replace("12:30p","12:30")
    texto76=texto75.replace("12:40p","12:40")
    texto77=texto76.replace("12:50p","12:50")
    texto78=texto77.replace("1:00p","13:00")
    texto79=texto78.replace("1:10p","13:10")
    texto80=texto79.replace("1:20p","13:20")
    texto81=texto80.replace("1:30p","13:30")
    texto82=texto81.replace("1:40p","13:40")
    texto83=texto82.replace("1:50p","13:50")
    texto84=texto83.replace("2:00p","14:00")
    texto85=texto84.replace("2:10p","14:10")
    texto86=texto85.replace("2:20p","14:20")
    texto87=texto86.replace("2:30p","14:30")
    texto88=texto87.replace("2:40p","14:40")
    texto89=texto88.replace("2:50p","14:50")
    texto90=texto89.replace("3:00p","15:00")
    texto91=texto90.replace("3:10p","15:10")
    texto92=texto91.replace("3:20p","15:20")
    texto93=texto92.replace("3:30p","15:30")
    texto94=texto93.replace("3:40p","15:40")
    texto95=texto94.replace("3:50p","15:50")
    texto96=texto95.replace("4:00p","16:00")
    texto97=texto96.replace("4:10p","16:10")
    texto98=texto97.replace("4:20p","16:20")
    texto99=texto98.replace("4:30p","16:30")
    texto100=texto99.replace("4:40p","16:40")
    texto11=texto100.replace("4:50p","16:50")
    texto12=texto11.replace("5:00p","17:00")
    texto13=texto12.replace("5:10p","17:10")
    texto14=texto13.replace("5:20p","17:20")
    texto15=texto14.replace("5:30p","17:30")
    texto16=texto15.replace("5:40p","17:40")
    texto17=texto16.replace("5:50p","17:50")
    texto18=texto17.replace("6:00p","18:00")
    texto19=texto18.replace("6:10p","18:10")
    texto110=texto19.replace("6:20p","18:20")
    texto111=texto110.replace("6:30p","18:30")
    texto112=texto111.replace("6:40p","18:40")
    texto113=texto112.replace("6:50p","18:50")
    texto114=texto113.replace("7:00p","19:00")
    texto115=texto114.replace("7:10p","19:10")
    texto116=texto115.replace("7:20p","19:20")
    texto117=texto116.replace("7:30p","19:30")
    texto118=texto117.replace("7:40p","19:40")
    texto119=texto118.replace("7:50p","19:50")
    texto120=texto119.replace("8:00p","20:00")
    texto121=texto120.replace("8:10p","20:10")
    texto122=texto121.replace("8:20p","20:20")
    texto123=texto122.replace("8:30p","20:30")
    texto124=texto123.replace("8:40p","20:40")
    texto125=texto124.replace("8:50p","20:50")
    texto126=texto125.replace("9:00p","21:00")
    texto127=texto126.replace("9:10p","21:10")
    texto128=texto127.replace("9:20p","21:20")
    texto129=texto128.replace("9:30p","21:30")
    texto130=texto129.replace("9:40p","21:40")
    texto131=texto130.replace("9:50p","21:50")
    texto132=texto131.replace("10:00p","22:00")
    texto133=texto132.replace("10:10p","22:10")
    texto134=texto133.replace("10:20p","22:20")
    texto135=texto134.replace("10:30p","22:30")
    texto136=texto135.replace("10:40p","22:40")
    texto137=texto136.replace("10:50p","22:50")
    texto138=texto137.replace("11:00p","23:00")
    texto139=texto138.replace("11:10p","23:10")
    texto140=texto139.replace("11:20p","23:20")
    texto141=texto140.replace("11:30p","23:30")
    texto142=texto141.replace("11:40p","23:40")
    texto143=texto142.replace("11:50p","23:50")
    texto144=texto143.replace("113:00","23:00")
    texto145=texto144.replace("113:10","23:10")
    texto146=texto145.replace("113:20","23:20")
    texto147=texto146.replace("113:30","23:30")
    texto148=texto147.replace("113:40","23:40")
    texto149=texto148.replace("113:50","23:50")
    enp91=open(dirtxtenp9,"w")
    enp91.write(texto149)
    enp91.close()
    enp9.close()

    enp9=open(dirtxtenp9)
    texto0=enp9.read()
    texto1=texto0.replace(",,",",")
    texto2=texto1.replace(",Date",",Fecha")
    enp91=open(dircsvenp9,"w")
    enp91.write(texto2)
    #print(texto2)
    enp91.close()
    enp9.close()

    enp9=pd.read_csv(dircsvenp9, usecols=(1,2,3,6,7,8,10,11,17,18,23), index_col=0, header=0)
    #print(enp9)
    enp9.to_csv(dircsvenp9)


    enp9=open(dircsvenp9)
    nombrescol=enp9.read()
    texto1=nombrescol.replace("Out","temperatura")
    texto2=texto1.replace("Hum","humedadRelativa")
    texto3=texto2.replace("Pt.","puntoRocio")
    texto4=texto3.replace("Speed.1","velocidadRacha")
    texto5=texto4.replace("Dir.1","direccionRacha")
    texto6=texto5.replace("Speed","velocidadViento")
    texto7=texto6.replace("Dir","direccionViento")
    texto8=texto7.replace("Bar","presionBar")
    texto9=texto8.replace("Rain","lluvia")
    texto10=texto9.replace("Index.3","UV")

    enp91=open(dircsvenp9,"w")
    enp91.write(texto10)
    enp91.close()
    enp9.close()

    enp9=open(dircsvenp9)
    texto=enp9.read()
    texto1=texto.replace("NNE","22.5")
    texto2=texto1.replace("ENE","67.5")
    texto3=texto2.replace("ESE","112.5")
    texto4=texto3.replace("SSE","157.5")
    texto5=texto4.replace("SSW","202.5")
    texto6=texto5.replace("WSW","247.5")
    texto7=texto6.replace("WNW","292.5")
    texto8=texto7.replace("NNW","337.5")
    texto9=texto8.replace("NE","45")
    texto10=texto9.replace("SE","135")
    texto11=texto10.replace("SW","225")
    texto12=texto11.replace("NW","315")
    enp91=open(dircsvenp9,"w")
    enp91.write(texto12)
    enp91.close()
    enp9.close()

    enp9=open(dircsvenp9)
    texto=enp9.read()
    texto1=texto.replace("N","360")
    texto2=texto1.replace("E","90")
    texto3=texto2.replace("S","180")
    texto4=texto3.replace("W","270")
    enp91=open(dircsvenp9,"w")
    enp91.write(texto4)
    enp91.close()
    enp9.close()

    enp9=pd.read_csv(dircsvenp9, index_col=0, header=0)
    #print(enp9)
    enp9['fechaHora']=enp9['Fecha'].map(str)  + ' ' + enp9['Time'].map(str)
    enp9
    #print(enp9)
    enp9.to_csv(dircsvenp9)


    DF=pd.read_csv(dircsvenp9, index_col=0)
    DF['idEstacion']=np.where(DF['Time'] !='[]', 'enp9', ' ', )
    #print(DF)
    DF.to_csv(dircsvenp9)

    enp9=pd.read_csv(dircsvenp9, usecols=(3,4,5,6,7,8,9,10,11,12,13), index_col=0, header=0)
    #print(enp9)
    enp9.to_csv(dircsvenp9)


    # try:
    #     enp9=pd.read_csv(dircsvenp9, index_col=0)
    #     filter= (enp9['fechaHora'] <= fecha_ayer1) & (enp9['fechaHora'] < fecha_hoy1)
    #     filtrado=enp9.loc[filter]
    #     #print(filtrado)
    #     filtrado.to_csv(dircsvenp9)
    #     print("Filtrado")
    # except:
    #     print("No se logro filtrar datos por fecha actual")


    print('Datos de la estación enp9 listos')
except:
    print("No se logro obtener datos de la estación enp9")
    remove(dircsvenp9)

print('ccha')
try:
    print(espacio)
    file1 = dirtxtccha
    r = urllib.request.urlopen(urlccha)
    f = open(file1,'wb')
    f.write(r.read())
    f.close()
    #print(file1)
    print('Datos de la estación ccha obtenidos')

    try:
        with open(dirtxtccha, 'r') as fr:
            # reading line by line
            lines = fr.readlines()

            # pointer for position
            ptr = 1

            # opening in writing mode
            with open(dirtxtccha, 'w') as fw:
                for line in lines:

                    # we want to remove 5th line
                    if ptr != 1:
                        fw.write(line)
                    ptr += 1
        print("Deleted")

    except:
        print("Oops! No se pudo eliminar fila")

    try:
        with open(dirtxtccha, 'r') as fr:
            # reading line by line
            lines = fr.readlines()

            # pointer for position
            ptr = 1

            # opening in writing mode
            with open(dirtxtccha, 'w') as fw:
                for line in lines:

                    # we want to remove 5th line
                    if ptr != 2:
                        fw.write(line)
                    ptr += 1
        print("Deleted")

    except:
        print("Oops! No se pudo eliminar fila")


    ccha=open(dirtxtccha)
    texto0=ccha.read()
    texto1=texto0.replace(" ",",")
    texto2=texto1.replace("---","9999")
    texto3=texto2.replace(",,",",")
    texto4=texto3.replace(",,,",",")
    texto5=texto4.replace(",,,,",",")
    texto6=texto5.replace(fecha_ayer0,fecha_ayerc)
    texto7=texto6.replace(fecha_hoy0,fecha_hoyc)
    #print(texto7)
    ccha1=open(dirtxtccha,"w")
    ccha1.write(texto7)
    ccha1.close()

    ccha=open(dirtxtccha)
    texto=ccha.read()
    texto0=texto.replace("12:00a","00:00")
    texto1=texto0.replace("12:10a","00:10")
    texto2=texto1.replace("12:20a","00:20")
    texto3=texto2.replace("12:30a","00:30")
    texto4=texto3.replace("12:40a","00:40")
    texto5=texto4.replace("12:50a","00:50")
    texto6=texto5.replace("1:00a","1:00")
    texto7=texto6.replace("1:10a","1:10")
    texto8=texto7.replace("1:20a","1:20")
    texto9=texto8.replace("1:30a","1:30")
    texto10=texto9.replace("1:40a","1:40")
    texto11=texto10.replace("1:50a","1:50")
    texto12=texto11.replace("2:00a","2:00")
    texto13=texto12.replace("2:10a","2:10")
    texto14=texto13.replace("2:20a","2:20")
    texto15=texto14.replace("2:30a","2:30")
    texto16=texto15.replace("2:40a","2:40")
    texto17=texto16.replace("2:50a","2:50")
    texto18=texto17.replace("3:00a","3:00")
    texto19=texto18.replace("3:10a","3:10")
    texto20=texto19.replace("3:20a","3:20")
    texto21=texto20.replace("3:30a","3:30")
    texto22=texto21.replace("3:40a","3:40")
    texto23=texto22.replace("3:50a","3:50")
    texto24=texto23.replace("4:00a","4:00")
    texto25=texto24.replace("4:10a","4:10")
    texto26=texto25.replace("4:20a","4:20")
    texto27=texto26.replace("4:30a","4:30")
    texto28=texto27.replace("4:40a","4:40")
    texto29=texto28.replace("4:50a","4:50")
    texto30=texto29.replace("5:00a","5:00")
    texto31=texto30.replace("5:10a","5:10")
    texto32=texto31.replace("5:20a","5:20")
    texto33=texto32.replace("5:30a","5:30")
    texto34=texto33.replace("5:40a","5:40")
    texto35=texto34.replace("5:50a","5:50")
    texto36=texto35.replace("6:00a","6:00")
    texto37=texto36.replace("6:10a","6:10")
    texto38=texto37.replace("6:20a","6:20")
    texto39=texto38.replace("6:30a","6:30")
    texto40=texto39.replace("6:40a","6:40")
    texto41=texto40.replace("6:50a","6:50")
    texto42=texto41.replace("7:00a","7:00")
    texto43=texto42.replace("7:10a","7:10")
    texto44=texto43.replace("7:20a","7:20")
    texto45=texto44.replace("7:30a","7:30")
    texto46=texto45.replace("7:40a","7:40")
    texto47=texto46.replace("7:50a","7:50")
    texto48=texto47.replace("8:00a","8:00")
    texto49=texto48.replace("8:10a","8:10")
    texto50=texto49.replace("8:20a","8:20")
    texto51=texto50.replace("8:30a","8:30")
    texto52=texto51.replace("8:40a","8:40")
    texto53=texto52.replace("8:50a","8:50")
    texto54=texto53.replace("9:00a","9:00")
    texto55=texto54.replace("9:10a","9:10")
    texto56=texto55.replace("9:20a","9:20")
    texto57=texto56.replace("9:30a","9:30")
    texto58=texto57.replace("9:40a","9:40")
    texto59=texto58.replace("9:50a","9:50")
    texto60=texto59.replace("10:00a","10:00")
    texto61=texto60.replace("10:10a","10:10")
    texto62=texto61.replace("10:20a","10:20")
    texto63=texto62.replace("10:30a","10:30")
    texto64=texto63.replace("10:40a","10:40")
    texto65=texto64.replace("10:50a","10:50")
    texto66=texto65.replace("11:00a","11:00")
    texto67=texto66.replace("11:10a","11:10")
    texto68=texto67.replace("11:20a","11:20")
    texto69=texto68.replace("11:30a","11:30")
    texto70=texto69.replace("11:40a","11:40")
    texto71=texto70.replace("11:50a","11:50")
    texto72=texto71.replace("12:00p","12:00")
    texto73=texto72.replace("12:10p","12:10")
    texto74=texto73.replace("12:20p","12:20")
    texto75=texto74.replace("12:30p","12:30")
    texto76=texto75.replace("12:40p","12:40")
    texto77=texto76.replace("12:50p","12:50")
    texto78=texto77.replace("1:00p","13:00")
    texto79=texto78.replace("1:10p","13:10")
    texto80=texto79.replace("1:20p","13:20")
    texto81=texto80.replace("1:30p","13:30")
    texto82=texto81.replace("1:40p","13:40")
    texto83=texto82.replace("1:50p","13:50")
    texto84=texto83.replace("2:00p","14:00")
    texto85=texto84.replace("2:10p","14:10")
    texto86=texto85.replace("2:20p","14:20")
    texto87=texto86.replace("2:30p","14:30")
    texto88=texto87.replace("2:40p","14:40")
    texto89=texto88.replace("2:50p","14:50")
    texto90=texto89.replace("3:00p","15:00")
    texto91=texto90.replace("3:10p","15:10")
    texto92=texto91.replace("3:20p","15:20")
    texto93=texto92.replace("3:30p","15:30")
    texto94=texto93.replace("3:40p","15:40")
    texto95=texto94.replace("3:50p","15:50")
    texto96=texto95.replace("4:00p","16:00")
    texto97=texto96.replace("4:10p","16:10")
    texto98=texto97.replace("4:20p","16:20")
    texto99=texto98.replace("4:30p","16:30")
    texto100=texto99.replace("4:40p","16:40")
    texto11=texto100.replace("4:50p","16:50")
    texto12=texto11.replace("5:00p","17:00")
    texto13=texto12.replace("5:10p","17:10")
    texto14=texto13.replace("5:20p","17:20")
    texto15=texto14.replace("5:30p","17:30")
    texto16=texto15.replace("5:40p","17:40")
    texto17=texto16.replace("5:50p","17:50")
    texto18=texto17.replace("6:00p","18:00")
    texto19=texto18.replace("6:10p","18:10")
    texto110=texto19.replace("6:20p","18:20")
    texto111=texto110.replace("6:30p","18:30")
    texto112=texto111.replace("6:40p","18:40")
    texto113=texto112.replace("6:50p","18:50")
    texto114=texto113.replace("7:00p","19:00")
    texto115=texto114.replace("7:10p","19:10")
    texto116=texto115.replace("7:20p","19:20")
    texto117=texto116.replace("7:30p","19:30")
    texto118=texto117.replace("7:40p","19:40")
    texto119=texto118.replace("7:50p","19:50")
    texto120=texto119.replace("8:00p","20:00")
    texto121=texto120.replace("8:10p","20:10")
    texto122=texto121.replace("8:20p","20:20")
    texto123=texto122.replace("8:30p","20:30")
    texto124=texto123.replace("8:40p","20:40")
    texto125=texto124.replace("8:50p","20:50")
    texto126=texto125.replace("9:00p","21:00")
    texto127=texto126.replace("9:10p","21:10")
    texto128=texto127.replace("9:20p","21:20")
    texto129=texto128.replace("9:30p","21:30")
    texto130=texto129.replace("9:40p","21:40")
    texto131=texto130.replace("9:50p","21:50")
    texto132=texto131.replace("10:00p","22:00")
    texto133=texto132.replace("10:10p","22:10")
    texto134=texto133.replace("10:20p","22:20")
    texto135=texto134.replace("10:30p","22:30")
    texto136=texto135.replace("10:40p","22:40")
    texto137=texto136.replace("10:50p","22:50")
    texto138=texto137.replace("11:00p","23:00")
    texto139=texto138.replace("11:10p","23:10")
    texto140=texto139.replace("11:20p","23:20")
    texto141=texto140.replace("11:30p","23:30")
    texto142=texto141.replace("11:40p","23:40")
    texto143=texto142.replace("11:50p","23:50")
    texto144=texto143.replace("113:00","23:00")
    texto145=texto144.replace("113:10","23:10")
    texto146=texto145.replace("113:20","23:20")
    texto147=texto146.replace("113:30","23:30")
    texto148=texto147.replace("113:40","23:40")
    texto149=texto148.replace("113:50","23:50")
    ccha1=open(dirtxtccha,"w")
    ccha1.write(texto149)
    ccha1.close()
    ccha.close()

    ccha=open(dirtxtccha)
    texto0=ccha.read()
    texto1=texto0.replace(",,",",")
    texto2=texto1.replace(",Date",",Fecha")
    ccha1=open(dircsvccha,"w")
    ccha1.write(texto2)
    #print(texto2)
    ccha1.close()
    ccha.close()

    ccha=pd.read_csv(dircsvccha, usecols=(1,2,3,6,7,8,10,11,17,18,23), index_col=0, header=0)
    #print(ccha)
    ccha.to_csv(dircsvccha)


    ccha=open(dircsvccha)
    nombrescol=ccha.read()
    texto1=nombrescol.replace("Out","temperatura")
    texto2=texto1.replace("Hum","humedadRelativa")
    texto3=texto2.replace("Pt.","puntoRocio")
    texto4=texto3.replace("Speed.1","velocidadRacha")
    texto5=texto4.replace("Dir.1","direccionRacha")
    texto6=texto5.replace("Speed","velocidadViento")
    texto7=texto6.replace("Dir","direccionViento")
    texto8=texto7.replace("Bar","presionBar")
    texto9=texto8.replace("Rain","lluvia")
    texto10=texto9.replace("Index.3","UV")

    ccha1=open(dircsvccha,"w")
    ccha1.write(texto10)
    ccha1.close()
    ccha.close()

    ccha=open(dircsvccha)
    texto=ccha.read()
    texto1=texto.replace("NNE","22.5")
    texto2=texto1.replace("ENE","67.5")
    texto3=texto2.replace("ESE","112.5")
    texto4=texto3.replace("SSE","157.5")
    texto5=texto4.replace("SSW","202.5")
    texto6=texto5.replace("WSW","247.5")
    texto7=texto6.replace("WNW","292.5")
    texto8=texto7.replace("NNW","337.5")
    texto9=texto8.replace("NE","45")
    texto10=texto9.replace("SE","135")
    texto11=texto10.replace("SW","225")
    texto12=texto11.replace("NW","315")
    ccha1=open(dircsvccha,"w")
    ccha1.write(texto12)
    ccha1.close()
    ccha.close()

    ccha=open(dircsvccha)
    texto=ccha.read()
    texto1=texto.replace("N","360")
    texto2=texto1.replace("E","90")
    texto3=texto2.replace("S","180")
    texto4=texto3.replace("W","270")
    ccha1=open(dircsvccha,"w")
    ccha1.write(texto4)
    ccha1.close()
    ccha.close()

    ccha=pd.read_csv(dircsvccha, index_col=0, header=0)
    #print(ccha)
    ccha['fechaHora']=ccha['Fecha'].map(str)  + ' ' + ccha['Time'].map(str)
    ccha
    #print(ccha)
    ccha.to_csv(dircsvccha)


    DF=pd.read_csv(dircsvccha, index_col=0)
    DF['idEstacion']=np.where(DF['Time'] !='[]', 'ccha', ' ', )
    #print(DF)
    DF.to_csv(dircsvccha)

    ccha=pd.read_csv(dircsvccha, usecols=(3,4,5,6,7,8,9,10,11,12,13), index_col=0, header=0)
    #print(ccha)
    ccha.to_csv(dircsvccha)


    # try:
    #     ccha=pd.read_csv(dircsvccha, index_col=0)
    #     filter= (ccha['fechaHora'] <= fecha_ayer1) & (ccha['fechaHora'] < fecha_hoy1)
    #     filtrado=ccha.loc[filter]
    #     #print(filtrado)
    #     filtrado.to_csv(dircsvccha)
    #     print("Filtrado")
    # except:
    #     print("No se logro filtrar datos por fecha actual")


    print('Datos de la estación ccha listos')
except:
    print("No se logro obtener datos de la estación ccha")
    remove(dircsvccha)

print('cchn')
try:
    print(espacio)
    file1 = dirtxtcchn
    r = urllib.request.urlopen(urlcchn)
    f = open(file1,'wb')
    f.write(r.read())
    f.close()
    #print(file1)
    print('Datos de la estación cchn obtenidos')

    try:
        with open(dirtxtcchn, 'r') as fr:
            # reading line by line
            lines = fr.readlines()

            # pointer for position
            ptr = 1

            # opening in writing mode
            with open(dirtxtcchn, 'w') as fw:
                for line in lines:

                    # we want to remove 5th line
                    if ptr != 1:
                        fw.write(line)
                    ptr += 1
        print("Deleted")

    except:
        print("Oops! No se pudo eliminar fila")

    try:
        with open(dirtxtcchn, 'r') as fr:
            # reading line by line
            lines = fr.readlines()

            # pointer for position
            ptr = 1

            # opening in writing mode
            with open(dirtxtcchn, 'w') as fw:
                for line in lines:

                    # we want to remove 5th line
                    if ptr != 2:
                        fw.write(line)
                    ptr += 1
        print("Deleted")

    except:
        print("Oops! No se pudo eliminar fila")


    cchn=open(dirtxtcchn)
    texto0=cchn.read()
    texto1=texto0.replace(" ",",")
    texto2=texto1.replace("---","9999")
    texto3=texto2.replace(",,",",")
    texto4=texto3.replace(",,,",",")
    texto5=texto4.replace(",,,,",",")
    texto6=texto5.replace(fecha_ayer0,fecha_ayerc)
    texto7=texto6.replace(fecha_hoy0,fecha_hoyc)
    #print(texto7)
    cchn1=open(dirtxtcchn,"w")
    cchn1.write(texto7)
    cchn1.close()

    cchn=open(dirtxtcchn)
    texto=cchn.read()
    texto0=texto.replace("12:00a","00:00")
    texto1=texto0.replace("12:10a","00:10")
    texto2=texto1.replace("12:20a","00:20")
    texto3=texto2.replace("12:30a","00:30")
    texto4=texto3.replace("12:40a","00:40")
    texto5=texto4.replace("12:50a","00:50")
    texto6=texto5.replace("1:00a","1:00")
    texto7=texto6.replace("1:10a","1:10")
    texto8=texto7.replace("1:20a","1:20")
    texto9=texto8.replace("1:30a","1:30")
    texto10=texto9.replace("1:40a","1:40")
    texto11=texto10.replace("1:50a","1:50")
    texto12=texto11.replace("2:00a","2:00")
    texto13=texto12.replace("2:10a","2:10")
    texto14=texto13.replace("2:20a","2:20")
    texto15=texto14.replace("2:30a","2:30")
    texto16=texto15.replace("2:40a","2:40")
    texto17=texto16.replace("2:50a","2:50")
    texto18=texto17.replace("3:00a","3:00")
    texto19=texto18.replace("3:10a","3:10")
    texto20=texto19.replace("3:20a","3:20")
    texto21=texto20.replace("3:30a","3:30")
    texto22=texto21.replace("3:40a","3:40")
    texto23=texto22.replace("3:50a","3:50")
    texto24=texto23.replace("4:00a","4:00")
    texto25=texto24.replace("4:10a","4:10")
    texto26=texto25.replace("4:20a","4:20")
    texto27=texto26.replace("4:30a","4:30")
    texto28=texto27.replace("4:40a","4:40")
    texto29=texto28.replace("4:50a","4:50")
    texto30=texto29.replace("5:00a","5:00")
    texto31=texto30.replace("5:10a","5:10")
    texto32=texto31.replace("5:20a","5:20")
    texto33=texto32.replace("5:30a","5:30")
    texto34=texto33.replace("5:40a","5:40")
    texto35=texto34.replace("5:50a","5:50")
    texto36=texto35.replace("6:00a","6:00")
    texto37=texto36.replace("6:10a","6:10")
    texto38=texto37.replace("6:20a","6:20")
    texto39=texto38.replace("6:30a","6:30")
    texto40=texto39.replace("6:40a","6:40")
    texto41=texto40.replace("6:50a","6:50")
    texto42=texto41.replace("7:00a","7:00")
    texto43=texto42.replace("7:10a","7:10")
    texto44=texto43.replace("7:20a","7:20")
    texto45=texto44.replace("7:30a","7:30")
    texto46=texto45.replace("7:40a","7:40")
    texto47=texto46.replace("7:50a","7:50")
    texto48=texto47.replace("8:00a","8:00")
    texto49=texto48.replace("8:10a","8:10")
    texto50=texto49.replace("8:20a","8:20")
    texto51=texto50.replace("8:30a","8:30")
    texto52=texto51.replace("8:40a","8:40")
    texto53=texto52.replace("8:50a","8:50")
    texto54=texto53.replace("9:00a","9:00")
    texto55=texto54.replace("9:10a","9:10")
    texto56=texto55.replace("9:20a","9:20")
    texto57=texto56.replace("9:30a","9:30")
    texto58=texto57.replace("9:40a","9:40")
    texto59=texto58.replace("9:50a","9:50")
    texto60=texto59.replace("10:00a","10:00")
    texto61=texto60.replace("10:10a","10:10")
    texto62=texto61.replace("10:20a","10:20")
    texto63=texto62.replace("10:30a","10:30")
    texto64=texto63.replace("10:40a","10:40")
    texto65=texto64.replace("10:50a","10:50")
    texto66=texto65.replace("11:00a","11:00")
    texto67=texto66.replace("11:10a","11:10")
    texto68=texto67.replace("11:20a","11:20")
    texto69=texto68.replace("11:30a","11:30")
    texto70=texto69.replace("11:40a","11:40")
    texto71=texto70.replace("11:50a","11:50")
    texto72=texto71.replace("12:00p","12:00")
    texto73=texto72.replace("12:10p","12:10")
    texto74=texto73.replace("12:20p","12:20")
    texto75=texto74.replace("12:30p","12:30")
    texto76=texto75.replace("12:40p","12:40")
    texto77=texto76.replace("12:50p","12:50")
    texto78=texto77.replace("1:00p","13:00")
    texto79=texto78.replace("1:10p","13:10")
    texto80=texto79.replace("1:20p","13:20")
    texto81=texto80.replace("1:30p","13:30")
    texto82=texto81.replace("1:40p","13:40")
    texto83=texto82.replace("1:50p","13:50")
    texto84=texto83.replace("2:00p","14:00")
    texto85=texto84.replace("2:10p","14:10")
    texto86=texto85.replace("2:20p","14:20")
    texto87=texto86.replace("2:30p","14:30")
    texto88=texto87.replace("2:40p","14:40")
    texto89=texto88.replace("2:50p","14:50")
    texto90=texto89.replace("3:00p","15:00")
    texto91=texto90.replace("3:10p","15:10")
    texto92=texto91.replace("3:20p","15:20")
    texto93=texto92.replace("3:30p","15:30")
    texto94=texto93.replace("3:40p","15:40")
    texto95=texto94.replace("3:50p","15:50")
    texto96=texto95.replace("4:00p","16:00")
    texto97=texto96.replace("4:10p","16:10")
    texto98=texto97.replace("4:20p","16:20")
    texto99=texto98.replace("4:30p","16:30")
    texto100=texto99.replace("4:40p","16:40")
    texto11=texto100.replace("4:50p","16:50")
    texto12=texto11.replace("5:00p","17:00")
    texto13=texto12.replace("5:10p","17:10")
    texto14=texto13.replace("5:20p","17:20")
    texto15=texto14.replace("5:30p","17:30")
    texto16=texto15.replace("5:40p","17:40")
    texto17=texto16.replace("5:50p","17:50")
    texto18=texto17.replace("6:00p","18:00")
    texto19=texto18.replace("6:10p","18:10")
    texto110=texto19.replace("6:20p","18:20")
    texto111=texto110.replace("6:30p","18:30")
    texto112=texto111.replace("6:40p","18:40")
    texto113=texto112.replace("6:50p","18:50")
    texto114=texto113.replace("7:00p","19:00")
    texto115=texto114.replace("7:10p","19:10")
    texto116=texto115.replace("7:20p","19:20")
    texto117=texto116.replace("7:30p","19:30")
    texto118=texto117.replace("7:40p","19:40")
    texto119=texto118.replace("7:50p","19:50")
    texto120=texto119.replace("8:00p","20:00")
    texto121=texto120.replace("8:10p","20:10")
    texto122=texto121.replace("8:20p","20:20")
    texto123=texto122.replace("8:30p","20:30")
    texto124=texto123.replace("8:40p","20:40")
    texto125=texto124.replace("8:50p","20:50")
    texto126=texto125.replace("9:00p","21:00")
    texto127=texto126.replace("9:10p","21:10")
    texto128=texto127.replace("9:20p","21:20")
    texto129=texto128.replace("9:30p","21:30")
    texto130=texto129.replace("9:40p","21:40")
    texto131=texto130.replace("9:50p","21:50")
    texto132=texto131.replace("10:00p","22:00")
    texto133=texto132.replace("10:10p","22:10")
    texto134=texto133.replace("10:20p","22:20")
    texto135=texto134.replace("10:30p","22:30")
    texto136=texto135.replace("10:40p","22:40")
    texto137=texto136.replace("10:50p","22:50")
    texto138=texto137.replace("11:00p","23:00")
    texto139=texto138.replace("11:10p","23:10")
    texto140=texto139.replace("11:20p","23:20")
    texto141=texto140.replace("11:30p","23:30")
    texto142=texto141.replace("11:40p","23:40")
    texto143=texto142.replace("11:50p","23:50")
    texto144=texto143.replace("113:00","23:00")
    texto145=texto144.replace("113:10","23:10")
    texto146=texto145.replace("113:20","23:20")
    texto147=texto146.replace("113:30","23:30")
    texto148=texto147.replace("113:40","23:40")
    texto149=texto148.replace("113:50","23:50")
    cchn1=open(dirtxtcchn,"w")
    cchn1.write(texto149)
    cchn1.close()
    cchn.close()

    cchn=open(dirtxtcchn)
    texto0=cchn.read()
    texto1=texto0.replace(",,",",")
    texto2=texto1.replace(",Date",",Fecha")
    cchn1=open(dircsvcchn,"w")
    cchn1.write(texto2)
    #print(texto2)
    cchn1.close()
    cchn.close()

    cchn=pd.read_csv(dircsvcchn, usecols=(1,2,3,6,7,8,10,11,17,18,23), index_col=0, header=0)
    #print(cchn)
    cchn.to_csv(dircsvcchn)


    cchn=open(dircsvcchn)
    nombrescol=cchn.read()
    texto1=nombrescol.replace("Out","temperatura")
    texto2=texto1.replace("Hum","humedadRelativa")
    texto3=texto2.replace("Pt.","puntoRocio")
    texto4=texto3.replace("Speed.1","velocidadRacha")
    texto5=texto4.replace("Dir.1","direccionRacha")
    texto6=texto5.replace("Speed","velocidadViento")
    texto7=texto6.replace("Dir","direccionViento")
    texto8=texto7.replace("Bar","presionBar")
    texto9=texto8.replace("Rain","lluvia")
    texto10=texto9.replace("Index.3","UV")

    cchn1=open(dircsvcchn,"w")
    cchn1.write(texto10)
    cchn1.close()
    cchn.close()

    cchn=open(dircsvcchn)
    texto=cchn.read()
    texto1=texto.replace("NNE","22.5")
    texto2=texto1.replace("ENE","67.5")
    texto3=texto2.replace("ESE","112.5")
    texto4=texto3.replace("SSE","157.5")
    texto5=texto4.replace("SSW","202.5")
    texto6=texto5.replace("WSW","247.5")
    texto7=texto6.replace("WNW","292.5")
    texto8=texto7.replace("NNW","337.5")
    texto9=texto8.replace("NE","45")
    texto10=texto9.replace("SE","135")
    texto11=texto10.replace("SW","225")
    texto12=texto11.replace("NW","315")
    cchn1=open(dircsvcchn,"w")
    cchn1.write(texto12)
    cchn1.close()
    cchn.close()

    cchn=open(dircsvcchn)
    texto=cchn.read()
    texto1=texto.replace("N","360")
    texto2=texto1.replace("E","90")
    texto3=texto2.replace("S","180")
    texto4=texto3.replace("W","270")
    cchn1=open(dircsvcchn,"w")
    cchn1.write(texto4)
    cchn1.close()
    cchn.close()

    cchn=pd.read_csv(dircsvcchn, index_col=0, header=0)
    #print(cchn)
    cchn['fechaHora']=cchn['Fecha'].map(str)  + ' ' + cchn['Time'].map(str)
    cchn
    #print(cchn)
    cchn.to_csv(dircsvcchn)


    DF=pd.read_csv(dircsvcchn, index_col=0)
    DF['idEstacion']=np.where(DF['Time'] !='[]', 'cchn', ' ', )
    #print(DF)
    DF.to_csv(dircsvcchn)

    cchn=pd.read_csv(dircsvcchn, usecols=(3,4,5,6,7,8,9,10,11,12,13), index_col=0, header=0)
    #print(cchn)
    cchn.to_csv(dircsvcchn)


    # try:
    #     cchn=pd.read_csv(dircsvcchn, index_col=0)
    #     filter= (cchn['fechaHora'] <= fecha_ayer1) & (cchn['fechaHora'] < fecha_hoy1)
    #     filtrado=cchn.loc[filter]
    #     #print(filtrado)
    #     filtrado.to_csv(dircsvcchn)
    #     print("Filtrado")
    # except:
    #     print("No se logro filtrar datos por fecha actual")


    print('Datos de la estación cchn listos')
except:
    print("No se logro obtener datos de la estación cchn")
    remove(dircsvcchn)

print('ccho')
try:
    print(espacio)
    file1 = dirtxtccho
    r = urllib.request.urlopen(urlccho)
    f = open(file1,'wb')
    f.write(r.read())
    f.close()
    #print(file1)
    print('Datos de la estación ccho obtenidos')

    try:
        with open(dirtxtccho, 'r') as fr:
            # reading line by line
            lines = fr.readlines()

            # pointer for position
            ptr = 1

            # opening in writing mode
            with open(dirtxtccho, 'w') as fw:
                for line in lines:

                    # we want to remove 5th line
                    if ptr != 1:
                        fw.write(line)
                    ptr += 1
        print("Deleted")

    except:
        print("Oops! No se pudo eliminar fila")

    try:
        with open(dirtxtccho, 'r') as fr:
            # reading line by line
            lines = fr.readlines()

            # pointer for position
            ptr = 1

            # opening in writing mode
            with open(dirtxtccho, 'w') as fw:
                for line in lines:

                    # we want to remove 5th line
                    if ptr != 2:
                        fw.write(line)
                    ptr += 1
        print("Deleted")

    except:
        print("Oops! No se pudo eliminar fila")


    ccho=open(dirtxtccho)
    texto0=ccho.read()
    texto1=texto0.replace(" ",",")
    texto2=texto1.replace("---","9999")
    texto3=texto2.replace(",,",",")
    texto4=texto3.replace(",,,",",")
    texto5=texto4.replace(",,,,",",")
    texto6=texto5.replace(fecha_ayer0,fecha_ayerc)
    texto7=texto6.replace(fecha_hoy0,fecha_hoyc)
    #print(texto7)
    ccho1=open(dirtxtccho,"w")
    ccho1.write(texto7)
    ccho1.close()

    ccho=open(dirtxtccho)
    texto=ccho.read()
    texto0=texto.replace("12:00a","00:00")
    texto1=texto0.replace("12:10a","00:10")
    texto2=texto1.replace("12:20a","00:20")
    texto3=texto2.replace("12:30a","00:30")
    texto4=texto3.replace("12:40a","00:40")
    texto5=texto4.replace("12:50a","00:50")
    texto6=texto5.replace("1:00a","1:00")
    texto7=texto6.replace("1:10a","1:10")
    texto8=texto7.replace("1:20a","1:20")
    texto9=texto8.replace("1:30a","1:30")
    texto10=texto9.replace("1:40a","1:40")
    texto11=texto10.replace("1:50a","1:50")
    texto12=texto11.replace("2:00a","2:00")
    texto13=texto12.replace("2:10a","2:10")
    texto14=texto13.replace("2:20a","2:20")
    texto15=texto14.replace("2:30a","2:30")
    texto16=texto15.replace("2:40a","2:40")
    texto17=texto16.replace("2:50a","2:50")
    texto18=texto17.replace("3:00a","3:00")
    texto19=texto18.replace("3:10a","3:10")
    texto20=texto19.replace("3:20a","3:20")
    texto21=texto20.replace("3:30a","3:30")
    texto22=texto21.replace("3:40a","3:40")
    texto23=texto22.replace("3:50a","3:50")
    texto24=texto23.replace("4:00a","4:00")
    texto25=texto24.replace("4:10a","4:10")
    texto26=texto25.replace("4:20a","4:20")
    texto27=texto26.replace("4:30a","4:30")
    texto28=texto27.replace("4:40a","4:40")
    texto29=texto28.replace("4:50a","4:50")
    texto30=texto29.replace("5:00a","5:00")
    texto31=texto30.replace("5:10a","5:10")
    texto32=texto31.replace("5:20a","5:20")
    texto33=texto32.replace("5:30a","5:30")
    texto34=texto33.replace("5:40a","5:40")
    texto35=texto34.replace("5:50a","5:50")
    texto36=texto35.replace("6:00a","6:00")
    texto37=texto36.replace("6:10a","6:10")
    texto38=texto37.replace("6:20a","6:20")
    texto39=texto38.replace("6:30a","6:30")
    texto40=texto39.replace("6:40a","6:40")
    texto41=texto40.replace("6:50a","6:50")
    texto42=texto41.replace("7:00a","7:00")
    texto43=texto42.replace("7:10a","7:10")
    texto44=texto43.replace("7:20a","7:20")
    texto45=texto44.replace("7:30a","7:30")
    texto46=texto45.replace("7:40a","7:40")
    texto47=texto46.replace("7:50a","7:50")
    texto48=texto47.replace("8:00a","8:00")
    texto49=texto48.replace("8:10a","8:10")
    texto50=texto49.replace("8:20a","8:20")
    texto51=texto50.replace("8:30a","8:30")
    texto52=texto51.replace("8:40a","8:40")
    texto53=texto52.replace("8:50a","8:50")
    texto54=texto53.replace("9:00a","9:00")
    texto55=texto54.replace("9:10a","9:10")
    texto56=texto55.replace("9:20a","9:20")
    texto57=texto56.replace("9:30a","9:30")
    texto58=texto57.replace("9:40a","9:40")
    texto59=texto58.replace("9:50a","9:50")
    texto60=texto59.replace("10:00a","10:00")
    texto61=texto60.replace("10:10a","10:10")
    texto62=texto61.replace("10:20a","10:20")
    texto63=texto62.replace("10:30a","10:30")
    texto64=texto63.replace("10:40a","10:40")
    texto65=texto64.replace("10:50a","10:50")
    texto66=texto65.replace("11:00a","11:00")
    texto67=texto66.replace("11:10a","11:10")
    texto68=texto67.replace("11:20a","11:20")
    texto69=texto68.replace("11:30a","11:30")
    texto70=texto69.replace("11:40a","11:40")
    texto71=texto70.replace("11:50a","11:50")
    texto72=texto71.replace("12:00p","12:00")
    texto73=texto72.replace("12:10p","12:10")
    texto74=texto73.replace("12:20p","12:20")
    texto75=texto74.replace("12:30p","12:30")
    texto76=texto75.replace("12:40p","12:40")
    texto77=texto76.replace("12:50p","12:50")
    texto78=texto77.replace("1:00p","13:00")
    texto79=texto78.replace("1:10p","13:10")
    texto80=texto79.replace("1:20p","13:20")
    texto81=texto80.replace("1:30p","13:30")
    texto82=texto81.replace("1:40p","13:40")
    texto83=texto82.replace("1:50p","13:50")
    texto84=texto83.replace("2:00p","14:00")
    texto85=texto84.replace("2:10p","14:10")
    texto86=texto85.replace("2:20p","14:20")
    texto87=texto86.replace("2:30p","14:30")
    texto88=texto87.replace("2:40p","14:40")
    texto89=texto88.replace("2:50p","14:50")
    texto90=texto89.replace("3:00p","15:00")
    texto91=texto90.replace("3:10p","15:10")
    texto92=texto91.replace("3:20p","15:20")
    texto93=texto92.replace("3:30p","15:30")
    texto94=texto93.replace("3:40p","15:40")
    texto95=texto94.replace("3:50p","15:50")
    texto96=texto95.replace("4:00p","16:00")
    texto97=texto96.replace("4:10p","16:10")
    texto98=texto97.replace("4:20p","16:20")
    texto99=texto98.replace("4:30p","16:30")
    texto100=texto99.replace("4:40p","16:40")
    texto11=texto100.replace("4:50p","16:50")
    texto12=texto11.replace("5:00p","17:00")
    texto13=texto12.replace("5:10p","17:10")
    texto14=texto13.replace("5:20p","17:20")
    texto15=texto14.replace("5:30p","17:30")
    texto16=texto15.replace("5:40p","17:40")
    texto17=texto16.replace("5:50p","17:50")
    texto18=texto17.replace("6:00p","18:00")
    texto19=texto18.replace("6:10p","18:10")
    texto110=texto19.replace("6:20p","18:20")
    texto111=texto110.replace("6:30p","18:30")
    texto112=texto111.replace("6:40p","18:40")
    texto113=texto112.replace("6:50p","18:50")
    texto114=texto113.replace("7:00p","19:00")
    texto115=texto114.replace("7:10p","19:10")
    texto116=texto115.replace("7:20p","19:20")
    texto117=texto116.replace("7:30p","19:30")
    texto118=texto117.replace("7:40p","19:40")
    texto119=texto118.replace("7:50p","19:50")
    texto120=texto119.replace("8:00p","20:00")
    texto121=texto120.replace("8:10p","20:10")
    texto122=texto121.replace("8:20p","20:20")
    texto123=texto122.replace("8:30p","20:30")
    texto124=texto123.replace("8:40p","20:40")
    texto125=texto124.replace("8:50p","20:50")
    texto126=texto125.replace("9:00p","21:00")
    texto127=texto126.replace("9:10p","21:10")
    texto128=texto127.replace("9:20p","21:20")
    texto129=texto128.replace("9:30p","21:30")
    texto130=texto129.replace("9:40p","21:40")
    texto131=texto130.replace("9:50p","21:50")
    texto132=texto131.replace("10:00p","22:00")
    texto133=texto132.replace("10:10p","22:10")
    texto134=texto133.replace("10:20p","22:20")
    texto135=texto134.replace("10:30p","22:30")
    texto136=texto135.replace("10:40p","22:40")
    texto137=texto136.replace("10:50p","22:50")
    texto138=texto137.replace("11:00p","23:00")
    texto139=texto138.replace("11:10p","23:10")
    texto140=texto139.replace("11:20p","23:20")
    texto141=texto140.replace("11:30p","23:30")
    texto142=texto141.replace("11:40p","23:40")
    texto143=texto142.replace("11:50p","23:50")
    texto144=texto143.replace("113:00","23:00")
    texto145=texto144.replace("113:10","23:10")
    texto146=texto145.replace("113:20","23:20")
    texto147=texto146.replace("113:30","23:30")
    texto148=texto147.replace("113:40","23:40")
    texto149=texto148.replace("113:50","23:50")
    ccho1=open(dirtxtccho,"w")
    ccho1.write(texto149)
    ccho1.close()
    ccho.close()

    ccho=open(dirtxtccho)
    texto0=ccho.read()
    texto1=texto0.replace(",,",",")
    texto2=texto1.replace(",Date",",Fecha")
    ccho1=open(dircsvccho,"w")
    ccho1.write(texto2)
    #print(texto2)
    ccho1.close()
    ccho.close()

    ccho=pd.read_csv(dircsvccho, usecols=(1,2,3,6,7,8,10,11,17,18,23), index_col=0, header=0)
    #print(ccho)
    ccho.to_csv(dircsvccho)


    ccho=open(dircsvccho)
    nombrescol=ccho.read()
    texto1=nombrescol.replace("Out","temperatura")
    texto2=texto1.replace("Hum","humedadRelativa")
    texto3=texto2.replace("Pt.","puntoRocio")
    texto4=texto3.replace("Speed.1","velocidadRacha")
    texto5=texto4.replace("Dir.1","direccionRacha")
    texto6=texto5.replace("Speed","velocidadViento")
    texto7=texto6.replace("Dir","direccionViento")
    texto8=texto7.replace("Bar","presionBar")
    texto9=texto8.replace("Rain","lluvia")
    texto10=texto9.replace("Index.3","UV")

    ccho1=open(dircsvccho,"w")
    ccho1.write(texto10)
    ccho1.close()
    ccho.close()

    ccho=open(dircsvccho)
    texto=ccho.read()
    texto1=texto.replace("NNE","22.5")
    texto2=texto1.replace("ENE","67.5")
    texto3=texto2.replace("ESE","112.5")
    texto4=texto3.replace("SSE","157.5")
    texto5=texto4.replace("SSW","202.5")
    texto6=texto5.replace("WSW","247.5")
    texto7=texto6.replace("WNW","292.5")
    texto8=texto7.replace("NNW","337.5")
    texto9=texto8.replace("NE","45")
    texto10=texto9.replace("SE","135")
    texto11=texto10.replace("SW","225")
    texto12=texto11.replace("NW","315")
    ccho1=open(dircsvccho,"w")
    ccho1.write(texto12)
    ccho1.close()
    ccho.close()

    ccho=open(dircsvccho)
    texto=ccho.read()
    texto1=texto.replace("N","360")
    texto2=texto1.replace("E","90")
    texto3=texto2.replace("S","180")
    texto4=texto3.replace("W","270")
    ccho1=open(dircsvccho,"w")
    ccho1.write(texto4)
    ccho1.close()
    ccho.close()

    ccho=pd.read_csv(dircsvccho, index_col=0, header=0)
    #print(ccho)
    ccho['fechaHora']=ccho['Fecha'].map(str)  + ' ' + ccho['Time'].map(str)
    ccho
    #print(ccho)
    ccho.to_csv(dircsvccho)


    DF=pd.read_csv(dircsvccho, index_col=0)
    DF['idEstacion']=np.where(DF['Time'] !='[]', 'ccho', ' ', )
    #print(DF)
    DF.to_csv(dircsvccho)

    ccho=pd.read_csv(dircsvccho, usecols=(3,4,5,6,7,8,9,10,11,12,13), index_col=0, header=0)
    #print(ccho)
    ccho.to_csv(dircsvccho)


    # try:
    #     ccho=pd.read_csv(dircsvccho, index_col=0)
    #     filter= (ccho['fechaHora'] <= fecha_ayer1) & (ccho['fechaHora'] < fecha_hoy1)
    #     filtrado=ccho.loc[filter]
    #     #print(filtrado)
    #     filtrado.to_csv(dircsvccho)
    #     print("Filtrado")
    # except:
    #     print("No se logro filtrar datos por fecha actual")


    print('Datos de la estación ccho listos')
except:
    print("No se logro obtener datos de la estación ccho")
    remove(dircsvccho)

print('cchs')
try:
    print(espacio)
    file1 = dirtxtcchs
    r = urllib.request.urlopen(urlcchs)
    f = open(file1,'wb')
    f.write(r.read())
    f.close()
    #print(file1)
    print('Datos de la estación cchs obtenidos')

    try:
        with open(dirtxtcchs, 'r') as fr:
            # reading line by line
            lines = fr.readlines()

            # pointer for position
            ptr = 1

            # opening in writing mode
            with open(dirtxtcchs, 'w') as fw:
                for line in lines:

                    # we want to remove 5th line
                    if ptr != 1:
                        fw.write(line)
                    ptr += 1
        print("Deleted")

    except:
        print("Oops! No se pudo eliminar fila")

    try:
        with open(dirtxtcchs, 'r') as fr:
            # reading line by line
            lines = fr.readlines()

            # pointer for position
            ptr = 1

            # opening in writing mode
            with open(dirtxtcchs, 'w') as fw:
                for line in lines:

                    # we want to remove 5th line
                    if ptr != 2:
                        fw.write(line)
                    ptr += 1
        print("Deleted")

    except:
        print("Oops! No se pudo eliminar fila")


    cchs=open(dirtxtcchs)
    texto0=cchs.read()
    texto1=texto0.replace(" ",",")
    texto2=texto1.replace("---","9999")
    texto3=texto2.replace(",,",",")
    texto4=texto3.replace(",,,",",")
    texto5=texto4.replace(",,,,",",")
    texto6=texto5.replace(fecha_ayer0,fecha_ayerc)
    texto7=texto6.replace(fecha_hoy0,fecha_hoyc)
    #print(texto7)
    cchs1=open(dirtxtcchs,"w")
    cchs1.write(texto7)
    cchs1.close()

    cchs=open(dirtxtcchs)
    texto=cchs.read()
    texto0=texto.replace("12:00a","00:00")
    texto1=texto0.replace("12:10a","00:10")
    texto2=texto1.replace("12:20a","00:20")
    texto3=texto2.replace("12:30a","00:30")
    texto4=texto3.replace("12:40a","00:40")
    texto5=texto4.replace("12:50a","00:50")
    texto6=texto5.replace("1:00a","1:00")
    texto7=texto6.replace("1:10a","1:10")
    texto8=texto7.replace("1:20a","1:20")
    texto9=texto8.replace("1:30a","1:30")
    texto10=texto9.replace("1:40a","1:40")
    texto11=texto10.replace("1:50a","1:50")
    texto12=texto11.replace("2:00a","2:00")
    texto13=texto12.replace("2:10a","2:10")
    texto14=texto13.replace("2:20a","2:20")
    texto15=texto14.replace("2:30a","2:30")
    texto16=texto15.replace("2:40a","2:40")
    texto17=texto16.replace("2:50a","2:50")
    texto18=texto17.replace("3:00a","3:00")
    texto19=texto18.replace("3:10a","3:10")
    texto20=texto19.replace("3:20a","3:20")
    texto21=texto20.replace("3:30a","3:30")
    texto22=texto21.replace("3:40a","3:40")
    texto23=texto22.replace("3:50a","3:50")
    texto24=texto23.replace("4:00a","4:00")
    texto25=texto24.replace("4:10a","4:10")
    texto26=texto25.replace("4:20a","4:20")
    texto27=texto26.replace("4:30a","4:30")
    texto28=texto27.replace("4:40a","4:40")
    texto29=texto28.replace("4:50a","4:50")
    texto30=texto29.replace("5:00a","5:00")
    texto31=texto30.replace("5:10a","5:10")
    texto32=texto31.replace("5:20a","5:20")
    texto33=texto32.replace("5:30a","5:30")
    texto34=texto33.replace("5:40a","5:40")
    texto35=texto34.replace("5:50a","5:50")
    texto36=texto35.replace("6:00a","6:00")
    texto37=texto36.replace("6:10a","6:10")
    texto38=texto37.replace("6:20a","6:20")
    texto39=texto38.replace("6:30a","6:30")
    texto40=texto39.replace("6:40a","6:40")
    texto41=texto40.replace("6:50a","6:50")
    texto42=texto41.replace("7:00a","7:00")
    texto43=texto42.replace("7:10a","7:10")
    texto44=texto43.replace("7:20a","7:20")
    texto45=texto44.replace("7:30a","7:30")
    texto46=texto45.replace("7:40a","7:40")
    texto47=texto46.replace("7:50a","7:50")
    texto48=texto47.replace("8:00a","8:00")
    texto49=texto48.replace("8:10a","8:10")
    texto50=texto49.replace("8:20a","8:20")
    texto51=texto50.replace("8:30a","8:30")
    texto52=texto51.replace("8:40a","8:40")
    texto53=texto52.replace("8:50a","8:50")
    texto54=texto53.replace("9:00a","9:00")
    texto55=texto54.replace("9:10a","9:10")
    texto56=texto55.replace("9:20a","9:20")
    texto57=texto56.replace("9:30a","9:30")
    texto58=texto57.replace("9:40a","9:40")
    texto59=texto58.replace("9:50a","9:50")
    texto60=texto59.replace("10:00a","10:00")
    texto61=texto60.replace("10:10a","10:10")
    texto62=texto61.replace("10:20a","10:20")
    texto63=texto62.replace("10:30a","10:30")
    texto64=texto63.replace("10:40a","10:40")
    texto65=texto64.replace("10:50a","10:50")
    texto66=texto65.replace("11:00a","11:00")
    texto67=texto66.replace("11:10a","11:10")
    texto68=texto67.replace("11:20a","11:20")
    texto69=texto68.replace("11:30a","11:30")
    texto70=texto69.replace("11:40a","11:40")
    texto71=texto70.replace("11:50a","11:50")
    texto72=texto71.replace("12:00p","12:00")
    texto73=texto72.replace("12:10p","12:10")
    texto74=texto73.replace("12:20p","12:20")
    texto75=texto74.replace("12:30p","12:30")
    texto76=texto75.replace("12:40p","12:40")
    texto77=texto76.replace("12:50p","12:50")
    texto78=texto77.replace("1:00p","13:00")
    texto79=texto78.replace("1:10p","13:10")
    texto80=texto79.replace("1:20p","13:20")
    texto81=texto80.replace("1:30p","13:30")
    texto82=texto81.replace("1:40p","13:40")
    texto83=texto82.replace("1:50p","13:50")
    texto84=texto83.replace("2:00p","14:00")
    texto85=texto84.replace("2:10p","14:10")
    texto86=texto85.replace("2:20p","14:20")
    texto87=texto86.replace("2:30p","14:30")
    texto88=texto87.replace("2:40p","14:40")
    texto89=texto88.replace("2:50p","14:50")
    texto90=texto89.replace("3:00p","15:00")
    texto91=texto90.replace("3:10p","15:10")
    texto92=texto91.replace("3:20p","15:20")
    texto93=texto92.replace("3:30p","15:30")
    texto94=texto93.replace("3:40p","15:40")
    texto95=texto94.replace("3:50p","15:50")
    texto96=texto95.replace("4:00p","16:00")
    texto97=texto96.replace("4:10p","16:10")
    texto98=texto97.replace("4:20p","16:20")
    texto99=texto98.replace("4:30p","16:30")
    texto100=texto99.replace("4:40p","16:40")
    texto11=texto100.replace("4:50p","16:50")
    texto12=texto11.replace("5:00p","17:00")
    texto13=texto12.replace("5:10p","17:10")
    texto14=texto13.replace("5:20p","17:20")
    texto15=texto14.replace("5:30p","17:30")
    texto16=texto15.replace("5:40p","17:40")
    texto17=texto16.replace("5:50p","17:50")
    texto18=texto17.replace("6:00p","18:00")
    texto19=texto18.replace("6:10p","18:10")
    texto110=texto19.replace("6:20p","18:20")
    texto111=texto110.replace("6:30p","18:30")
    texto112=texto111.replace("6:40p","18:40")
    texto113=texto112.replace("6:50p","18:50")
    texto114=texto113.replace("7:00p","19:00")
    texto115=texto114.replace("7:10p","19:10")
    texto116=texto115.replace("7:20p","19:20")
    texto117=texto116.replace("7:30p","19:30")
    texto118=texto117.replace("7:40p","19:40")
    texto119=texto118.replace("7:50p","19:50")
    texto120=texto119.replace("8:00p","20:00")
    texto121=texto120.replace("8:10p","20:10")
    texto122=texto121.replace("8:20p","20:20")
    texto123=texto122.replace("8:30p","20:30")
    texto124=texto123.replace("8:40p","20:40")
    texto125=texto124.replace("8:50p","20:50")
    texto126=texto125.replace("9:00p","21:00")
    texto127=texto126.replace("9:10p","21:10")
    texto128=texto127.replace("9:20p","21:20")
    texto129=texto128.replace("9:30p","21:30")
    texto130=texto129.replace("9:40p","21:40")
    texto131=texto130.replace("9:50p","21:50")
    texto132=texto131.replace("10:00p","22:00")
    texto133=texto132.replace("10:10p","22:10")
    texto134=texto133.replace("10:20p","22:20")
    texto135=texto134.replace("10:30p","22:30")
    texto136=texto135.replace("10:40p","22:40")
    texto137=texto136.replace("10:50p","22:50")
    texto138=texto137.replace("11:00p","23:00")
    texto139=texto138.replace("11:10p","23:10")
    texto140=texto139.replace("11:20p","23:20")
    texto141=texto140.replace("11:30p","23:30")
    texto142=texto141.replace("11:40p","23:40")
    texto143=texto142.replace("11:50p","23:50")
    texto144=texto143.replace("113:00","23:00")
    texto145=texto144.replace("113:10","23:10")
    texto146=texto145.replace("113:20","23:20")
    texto147=texto146.replace("113:30","23:30")
    texto148=texto147.replace("113:40","23:40")
    texto149=texto148.replace("113:50","23:50")
    cchs1=open(dirtxtcchs,"w")
    cchs1.write(texto149)
    cchs1.close()
    cchs.close()

    cchs=open(dirtxtcchs)
    texto0=cchs.read()
    texto1=texto0.replace(",,",",")
    texto2=texto1.replace(",Date",",Fecha")
    cchs1=open(dircsvcchs,"w")
    cchs1.write(texto2)
    #print(texto2)
    cchs1.close()
    cchs.close()

    cchs=pd.read_csv(dircsvcchs, usecols=(1,2,3,6,7,8,10,11,17,18,23), index_col=0, header=0)
    #print(cchs)
    cchs.to_csv(dircsvcchs)


    cchs=open(dircsvcchs)
    nombrescol=cchs.read()
    texto1=nombrescol.replace("Out","temperatura")
    texto2=texto1.replace("Hum","humedadRelativa")
    texto3=texto2.replace("Pt.","puntoRocio")
    texto4=texto3.replace("Speed.1","velocidadRacha")
    texto5=texto4.replace("Dir.1","direccionRacha")
    texto6=texto5.replace("Speed","velocidadViento")
    texto7=texto6.replace("Dir","direccionViento")
    texto8=texto7.replace("Bar","presionBar")
    texto9=texto8.replace("Rain","lluvia")
    texto10=texto9.replace("Index.3","UV")

    cchs1=open(dircsvcchs,"w")
    cchs1.write(texto10)
    cchs1.close()
    cchs.close()

    cchs=open(dircsvcchs)
    texto=cchs.read()
    texto1=texto.replace("NNE","22.5")
    texto2=texto1.replace("ENE","67.5")
    texto3=texto2.replace("ESE","112.5")
    texto4=texto3.replace("SSE","157.5")
    texto5=texto4.replace("SSW","202.5")
    texto6=texto5.replace("WSW","247.5")
    texto7=texto6.replace("WNW","292.5")
    texto8=texto7.replace("NNW","337.5")
    texto9=texto8.replace("NE","45")
    texto10=texto9.replace("SE","135")
    texto11=texto10.replace("SW","225")
    texto12=texto11.replace("NW","315")
    cchs1=open(dircsvcchs,"w")
    cchs1.write(texto12)
    cchs1.close()
    cchs.close()

    cchs=open(dircsvcchs)
    texto=cchs.read()
    texto1=texto.replace("N","360")
    texto2=texto1.replace("E","90")
    texto3=texto2.replace("S","180")
    texto4=texto3.replace("W","270")
    cchs1=open(dircsvcchs,"w")
    cchs1.write(texto4)
    cchs1.close()
    cchs.close()

    cchs=pd.read_csv(dircsvcchs, index_col=0, header=0)
    #print(cchs)
    cchs['fechaHora']=cchs['Fecha'].map(str)  + ' ' + cchs['Time'].map(str)
    cchs
    #print(cchs)
    cchs.to_csv(dircsvcchs)


    DF=pd.read_csv(dircsvcchs, index_col=0)
    DF['idEstacion']=np.where(DF['Time'] !='[]', 'cchs', ' ', )
    #print(DF)
    DF.to_csv(dircsvcchs)

    cchs=pd.read_csv(dircsvcchs, usecols=(3,4,5,6,7,8,9,10,11,12,13), index_col=0, header=0)
    #print(cchs)
    cchs.to_csv(dircsvcchs)


    # try:
    #     cchs=pd.read_csv(dircsvcchs, index_col=0)
    #     filter= (cchs['fechaHora'] <= fecha_ayer1) & (cchs['fechaHora'] < fecha_hoy1)
    #     filtrado=cchs.loc[filter]
    #     #print(filtrado)
    #     filtrado.to_csv(dircsvcchs)
    #     print("Filtrado")
    # except:
    #     print("No se logro filtrar datos por fecha actual")


    print('Datos de la estación cchs listos')
except:
    print("No se logro obtener datos de la estación cchs")
    remove(dircsvcchs)

print('cchv')
try:
    print(espacio)
    file1 = dirtxtcchv
    r = urllib.request.urlopen(urlcchv)
    f = open(file1,'wb')
    f.write(r.read())
    f.close()
    #print(file1)
    print('Datos de la estación cchv obtenidos')

    try:
        with open(dirtxtcchv, 'r') as fr:
            # reading line by line
            lines = fr.readlines()

            # pointer for position
            ptr = 1

            # opening in writing mode
            with open(dirtxtcchv, 'w') as fw:
                for line in lines:

                    # we want to remove 5th line
                    if ptr != 1:
                        fw.write(line)
                    ptr += 1
        print("Deleted")

    except:
        print("Oops! No se pudo eliminar fila")

    try:
        with open(dirtxtcchv, 'r') as fr:
            # reading line by line
            lines = fr.readlines()

            # pointer for position
            ptr = 1

            # opening in writing mode
            with open(dirtxtcchv, 'w') as fw:
                for line in lines:

                    # we want to remove 5th line
                    if ptr != 2:
                        fw.write(line)
                    ptr += 1
        print("Deleted")

    except:
        print("Oops! No se pudo eliminar fila")


    cchv=open(dirtxtcchv)
    texto0=cchv.read()
    texto1=texto0.replace(" ",",")
    texto2=texto1.replace("---","9999")
    texto3=texto2.replace(",,",",")
    texto4=texto3.replace(",,,",",")
    texto5=texto4.replace(",,,,",",")
    texto6=texto5.replace(fecha_ayer0,fecha_ayerc)
    texto7=texto6.replace(fecha_hoy0,fecha_hoyc)
    #print(texto7)
    cchv1=open(dirtxtcchv,"w")
    cchv1.write(texto7)
    cchv1.close()

    cchv=open(dirtxtcchv)
    texto=cchv.read()
    texto0=texto.replace("12:00a","00:00")
    texto1=texto0.replace("12:10a","00:10")
    texto2=texto1.replace("12:20a","00:20")
    texto3=texto2.replace("12:30a","00:30")
    texto4=texto3.replace("12:40a","00:40")
    texto5=texto4.replace("12:50a","00:50")
    texto6=texto5.replace("1:00a","1:00")
    texto7=texto6.replace("1:10a","1:10")
    texto8=texto7.replace("1:20a","1:20")
    texto9=texto8.replace("1:30a","1:30")
    texto10=texto9.replace("1:40a","1:40")
    texto11=texto10.replace("1:50a","1:50")
    texto12=texto11.replace("2:00a","2:00")
    texto13=texto12.replace("2:10a","2:10")
    texto14=texto13.replace("2:20a","2:20")
    texto15=texto14.replace("2:30a","2:30")
    texto16=texto15.replace("2:40a","2:40")
    texto17=texto16.replace("2:50a","2:50")
    texto18=texto17.replace("3:00a","3:00")
    texto19=texto18.replace("3:10a","3:10")
    texto20=texto19.replace("3:20a","3:20")
    texto21=texto20.replace("3:30a","3:30")
    texto22=texto21.replace("3:40a","3:40")
    texto23=texto22.replace("3:50a","3:50")
    texto24=texto23.replace("4:00a","4:00")
    texto25=texto24.replace("4:10a","4:10")
    texto26=texto25.replace("4:20a","4:20")
    texto27=texto26.replace("4:30a","4:30")
    texto28=texto27.replace("4:40a","4:40")
    texto29=texto28.replace("4:50a","4:50")
    texto30=texto29.replace("5:00a","5:00")
    texto31=texto30.replace("5:10a","5:10")
    texto32=texto31.replace("5:20a","5:20")
    texto33=texto32.replace("5:30a","5:30")
    texto34=texto33.replace("5:40a","5:40")
    texto35=texto34.replace("5:50a","5:50")
    texto36=texto35.replace("6:00a","6:00")
    texto37=texto36.replace("6:10a","6:10")
    texto38=texto37.replace("6:20a","6:20")
    texto39=texto38.replace("6:30a","6:30")
    texto40=texto39.replace("6:40a","6:40")
    texto41=texto40.replace("6:50a","6:50")
    texto42=texto41.replace("7:00a","7:00")
    texto43=texto42.replace("7:10a","7:10")
    texto44=texto43.replace("7:20a","7:20")
    texto45=texto44.replace("7:30a","7:30")
    texto46=texto45.replace("7:40a","7:40")
    texto47=texto46.replace("7:50a","7:50")
    texto48=texto47.replace("8:00a","8:00")
    texto49=texto48.replace("8:10a","8:10")
    texto50=texto49.replace("8:20a","8:20")
    texto51=texto50.replace("8:30a","8:30")
    texto52=texto51.replace("8:40a","8:40")
    texto53=texto52.replace("8:50a","8:50")
    texto54=texto53.replace("9:00a","9:00")
    texto55=texto54.replace("9:10a","9:10")
    texto56=texto55.replace("9:20a","9:20")
    texto57=texto56.replace("9:30a","9:30")
    texto58=texto57.replace("9:40a","9:40")
    texto59=texto58.replace("9:50a","9:50")
    texto60=texto59.replace("10:00a","10:00")
    texto61=texto60.replace("10:10a","10:10")
    texto62=texto61.replace("10:20a","10:20")
    texto63=texto62.replace("10:30a","10:30")
    texto64=texto63.replace("10:40a","10:40")
    texto65=texto64.replace("10:50a","10:50")
    texto66=texto65.replace("11:00a","11:00")
    texto67=texto66.replace("11:10a","11:10")
    texto68=texto67.replace("11:20a","11:20")
    texto69=texto68.replace("11:30a","11:30")
    texto70=texto69.replace("11:40a","11:40")
    texto71=texto70.replace("11:50a","11:50")
    texto72=texto71.replace("12:00p","12:00")
    texto73=texto72.replace("12:10p","12:10")
    texto74=texto73.replace("12:20p","12:20")
    texto75=texto74.replace("12:30p","12:30")
    texto76=texto75.replace("12:40p","12:40")
    texto77=texto76.replace("12:50p","12:50")
    texto78=texto77.replace("1:00p","13:00")
    texto79=texto78.replace("1:10p","13:10")
    texto80=texto79.replace("1:20p","13:20")
    texto81=texto80.replace("1:30p","13:30")
    texto82=texto81.replace("1:40p","13:40")
    texto83=texto82.replace("1:50p","13:50")
    texto84=texto83.replace("2:00p","14:00")
    texto85=texto84.replace("2:10p","14:10")
    texto86=texto85.replace("2:20p","14:20")
    texto87=texto86.replace("2:30p","14:30")
    texto88=texto87.replace("2:40p","14:40")
    texto89=texto88.replace("2:50p","14:50")
    texto90=texto89.replace("3:00p","15:00")
    texto91=texto90.replace("3:10p","15:10")
    texto92=texto91.replace("3:20p","15:20")
    texto93=texto92.replace("3:30p","15:30")
    texto94=texto93.replace("3:40p","15:40")
    texto95=texto94.replace("3:50p","15:50")
    texto96=texto95.replace("4:00p","16:00")
    texto97=texto96.replace("4:10p","16:10")
    texto98=texto97.replace("4:20p","16:20")
    texto99=texto98.replace("4:30p","16:30")
    texto100=texto99.replace("4:40p","16:40")
    texto11=texto100.replace("4:50p","16:50")
    texto12=texto11.replace("5:00p","17:00")
    texto13=texto12.replace("5:10p","17:10")
    texto14=texto13.replace("5:20p","17:20")
    texto15=texto14.replace("5:30p","17:30")
    texto16=texto15.replace("5:40p","17:40")
    texto17=texto16.replace("5:50p","17:50")
    texto18=texto17.replace("6:00p","18:00")
    texto19=texto18.replace("6:10p","18:10")
    texto110=texto19.replace("6:20p","18:20")
    texto111=texto110.replace("6:30p","18:30")
    texto112=texto111.replace("6:40p","18:40")
    texto113=texto112.replace("6:50p","18:50")
    texto114=texto113.replace("7:00p","19:00")
    texto115=texto114.replace("7:10p","19:10")
    texto116=texto115.replace("7:20p","19:20")
    texto117=texto116.replace("7:30p","19:30")
    texto118=texto117.replace("7:40p","19:40")
    texto119=texto118.replace("7:50p","19:50")
    texto120=texto119.replace("8:00p","20:00")
    texto121=texto120.replace("8:10p","20:10")
    texto122=texto121.replace("8:20p","20:20")
    texto123=texto122.replace("8:30p","20:30")
    texto124=texto123.replace("8:40p","20:40")
    texto125=texto124.replace("8:50p","20:50")
    texto126=texto125.replace("9:00p","21:00")
    texto127=texto126.replace("9:10p","21:10")
    texto128=texto127.replace("9:20p","21:20")
    texto129=texto128.replace("9:30p","21:30")
    texto130=texto129.replace("9:40p","21:40")
    texto131=texto130.replace("9:50p","21:50")
    texto132=texto131.replace("10:00p","22:00")
    texto133=texto132.replace("10:10p","22:10")
    texto134=texto133.replace("10:20p","22:20")
    texto135=texto134.replace("10:30p","22:30")
    texto136=texto135.replace("10:40p","22:40")
    texto137=texto136.replace("10:50p","22:50")
    texto138=texto137.replace("11:00p","23:00")
    texto139=texto138.replace("11:10p","23:10")
    texto140=texto139.replace("11:20p","23:20")
    texto141=texto140.replace("11:30p","23:30")
    texto142=texto141.replace("11:40p","23:40")
    texto143=texto142.replace("11:50p","23:50")
    texto144=texto143.replace("113:00","23:00")
    texto145=texto144.replace("113:10","23:10")
    texto146=texto145.replace("113:20","23:20")
    texto147=texto146.replace("113:30","23:30")
    texto148=texto147.replace("113:40","23:40")
    texto149=texto148.replace("113:50","23:50")
    cchv1=open(dirtxtcchv,"w")
    cchv1.write(texto149)
    cchv1.close()
    cchv.close()

    cchv=open(dirtxtcchv)
    texto0=cchv.read()
    texto1=texto0.replace(",,",",")
    texto2=texto1.replace(",Date",",Fecha")
    cchv1=open(dircsvcchv,"w")
    cchv1.write(texto2)
    #print(texto2)
    cchv1.close()
    cchv.close()

    cchv=pd.read_csv(dircsvcchv, usecols=(1,2,3,6,7,8,10,11,17,18,23), index_col=0, header=0)
    #print(cchv)
    cchv.to_csv(dircsvcchv)


    cchv=open(dircsvcchv)
    nombrescol=cchv.read()
    texto1=nombrescol.replace("Out","temperatura")
    texto2=texto1.replace("Hum","humedadRelativa")
    texto3=texto2.replace("Pt.","puntoRocio")
    texto4=texto3.replace("Speed.1","velocidadRacha")
    texto5=texto4.replace("Dir.1","direccionRacha")
    texto6=texto5.replace("Speed","velocidadViento")
    texto7=texto6.replace("Dir","direccionViento")
    texto8=texto7.replace("Bar","presionBar")
    texto9=texto8.replace("Rain","lluvia")
    texto10=texto9.replace("Index.3","UV")

    cchv1=open(dircsvcchv,"w")
    cchv1.write(texto10)
    cchv1.close()
    cchv.close()

    cchv=open(dircsvcchv)
    texto=cchv.read()
    texto1=texto.replace("NNE","22.5")
    texto2=texto1.replace("ENE","67.5")
    texto3=texto2.replace("ESE","112.5")
    texto4=texto3.replace("SSE","157.5")
    texto5=texto4.replace("SSW","202.5")
    texto6=texto5.replace("WSW","247.5")
    texto7=texto6.replace("WNW","292.5")
    texto8=texto7.replace("NNW","337.5")
    texto9=texto8.replace("NE","45")
    texto10=texto9.replace("SE","135")
    texto11=texto10.replace("SW","225")
    texto12=texto11.replace("NW","315")
    cchv1=open(dircsvcchv,"w")
    cchv1.write(texto12)
    cchv1.close()
    cchv.close()

    cchv=open(dircsvcchv)
    texto=cchv.read()
    texto1=texto.replace("N","360")
    texto2=texto1.replace("E","90")
    texto3=texto2.replace("S","180")
    texto4=texto3.replace("W","270")
    cchv1=open(dircsvcchv,"w")
    cchv1.write(texto4)
    cchv1.close()
    cchv.close()

    cchv=pd.read_csv(dircsvcchv, index_col=0, header=0)
    #print(cchv)
    cchv['fechaHora']=cchv['Fecha'].map(str)  + ' ' + cchv['Time'].map(str)
    cchv
    #print(cchv)
    cchv.to_csv(dircsvcchv)


    DF=pd.read_csv(dircsvcchv, index_col=0)
    DF['idEstacion']=np.where(DF['Time'] !='[]', 'cchv', ' ', )
    #print(DF)
    DF.to_csv(dircsvcchv)

    cchv=pd.read_csv(dircsvcchv, usecols=(3,4,5,6,7,8,9,10,11,12,13), index_col=0, header=0)
    #print(cchv)
    cchv.to_csv(dircsvcchv)


    # try:
    #     cchv=pd.read_csv(dircsvcchv, index_col=0)
    #     filter= (cchv['fechaHora'] <= fecha_ayer1) & (cchv['fechaHora'] < fecha_hoy1)
    #     filtrado=cchv.loc[filter]
    #     #print(filtrado)
    #     filtrado.to_csv(dircsvcchv)
    #     print("Filtrado")
    # except:
    #     print("No se logro filtrar datos por fecha actual")


    print('Datos de la estación cchv listos')
except:
    print("No se logro obtener datos de la estación cchv")
    remove(dircsvcchv)

print('ICAyCC')
try:
    print(espacio)
    file1 = dirtxtICAyCC
    r = urllib.request.urlopen(urlICAyCC)
    f = open(file1,'wb')
    f.write(r.read())
    f.close()
    #print(file1)
    print('Datos de la estación ICAyCC obtenidos')

    try:
        with open(dirtxtICAyCC, 'r') as fr:
            # reading line by line
            lines = fr.readlines()

            # pointer for position
            ptr = 1

            # opening in writing mode
            with open(dirtxtICAyCC, 'w') as fw:
                for line in lines:

                    # we want to remove 5th line
                    if ptr != 1:
                        fw.write(line)
                    ptr += 1
        print("Deleted")

    except:
        print("Oops! No se pudo eliminar fila")

    try:
        with open(dirtxtICAyCC, 'r') as fr:
            # reading line by line
            lines = fr.readlines()

            # pointer for position
            ptr = 1

            # opening in writing mode
            with open(dirtxtICAyCC, 'w') as fw:
                for line in lines:

                    # we want to remove 5th line
                    if ptr != 2:
                        fw.write(line)
                    ptr += 1
        print("Deleted")

    except:
        print("Oops! No se pudo eliminar fila")


    ICAyCC=open(dirtxtICAyCC)
    texto0=ICAyCC.read()
    texto1=texto0.replace(" ",",")
    texto2=texto1.replace("---","9999")
    texto3=texto2.replace(",,",",")
    texto4=texto3.replace(",,,",",")
    texto5=texto4.replace(",,,,",",")
    texto6=texto5.replace(fecha_ayer0,fecha_ayerc)
    texto7=texto6.replace(fecha_hoy0,fecha_hoyc)
    #print(texto7)
    ICAyCC1=open(dirtxtICAyCC,"w")
    ICAyCC1.write(texto7)
    ICAyCC1.close()

    ICAyCC=open(dirtxtICAyCC)
    texto=ICAyCC.read()
    texto0=texto.replace("12:00a","00:00")
    texto1=texto0.replace("12:10a","00:10")
    texto2=texto1.replace("12:20a","00:20")
    texto3=texto2.replace("12:30a","00:30")
    texto4=texto3.replace("12:40a","00:40")
    texto5=texto4.replace("12:50a","00:50")
    texto6=texto5.replace("1:00a","1:00")
    texto7=texto6.replace("1:10a","1:10")
    texto8=texto7.replace("1:20a","1:20")
    texto9=texto8.replace("1:30a","1:30")
    texto10=texto9.replace("1:40a","1:40")
    texto11=texto10.replace("1:50a","1:50")
    texto12=texto11.replace("2:00a","2:00")
    texto13=texto12.replace("2:10a","2:10")
    texto14=texto13.replace("2:20a","2:20")
    texto15=texto14.replace("2:30a","2:30")
    texto16=texto15.replace("2:40a","2:40")
    texto17=texto16.replace("2:50a","2:50")
    texto18=texto17.replace("3:00a","3:00")
    texto19=texto18.replace("3:10a","3:10")
    texto20=texto19.replace("3:20a","3:20")
    texto21=texto20.replace("3:30a","3:30")
    texto22=texto21.replace("3:40a","3:40")
    texto23=texto22.replace("3:50a","3:50")
    texto24=texto23.replace("4:00a","4:00")
    texto25=texto24.replace("4:10a","4:10")
    texto26=texto25.replace("4:20a","4:20")
    texto27=texto26.replace("4:30a","4:30")
    texto28=texto27.replace("4:40a","4:40")
    texto29=texto28.replace("4:50a","4:50")
    texto30=texto29.replace("5:00a","5:00")
    texto31=texto30.replace("5:10a","5:10")
    texto32=texto31.replace("5:20a","5:20")
    texto33=texto32.replace("5:30a","5:30")
    texto34=texto33.replace("5:40a","5:40")
    texto35=texto34.replace("5:50a","5:50")
    texto36=texto35.replace("6:00a","6:00")
    texto37=texto36.replace("6:10a","6:10")
    texto38=texto37.replace("6:20a","6:20")
    texto39=texto38.replace("6:30a","6:30")
    texto40=texto39.replace("6:40a","6:40")
    texto41=texto40.replace("6:50a","6:50")
    texto42=texto41.replace("7:00a","7:00")
    texto43=texto42.replace("7:10a","7:10")
    texto44=texto43.replace("7:20a","7:20")
    texto45=texto44.replace("7:30a","7:30")
    texto46=texto45.replace("7:40a","7:40")
    texto47=texto46.replace("7:50a","7:50")
    texto48=texto47.replace("8:00a","8:00")
    texto49=texto48.replace("8:10a","8:10")
    texto50=texto49.replace("8:20a","8:20")
    texto51=texto50.replace("8:30a","8:30")
    texto52=texto51.replace("8:40a","8:40")
    texto53=texto52.replace("8:50a","8:50")
    texto54=texto53.replace("9:00a","9:00")
    texto55=texto54.replace("9:10a","9:10")
    texto56=texto55.replace("9:20a","9:20")
    texto57=texto56.replace("9:30a","9:30")
    texto58=texto57.replace("9:40a","9:40")
    texto59=texto58.replace("9:50a","9:50")
    texto60=texto59.replace("10:00a","10:00")
    texto61=texto60.replace("10:10a","10:10")
    texto62=texto61.replace("10:20a","10:20")
    texto63=texto62.replace("10:30a","10:30")
    texto64=texto63.replace("10:40a","10:40")
    texto65=texto64.replace("10:50a","10:50")
    texto66=texto65.replace("11:00a","11:00")
    texto67=texto66.replace("11:10a","11:10")
    texto68=texto67.replace("11:20a","11:20")
    texto69=texto68.replace("11:30a","11:30")
    texto70=texto69.replace("11:40a","11:40")
    texto71=texto70.replace("11:50a","11:50")
    texto72=texto71.replace("12:00p","12:00")
    texto73=texto72.replace("12:10p","12:10")
    texto74=texto73.replace("12:20p","12:20")
    texto75=texto74.replace("12:30p","12:30")
    texto76=texto75.replace("12:40p","12:40")
    texto77=texto76.replace("12:50p","12:50")
    texto78=texto77.replace("1:00p","13:00")
    texto79=texto78.replace("1:10p","13:10")
    texto80=texto79.replace("1:20p","13:20")
    texto81=texto80.replace("1:30p","13:30")
    texto82=texto81.replace("1:40p","13:40")
    texto83=texto82.replace("1:50p","13:50")
    texto84=texto83.replace("2:00p","14:00")
    texto85=texto84.replace("2:10p","14:10")
    texto86=texto85.replace("2:20p","14:20")
    texto87=texto86.replace("2:30p","14:30")
    texto88=texto87.replace("2:40p","14:40")
    texto89=texto88.replace("2:50p","14:50")
    texto90=texto89.replace("3:00p","15:00")
    texto91=texto90.replace("3:10p","15:10")
    texto92=texto91.replace("3:20p","15:20")
    texto93=texto92.replace("3:30p","15:30")
    texto94=texto93.replace("3:40p","15:40")
    texto95=texto94.replace("3:50p","15:50")
    texto96=texto95.replace("4:00p","16:00")
    texto97=texto96.replace("4:10p","16:10")
    texto98=texto97.replace("4:20p","16:20")
    texto99=texto98.replace("4:30p","16:30")
    texto100=texto99.replace("4:40p","16:40")
    texto11=texto100.replace("4:50p","16:50")
    texto12=texto11.replace("5:00p","17:00")
    texto13=texto12.replace("5:10p","17:10")
    texto14=texto13.replace("5:20p","17:20")
    texto15=texto14.replace("5:30p","17:30")
    texto16=texto15.replace("5:40p","17:40")
    texto17=texto16.replace("5:50p","17:50")
    texto18=texto17.replace("6:00p","18:00")
    texto19=texto18.replace("6:10p","18:10")
    texto110=texto19.replace("6:20p","18:20")
    texto111=texto110.replace("6:30p","18:30")
    texto112=texto111.replace("6:40p","18:40")
    texto113=texto112.replace("6:50p","18:50")
    texto114=texto113.replace("7:00p","19:00")
    texto115=texto114.replace("7:10p","19:10")
    texto116=texto115.replace("7:20p","19:20")
    texto117=texto116.replace("7:30p","19:30")
    texto118=texto117.replace("7:40p","19:40")
    texto119=texto118.replace("7:50p","19:50")
    texto120=texto119.replace("8:00p","20:00")
    texto121=texto120.replace("8:10p","20:10")
    texto122=texto121.replace("8:20p","20:20")
    texto123=texto122.replace("8:30p","20:30")
    texto124=texto123.replace("8:40p","20:40")
    texto125=texto124.replace("8:50p","20:50")
    texto126=texto125.replace("9:00p","21:00")
    texto127=texto126.replace("9:10p","21:10")
    texto128=texto127.replace("9:20p","21:20")
    texto129=texto128.replace("9:30p","21:30")
    texto130=texto129.replace("9:40p","21:40")
    texto131=texto130.replace("9:50p","21:50")
    texto132=texto131.replace("10:00p","22:00")
    texto133=texto132.replace("10:10p","22:10")
    texto134=texto133.replace("10:20p","22:20")
    texto135=texto134.replace("10:30p","22:30")
    texto136=texto135.replace("10:40p","22:40")
    texto137=texto136.replace("10:50p","22:50")
    texto138=texto137.replace("11:00p","23:00")
    texto139=texto138.replace("11:10p","23:10")
    texto140=texto139.replace("11:20p","23:20")
    texto141=texto140.replace("11:30p","23:30")
    texto142=texto141.replace("11:40p","23:40")
    texto143=texto142.replace("11:50p","23:50")
    texto144=texto143.replace("113:00","23:00")
    texto145=texto144.replace("113:10","23:10")
    texto146=texto145.replace("113:20","23:20")
    texto147=texto146.replace("113:30","23:30")
    texto148=texto147.replace("113:40","23:40")
    texto149=texto148.replace("113:50","23:50")
    ICAyCC1=open(dirtxtICAyCC,"w")
    ICAyCC1.write(texto149)
    ICAyCC1.close()
    ICAyCC.close()

    ICAyCC=open(dirtxtICAyCC)
    texto0=ICAyCC.read()
    texto1=texto0.replace(",,",",")
    texto2=texto1.replace(",Date",",Fecha")
    ICAyCC1=open(dircsvICAyCC,"w")
    ICAyCC1.write(texto2)
    #print(texto2)
    ICAyCC1.close()
    ICAyCC.close()

    ICAyCC=pd.read_csv(dircsvICAyCC, usecols=(1,2,3,6,7,8,10,11,17,18,23), index_col=0, header=0)
    #print(ICAyCC)
    ICAyCC.to_csv(dircsvICAyCC)


    ICAyCC=open(dircsvICAyCC)
    nombrescol=ICAyCC.read()
    texto1=nombrescol.replace("Out","temperatura")
    texto2=texto1.replace("Hum","humedadRelativa")
    texto3=texto2.replace("Pt.","puntoRocio")
    texto4=texto3.replace("Speed.1","velocidadRacha")
    texto5=texto4.replace("Dir.1","direccionRacha")
    texto6=texto5.replace("Speed","velocidadViento")
    texto7=texto6.replace("Dir","direccionViento")
    texto8=texto7.replace("Bar","presionBar")
    texto9=texto8.replace("Rain","lluvia")
    texto10=texto9.replace("Index.3","UV")

    ICAyCC1=open(dircsvICAyCC,"w")
    ICAyCC1.write(texto10)
    ICAyCC1.close()
    ICAyCC.close()

    ICAyCC=open(dircsvICAyCC)
    texto=ICAyCC.read()
    texto1=texto.replace("NNE","22.5")
    texto2=texto1.replace("ENE","67.5")
    texto3=texto2.replace("ESE","112.5")
    texto4=texto3.replace("SSE","157.5")
    texto5=texto4.replace("SSW","202.5")
    texto6=texto5.replace("WSW","247.5")
    texto7=texto6.replace("WNW","292.5")
    texto8=texto7.replace("NNW","337.5")
    texto9=texto8.replace("NE","45")
    texto10=texto9.replace("SE","135")
    texto11=texto10.replace("SW","225")
    texto12=texto11.replace("NW","315")
    ICAyCC1=open(dircsvICAyCC,"w")
    ICAyCC1.write(texto12)
    ICAyCC1.close()
    ICAyCC.close()

    ICAyCC=open(dircsvICAyCC)
    texto=ICAyCC.read()
    texto1=texto.replace("N","360")
    texto2=texto1.replace("E","90")
    texto3=texto2.replace("S","180")
    texto4=texto3.replace("W","270")
    ICAyCC1=open(dircsvICAyCC,"w")
    ICAyCC1.write(texto4)
    ICAyCC1.close()
    ICAyCC.close()

    ICAyCC=pd.read_csv(dircsvICAyCC, index_col=0, header=0)
    #print(ICAyCC)
    ICAyCC['fechaHora']=ICAyCC['Fecha'].map(str)  + ' ' + ICAyCC['Time'].map(str)
    ICAyCC
    #print(ICAyCC)
    ICAyCC.to_csv(dircsvICAyCC)


    DF=pd.read_csv(dircsvICAyCC, index_col=0)
    DF['idEstacion']=np.where(DF['Time'] !='[]', 'ICAyCC', ' ', )
    #print(DF)
    DF.to_csv(dircsvICAyCC)

    ICAyCC=pd.read_csv(dircsvICAyCC, usecols=(3,4,5,6,7,8,9,10,11,12,13), index_col=0, header=0)
    #print(ICAyCC)
    ICAyCC.to_csv(dircsvICAyCC)


    # try:
    #     ICAyCC=pd.read_csv(dircsvICAyCC, index_col=0)
    #     filter= (ICAyCC['fechaHora'] <= fecha_ayer1) & (ICAyCC['fechaHora'] < fecha_hoy1)
    #     filtrado=ICAyCC.loc[filter]
    #     #print(filtrado)
    #     filtrado.to_csv(dircsvICAyCC)
    #     print("Filtrado")
    # except:
    #     print("No se logro filtrar datos por fecha actual")


    print('Datos de la estación ICAyCC listos')
except:
    print("No se logro obtener datos de la estación ICAyCC")
    remove(dircsvICAyCC)



dirtxtenp1=r'C:\Users\videowall_03\Downloads\enp1.txt'
dircsvenp1=r'C:\\Apache24\\htdocs\\estacionesMet\\files\\enp1.csv'
urlenp1 = 'https://www.ruoa.unam.mx/pembu/datos/enp1/downld02.txt'

dirtxtenp2=r'C:\Users\videowall_03\Downloads\enp2.txt'
dircsvenp2=r'C:\\Apache24\\htdocs\\estacionesMet\\files\\enp2.csv'
urlenp2 = 'https://www.ruoa.unam.mx/pembu/datos/enp2/downld02.txt'

dirtxtenp3=r'C:\Users\videowall_03\Downloads\enp3.txt'
dircsvenp3=r'C:\\Apache24\\htdocs\\estacionesMet\\files\\enp3.csv'
urlenp3 = 'https://www.ruoa.unam.mx/pembu/datos/enp3/downld02.txt'

dirtxtenp4=r'C:\Users\videowall_03\Downloads\enp4.txt'
dircsvenp4=r'C:\\Apache24\\htdocs\\estacionesMet\\files\\enp4.csv'
urlenp4 = 'https://www.ruoa.unam.mx/pembu/datos/enp4/downld02.txt'

dirtxtenp4=r'C:\Users\videowall_03\Downloads\enp4.txt'
dircsvenp4=r'C:\\Apache24\\htdocs\\estacionesMet\\files\\enp4.csv'
urlenp4 = 'https://www.ruoa.unam.mx/pembu/datos/enp4/downld02.txt'

dirtxtenp5=r'C:\Users\videowall_03\Downloads\enp5.txt'
dircsvenp5=r'C:\\Apache24\\htdocs\\estacionesMet\\files\\enp5.csv'
urlenp5 = 'https://www.ruoa.unam.mx/pembu/datos/enp5/downld02.txt'

dirtxtenp6=r'C:\Users\videowall_03\Downloads\enp6.txt'
dircsvenp6=r'C:\\Apache24\\htdocs\\estacionesMet\\files\\enp6.csv'
urlenp6 = 'https://www.ruoa.unam.mx/pembu/datos/enp6/downld02.txt'

dirtxtenp7=r'C:\Users\videowall_03\Downloads\enp7.txt'
dircsvenp7=r'C:\\Apache24\\htdocs\\estacionesMet\\files\\enp7.csv'
urlenp7 = 'https://www.ruoa.unam.mx/pembu/datos/enp7/downld02.txt'

dirtxtenp8=r'C:\Users\videowall_03\Downloads\enp8.txt'
dircsvenp8=r'C:\\Apache24\\htdocs\\estacionesMet\\files\\enp8.csv'
urlenp8 = 'https://www.ruoa.unam.mx/pembu/datos/enp8/downld02.txt'

dirtxtenp9=r'C:\Users\videowall_03\Downloads\enp9.txt'
dircsvenp9=r'C:\\Apache24\\htdocs\\estacionesMet\\files\\enp9.csv'
urlenp9 = 'https://www.ruoa.unam.mx/pembu/datos/enp9/downld02.txt'

dirtxtccha=r'C:\Users\videowall_03\Downloads\ccha.txt'
dircsvccha=r'C:\\Apache24\\htdocs\\estacionesMet\\files\\ccha.csv'
urlccha = 'https://www.ruoa.unam.mx/pembu/datos/ccha/downld02.txt'


dirtxtcchn=r'C:\Users\videowall_03\Downloads\cchn.txt'
dircsvcchn=r'C:\\Apache24\\htdocs\\estacionesMet\\files\\cchn.csv'
urlcchn = 'https://www.ruoa.unam.mx/pembu/datos/cchn/downld02.txt'

dirtxtccho=r'C:\Users\videowall_03\Downloads\ccho.txt'
dircsvccho=r'C:\\Apache24\\htdocs\\estacionesMet\\files\\ccho.csv'
urlccho = 'https://www.ruoa.unam.mx/pembu/datos/ccho/downld02.txt'

dirtxtcchs=r'C:\Users\videowall_03\Downloads\cchs.txt'
dircsvcchs=r'C:\\Apache24\\htdocs\\estacionesMet\\files\\cchs.csv'
urlcchs = 'https://www.ruoa.unam.mx/pembu/datos/cchs/downld02.txt'

dirtxtcchv=r'C:\Users\videowall_03\Downloads\cchv.txt'
dircsvcchv=r'C:\\Apache24\\htdocs\\estacionesMet\\files\\cchv.csv'
urlcchv = 'https://www.ruoa.unam.mx/pembu/datos/cchv/downld02.txt'

dirtxtICAyCC=r'C:\Users\videowall_03\Downloads\ICAyCC.txt'
dircsvICAyCC=r'C:\\Apache24\\htdocs\\estacionesMet\\files\\ICAyCC.csv'
urlICAyCC = 'https://www.ruoa.unam.mx/pembu/datos/ICAyCC/downld02.txt'
