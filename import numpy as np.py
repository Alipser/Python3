
import numpy as np
import random
texto=input('Enter your message:')
lentexto=len(texto)
sqrtlentexto=lentexto**(0.5)
flagsize=sqrtlentexto-int(sqrtlentexto)
if flagsize == 0:
    a= (int(sqrtlentexto))
else:
    a= (int(1+int((sqrtlentexto))))
texto=texto.ljust(a**2, "_")
texto=list(texto)
previewclave= list(enumerate(texto))    
random.shuffle(previewclave)

clave, array_encriptado = zip(*previewclave)

array_encriptado=list(map(ord,array_encriptado))
array_encriptado=np.array(array_encriptado).reshape((a,a))

print(array_encriptado)
print(clave)

array_encriptado=array_encriptado.ravel().tolist()
array_encriptado=list(map(chr,array_encriptado))
reorder=[]
for i in range(len(array_encriptado)):
    reorder.append(array_encriptado[clave.index(i)])
reorder="".join(reorder)
reorder=reorder.replace("_","")

print(reorder)


