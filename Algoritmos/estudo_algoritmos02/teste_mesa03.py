valor1 = 10
valor2 = 40
valor3 = 80

if valor1 > valor3:
    valor1 = 60
    valor2 = valor1 - 20
    valor3 = valor2 - 30

if valor2 < valor3:
    valor2 = 30
    valor3 = 50

if valor3 > valor2:
    valor3 = valor2 + 10
    valor1 = 25
    valor2 = 55

print (valor1)
print (valor2)
print (valor3)