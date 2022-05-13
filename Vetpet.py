Nombres= ["Martín", "Milú", 'Anastasia', 'Lupita', 'Tomasa', 'Pelusa', 'Genoveva', 'Motita']
Tipos= ['canino', 'canino', 'felino', 'felino', 'felino', 'canino', 'bovino', 'roedor']
Edades= [12, 9, 10, 8, 9, 2, 14, 1]
Pesos= [33, 26, 4, 5, 5, 6, 106.4, 0.34]

D1_key=list(range(1,len(Nombres)+1))
Dict_patient_init=dict(zip(D1_key,zip(Nombres,Tipos,Edades,Pesos)))
print(Dict_patient)
