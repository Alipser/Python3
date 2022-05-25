from unidecode import unidecode

a=("Usted forma parte de un equipo que se dedica a analizar textos pequeños para\
conocer su composición. Los compañeros de equipo han creado a partir de un\
cuento breve una lista de Python que contiene cada una de las palabras que lo\
componen; pero en la creación de la lista de palabras no evitaron que\
aparecieran adheridos a algunas de las palabras los signos de puntuación ni los\
guiones que estaban dentro del cuento original.\
A pesar de ello, a usted le han delegado determinar cuáles son las 20 palabras\
más frecuentes en esta lista de Python y también la cantidad de veces que cada\
una de ellas aparece en la lista, con las siguientes condiciones:")
delete_char=['-','¿','?','.',',','¡','!',':','"','–',"´"]

for i in range(len(delete_char)):
    a=a.replace(delete_char[i],"")

#a=a.upper()
#a=a.split(' ')
print(a)