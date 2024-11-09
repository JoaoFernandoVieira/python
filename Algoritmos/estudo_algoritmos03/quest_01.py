valor1 = int(input("Digite um valor: "))
valor2 = int(input("Digite outro valor: "))
valor3 = int(input("Digite mais um valor: "))

if valor1 < valor2 and valor1 < valor3:
    print("O menor valor é o valor 1: ", valor1)

if valor2 < valor1 and valor2 < valor3:
    menor = valor2
    print("O menor valor é o valor 2: ", valor2)

else:
    menor = valor3
    print("O menor valor é o valor 3: ", valor3)