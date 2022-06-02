a=[x for x in range(1,19)]
print (a)
Ca=int(input(""))
cb=int(input(""))
aa=int(input(""))
ab=int(input(""))

def organizador(cicloa, ciclob,añoa, añob):
    if añoa>añob:
        return([ciclob,cicloa,añob,añoa])
    return(cicloa, ciclob,añoa, añob)
        

def restas(cicloa, ciclob,añoa, añob):
    if añoa==añob:
        resta=abs(cicloa-ciclob)
    elif añob > añoa:
        resta=abs((18- cicloa + ciclob))+(18*((abs(añoa-añob)-1)))
    return(resta)
    
a=(organizador(Ca, cb,aa, ab))
print()
print(restas(a[0], a[1],a[2], a[3]))


  