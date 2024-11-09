fruta = 'uva'
numero1 = 20
if fruta == "uva":
    numero1 = numero1 + 50
if numero1 > 40:
    numero1 = numero1 - 50
    fruta = 'amora'
else:
    fruta = 'banana'

if fruta == 'amora' :
    numero2 = 100 + numero1

elif fruta == 'banana':
    numero2 = 1000 + numero1

elif fruta == 'uva':
    numero2 = 1500 + numero1
print (fruta, numero1, numero2)