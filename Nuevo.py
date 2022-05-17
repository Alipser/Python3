from ntpath import join


Coding=input("Ingrese codigo a cifrar:  ")
Coding_upper=Coding.upper()
Coding_upper_unique=list(set(Coding_upper))
Key_list=(list(map(chr, range(65, 65+len(Coding_upper_unique)))))
Dict1=dict(zip(Coding_upper_unique, Key_list))
Dict1[''] = ''

##################################################################################################
valor=list()
for i in range(len(Coding_upper)):
     valor.append(Dict1.get((Coding_upper[i])))  
valor=''.join(valor)
################################################################################################

  
       


    
