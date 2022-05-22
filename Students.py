grupo =[] 
estudiante = {}
continua = "s"
i=0
Lista_de_estudiantes=[]


while continua == "s":
    i +=1
    Creador_estudiante="Estudiante"+str(i)
    Lista_de_estudiantes.append(Creador_estudiante)
    cédula = int(input("Ingrese el número del documento:"))
    nombre = input("Ingrese nombre estudiante:")
    nota_fundamentos = float(input("Ingrese nota:"))
    estudiante[f"Estudiante {str(i)}"]= {'cédula' : cédula,'nombre' : nombre, 'nota_fundamentos' : nota_fundamentos}
    Lista_de_estudiantes.append(Creador_estudiante)
    continua = input("Desea cargar otro estudiante[s/n]?")

print(estudiante)

estudiante1=estudiante["Estudiante 1"]
estudiante2=estudiante["Estudiante 2"]
a=[estudiante1,estudiante2]
for i in a:
    print (i)




