


Unitary_price =eval(input('Input product unitary price: '))
print (Unitary_price)
sQuestion = input('Does the product have already taxes? [y/n]: ')

def verification(a):
    while a != 'y' and a != 'n':
        print ('Enter y or n')
        a = input('Does the product have already taxes? [y/n]: ')

verification(sQuestion)

if sQuestion == 'y':
    print(f'The produc already have taxes of 19%')
else:
    Unitary_price = Unitary_price*1.19
    print(f'We have added 19% taxes : {Unitary_price}')


print(f'Subtotal price per unity: {Unitary_price:1.3f}')

Number_products=int(input('How many products will you buy:'))
print(f'Total price: {Number_products*Unitary_price:1.3f}')
