#NO BORRAR LAS IMPORTACIONES QUE ENCUENTRAN A CONTINUACIÓN. LA FUNCIÓN QUE VA A 
#COMPLETAR NO REQUERIRÁ DE PARÁMETROS DE ENTRADA

#LOS MÓDULOS csv Y json ESTÁN ADJUNTOS POR DEFECTO EN LAS VERSIONES MÁS RECIENTES 
#DE PYTHON (3.x). ASEGÚRESE DE QUE LA VERSIÓN DE PYTHON EN LA QUE USTED HA ESTADO 
#EJECUTANDO SU PROPUESTA DE SOLUCIÓN CONTIENE DICHO MÓDULO
import pandas as pd
import numpy as np
from csv import reader
import json

def comprar_promedios(datos,promedios_temp, promedios_pres):
    above_avg_temp = []
    above_avg_pres = []
    
    for a in datos['id']:
        #**************************************************************************************
        if ((datos['location'][a-1] ==1) and (promedios_temp[0] == datos['temperature'][a-1])):
            above_avg_temp.append('IGUAL')
        if ((datos['location'][a-1] ==1) and (promedios_temp[0] < datos['temperature'][a-1])):
            above_avg_temp.append('SI')
        if ((datos['location'][a-1] ==1) and (promedios_temp[0] > datos['temperature'][a-1])):
            above_avg_temp.append('NO')
        #**************************************************************************************
        if ((datos['location'][a-1] ==2) and (promedios_temp[1] == datos['temperature'][a-1])):
            above_avg_temp.append('IGUAL')
        if ((datos['location'][a-1] ==2) and (promedios_temp[1] < datos['temperature'][a-1])):
            above_avg_temp.append('SI')
        if ((datos['location'][a-1] ==2) and (promedios_temp[1] > datos['temperature'][a-1])):
            above_avg_temp.append('NO')
        #**************************************************************************************
        if ((datos['location'][a-1] ==3) and (promedios_temp[2] == datos['temperature'][a-1])):
            above_avg_temp.append('IGUAL')
        if ((datos['location'][a-1] ==3) and (promedios_temp[2] < datos['temperature'][a-1])):
            above_avg_temp.append('SI')
        if ((datos['location'][a-1] ==3) and (promedios_temp[2] > datos['temperature'][a-1])):
            above_avg_temp.append('NO')
        #**************************************************************************************
        if ((datos['location'][a-1] ==4) and (promedios_temp[3] == datos['temperature'][a-1])):
            above_avg_temp.append('IGUAL')
        if ((datos['location'][a-1] ==4) and (promedios_temp[3] < datos['temperature'][a-1])):
            above_avg_temp.append('SI')
        if ((datos['location'][a-1] ==4) and (promedios_temp[3] > datos['temperature'][a-1])):
            above_avg_temp.append('NO')
        #**************************************************************************************
        if ((datos['location'][a-1] ==5) and (promedios_temp[4] == datos['temperature'][a-1])):
            above_avg_temp.append('IGUAL')
        if ((datos['location'][a-1] ==5) and (promedios_temp[4] < datos['temperature'][a-1])):
            above_avg_temp.append('SI')
        if ((datos['location'][a-1] ==5) and (promedios_temp[4] > datos['temperature'][a-1])):
            above_avg_temp.append('NO')
        #**************************************************************************************
        if ((datos['location'][a-1] ==6) and (promedios_temp[5] == datos['temperature'][a-1])):
            above_avg_temp.append('IGUAL')
        if ((datos['location'][a-1] ==6) and (promedios_temp[5] < datos['temperature'][a-1])):
            above_avg_temp.append('SI')
        if ((datos['location'][a-1] ==6) and (promedios_temp[5] > datos['temperature'][a-1])):
            above_avg_temp.append('NO')
        #**************************************************************************************
        
        #**************************************************************************************
        if ((datos['location'][a-1] ==1) and (promedios_pres[0] == datos['pressure'][a-1])):
            above_avg_pres.append('IGUAL')
        if ((datos['location'][a-1] ==1) and (promedios_pres[0] < datos['pressure'][a-1])):
            above_avg_pres.append('SI')
        if ((datos['location'][a-1] ==1) and (promedios_pres[0] > datos['pressure'][a-1])):
            above_avg_pres.append('NO')
        #**************************************************************************************
        if ((datos['location'][a-1] ==2) and (promedios_pres[1] == datos['pressure'][a-1])):
            above_avg_pres.append('IGUAL')
        if ((datos['location'][a-1] ==2) and (promedios_pres[1] < datos['pressure'][a-1])):
            above_avg_pres.append('SI')
        if ((datos['location'][a-1] ==2) and (promedios_pres[1] > datos['pressure'][a-1])):
            above_avg_pres.append('NO')
        #**************************************************************************************
        if ((datos['location'][a-1] ==3) and (promedios_pres[2] == datos['pressure'][a-1])):
            above_avg_pres.append('IGUAL')
        if ((datos['location'][a-1] ==3) and (promedios_pres[2] < datos['pressure'][a-1])):
            above_avg_pres.append('SI')
        if ((datos['location'][a-1] ==3) and (promedios_pres[2] > datos['pressure'][a-1])):
            above_avg_pres.append('NO')
        #**************************************************************************************
        if ((datos['location'][a-1] ==4) and (promedios_pres[3] == datos['pressure'][a-1])):
            above_avg_pres.append('IGUAL')
        if ((datos['location'][a-1] ==4) and (promedios_pres[3] < datos['pressure'][a-1])):
            above_avg_pres.append('SI')
        if ((datos['location'][a-1] ==4) and (promedios_pres[3] > datos['pressure'][a-1])):
            above_avg_pres.append('NO')
        #**************************************************************************************
        if ((datos['location'][a-1] ==5) and (promedios_pres[4] == datos['pressure'][a-1])):
            above_avg_pres.append('IGUAL')
        if ((datos['location'][a-1] ==5) and (promedios_pres[4] < datos['pressure'][a-1])):
            above_avg_pres.append('SI')
        if ((datos['location'][a-1] ==5) and (promedios_pres[4] > datos['pressure'][a-1])):
            above_avg_pres.append('NO')
        #**************************************************************************************
        if ((datos['location'][a-1] ==6) and (promedios_pres[5] == datos['pressure'][a-1])):
            above_avg_pres.append('IGUAL')
        if ((datos['location'][a-1] ==6) and (promedios_pres[5] < datos['pressure'][a-1])):
            above_avg_pres.append('SI')
        if ((datos['location'][a-1] ==6) and (promedios_pres[5] > datos['pressure'][a-1])):
            above_avg_pres.append('NO')
        #**************************************************************************************
        
        
    return(above_avg_temp,above_avg_pres )

