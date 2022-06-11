
def lectorlimpia(Archivo):
    from fileinput import close
    Weatherdata_ini=open(Archivo,"r")
    Weatherdata=Weatherdata_ini.read().split('\n')
    i=0
    for line in Weatherdata:
        Weatherdata[i]=line.split(",")
        
        i+=1
    Weatherdata_ini.close()
    return Weatherdata

def places(Weatherdata):
    i=0
    flag=0    
    places=list()
    for line in Weatherdata:
        if flag!=0:
            places.append(line[1])
            i+=1
        flag=1
    places=set([int(i) for i in places])
    return places


def aislamiento(num,Weatherdata):
    
    aislated=[]
    for line in Weatherdata:
        if line[1]==str(num):
            aislated.append(line)
    return(aislated)           

def promedio(Weather_place,indicator): #Weatherplace conjunto de datos sobre los que se va a trabjar, indicator es la columna del conjunto de datos a la que sacaremos promedio
    try :
        suma=0
        for line in Weather_place:
            suma=suma+float(line[indicator])
        promedio=round(suma/len(Weather_place),1)      
    except:
        promedio=0
    return(promedio)

        
def agregador_si_no(wheather_data,num):
    r=0
    for line in wheather_data:
            if line[1]==str(num) and float(line[2])> promedio(aislamiento(num,lectorlimpia("data.csv")),2):
                wheather_data[r].append("SI")
            elif line[1]==str(num) and float(line[2])< promedio(aislamiento(num,lectorlimpia("data.csv")),2):
                wheather_data[r].append("NO")
            elif line[1]==str(num) and float(line[2])== promedio(aislamiento(num,lectorlimpia("data.csv")),2):
                wheather_data[r].append("IGUAL")
            r+=1
    return wheather_data

def agregador_si_no_2(wheather_data,num):
    r=0
    for line in wheather_data:
            if line[1]==str(num) and float(line[3])> promedio(aislamiento(num,lectorlimpia("data.csv")),3):
                wheather_data[r].append("SI")
            elif line[1]==str(num) and float(line[3])< promedio(aislamiento(num,lectorlimpia("data.csv")),3):
                wheather_data[r].append("NO")
            elif line[1]==str(num) and float(line[3])== promedio(aislamiento(num,lectorlimpia("data.csv")),3):
                wheather_data[r].append("IGUAL")
            r+=1
    return wheather_data


########################MAIN FUNCTION###############################################################
def clima():
    import json as js
    import csv
    
    obje_js={}#creo un diccionario vacio para luego convertir en Json
    locations=list(places(lectorlimpia("data.csv")))#obtengo la lista de los lugares sobre los que voy a determinar la locación 
    wheather_data=lectorlimpia("data.csv")
    i=0
    for every_place in locations:
        obje_js[str(every_place)]=[promedio(aislamiento((locations[i]),lectorlimpia("data.csv")),2),promedio(aislamiento((locations[i]),lectorlimpia("data.csv")),3)]
                                    #promedio de la comuna 2 en el conjunto de datos aislados para el lugar locations[i], del archivo procesado en lectorlimpia.
        i+=1   
    for i in locations:
        wheather_data=agregador_si_no(wheather_data,i)
    for i in locations:
        wheather_data=agregador_si_no_2(wheather_data,i)
    
    wheather_data[0].append("above_avg_temp")
    wheather_data[0].append("above_avg_pres")
    i=0
    for line in wheather_data:
        wheather_data[i]=",".join(line)
        
        i+=1
    

    with open("data_nuevo.csv","w", newline='') :
       csv.writer(open("data_nuevo.csv","w"), delimiter='\n').writerow(wheather_data)
        
    
    datos=js.dumps(obje_js)
    archivo_json = open("data.json","w")
    archivo_json.write(datos)
    archivo_json.close()
    return datos

print(clima())

    



