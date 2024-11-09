lista =[]
i = 0
while i < 6:
    numeros = float(input("Digite um número inteiro: "))
    lista.append(numeros)
    i = i + 1
soma_lista = sum(lista)
media = soma_lista / len(lista)
print("A soma dos elementos da lista é: ", soma_lista)
print("A média dos elementos da lista é: ", media)
print(lista)