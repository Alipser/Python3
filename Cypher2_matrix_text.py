############ENCRIPATADO###########################################

import numpy as np
texto=input("Escriba el mensaje a encripar:  ")
clave=eval(input("ingrese un clave"))
lentexto=len(texto)
sqrtlentexto=lentexto**(0.5)
flagsize=sqrtlentexto-int(sqrtlentexto)
if flagsize == 0:
    a= (int(sqrtlentexto))
else:
    a= (int(1+int((sqrtlentexto))))
texto=texto.ljust(a**2, "_")
texto=list(texto)
texto=texto[clave:]+texto[:clave]
texto=list(map(ord,texto))
texto=np.array(list(texto)).reshape((a,a))
print(texto)
####################################################################
newtexto=texto.ravel().tolist()
newtexto=newtexto[(-1*clave):]+newtexto[:(-1*clave)]
newtexto=list(map(chr,newtexto))
newtexto=''.join(newtexto)
newtexto=newtexto.replace("_","")
print(newtexto)