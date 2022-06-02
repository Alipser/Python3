from unidecode import unidecode
import pandas as pd
import numpy as np

 
lista_texto=("Usted forma parte de un equipo que se dedica a analizar textos pequeños para "
"conocer su composición. Los compañeros de equipo han creado a partir de un "
"cuento breve una lista de Python que contiene cada una de las palabras que lo "
"componen; pero en la creación de la lista de palabras no evitaron que "
"aparecieran adheridos a algunas de las palabras los signos de puntuación ni los "
"guiones que estaban dentro del cuento original."
"A pesar de ello, a usted le han delegado determinar cuáles son las 20 palabras "
"más frecuentes en esta lista de Python y también la cantidad de veces que cada "
"una de ellas aparece en la lista, con las siguientes condiciones:")

delete_char=['-','¿','?','.',',','¡','!',':','"','–',";","\n"]
no_tildes = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )

for i in range(len(delete_char)):
     lista_texto= lista_texto.replace(delete_char[i],"")

for a, b in no_tildes:
         lista_texto =  lista_texto.replace(a, b)

lista_texto= lista_texto.upper()
lista_texto= lista_texto.split(' ')



lista_texto={"words": lista_texto}
lista_texto=pd.DataFrame.from_dict( lista_texto)
lista_conteo = pd.DataFrame(( lista_texto['words'].value_counts().head(20)))
lista_conteo=lista_conteo.reset_index()
lista_conteo=lista_conteo.to_numpy().tolist()



print((lista_conteo))
