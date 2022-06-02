nombres = ["Martín", "Milú", "Anastasia","Lupita", "Tomasa", "Pelusa", "Genoveva",
"Motita"]
tipos = ["canino", "canino", "felino", "felino", "felino", "canino", "bovino", "roedor"]
edades = [12, 9, 10, 8, 9, 2, 14, 1]
pesos = [33, 26, 4, 5, 5, 6, 106.4, 0.34]
diccionario = {}
beneficio_can_fel = {}
beneficio_equ_bov ={}
promedio_can_fel = 0
promedio_equ_bov = 0
Edades_C_f = 0
Edades_E_B = 0


#creo el primerDiccionario 

i = 0
for i in range(len(nombres)):
    lista_animal=[]
    lista_animal.extend([nombres[i],tipos[i],edades[i],pesos[i]])
    diccionario[str(i+1)] = lista_animal
    i = i +1
print(type(diccionario))

print("-----------------------------------------")
# seegundo diccionario canino_felino
c,k = (0,0)
for tipo in tipos:
    if edades[c] >=9 and (tipo == "canino" or tipo =="felino"):
       Edades_C_f = Edades_C_f + edades[c]
       lista_C_F=[]
       lista_C_F.extend([nombres[c],tipos[c],pesos[c]])
       k=k+1
       beneficio_can_fel [str(k)] = lista_C_F
    c =c+1   
print(beneficio_can_fel)


print("-----------------------------------------------")

E,B = (0,0)
for tipo in tipos:
    if edades[E] > 15 and (tipo == "equino" or tipo =="bovino"):
       Edades_E_B = Edades_E_B + edades[E]
       lista_E_B=[]
       lista_C_F.extend([nombres[E],tipos[E],pesos[E]])
       B=B+1
       beneficio_equ_bov [str(B)] = lista_E_B
    E = E+1   
print(beneficio_equ_bov)

print("------------------------------------------------")
#calculos de promedio
if k != 0:
    promedio_can_fel= Edades_C_f/k
else:
    promedio_can_fel = None
print(int(promedio_can_fel))

if B != 0:
    promedio_equ_bov= Edades_E_B/B
else:
    promedio_equ_bov = None

print(promedio_equ_bov)