def clima():
    df = pd.read_csv("data.csv")
    above_avg_temp = []
    above_avg_pres = []
    location=[]
    temperature=[]
    pressure=[]
    idd=[]
    
    # Tarea #1 *****************************************************************************************
    promedios_temp=[0,0,0,0,0]
    promedios_pres=[0,0,0,0,0]
    df = pd.DataFrame()
    df = pd.read_csv('data.csv', sep=',', engine='python')
    for a in range(1,6):
        suma = df.query("location =="+ str(a))['temperature'].sum()
        cont = df.query("location =="+ str(a))['temperature'].count()
        promedios_temp[a-1]= suma / cont
    for b in range(1,6):
        suma = df.query("location =="+ str(b))['pressure'].sum()
        cont = df.query("location =="+ str(b))['pressure'].count()
        promedios_pres[b-1]= suma / cont
        
    for c in range(1,6):
        promedios_temp[c-1]= round(promedios_temp[c-1],1)
        promedios_pres[c-1]= round(promedios_pres[c-1],1)
    
    dict_datos = {
        '1':[promedios_temp[0],promedios_pres[0]],
        '2':[promedios_temp[1],promedios_pres[1]],
        '3':[promedios_temp[2],promedios_pres[2]],
        '4':[promedios_temp[3],promedios_pres[3]],
        '5':[promedios_temp[4],promedios_pres[4]]}
    data_json = json.dumps(dict_datos)
    archivo_json = open("data.json","w")
    archivo_json.write(data_json)
    archivo_json.close()
    
    #***************************************************************************************************
    # Tarea #2 *****************************************************************************************
    above_avg_temp,above_avg_pres = comprar_promedios(df, promedios_temp, promedios_pres)
    
    with open ('data.csv', 'r') as archivo:
        next(archivo, None)
        for linea in archivo:
            linea = linea.rstrip()
            lista = linea.split(",")
            idd.append(lista[0])
            location.append(lista[1])
            temperature.append(lista[2])
            pressure.append(lista[3])
            
    datos= pd.DataFrame({'id':idd,
                         'location':location,
                         'temperature':temperature,
                         'pressure': pressure,
                         'above_avg_temp':above_avg_temp,
                         'above_avg_pres':above_avg_pres})
    datos=datos.set_index('id')
    datos.to_csv("data_nuevo.csv" )
    return data_json

print(clima())