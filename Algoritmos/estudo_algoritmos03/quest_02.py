valor1 = int(input("Digite um número: "))
valor2 = int(input("Digite outro valor: "))
valor3 = int(input("Digite mais um valor: "))

if valor1 < valor2 and valor2 < valor3:
    if valor1 < valor2 and valor3 < valor2:
        print("Ordem crescente: ", valor1, valor3, valor2)
    print("Ordem crescente: ", valor1, valor2, valor3)

elif valor2 < valor1 and valor1 < valor3:
    if valor2 < valor1 and valor3 < valor1:
        print("Ordem crescente: ", valor2, valor3, valor1)
    print("Ordem crescente: ", valor2, valor1, valor3)

elif valor3 < valor1 and valor1 < valor2:
    if valor3 < valor1 and valor2 < valor1:
        print("Ordem crescente: ", valor3, valor2, valor1)
    print("Ordem crescente: ", valor3, valor1, valor2)

else:
    print("Ordem crescente: ", valor3, valor2, valor1) 