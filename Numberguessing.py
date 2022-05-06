from random import randint
b=randint(30,100)
#c=randint(1,5)
n=randint(0,b)
a=0
d=0
while d !=n : 
    d= int(input(f'Ingrese un valor entero entre 0 y {b} :'))
    if d < 0 or d > b :
        print('¡Te saliste del intervalo!')
    elif d > n :
        print('¡Ups! Te pasaste')
    elif d < n  :
        print('¡Ups! Estás por debajo')
    a += 1 
print(f'¡LO LOGRASTE! Usaste {a} intentos')

