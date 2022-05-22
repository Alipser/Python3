from ntpath import join

Coding=input("Ingrese codigo a cifrar:  ")
key=int(input("key:  "))
Coding_upper=Coding.upper()
Coding_upper_unique=list(set(Coding_upper))
Key_list=(list(map(chr, range(65, 91))))
Key_list=Key_list[key:]+Key_list[:key]
###############################################
newlist=[]
for x in range(len(Coding_upper)):
     newlist.append(Key_list[x])
print(newlist)
#################################################################################################
Dict1=dict(zip(Coding_upper_unique, Key_list))
Dict1[" "] = " "
print(Dict1)

##################################################################################################
valor=list()
for i in range(len(Coding_upper)):
     valor.append(Dict1.get((Coding_upper[i])))  
valor=''.join(valor)
################################################################################################

print(valor)
  
       


    
