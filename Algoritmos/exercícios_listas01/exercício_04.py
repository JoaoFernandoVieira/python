numeros_pares = []
i = 0
while i < 10:
    numeros = int(input("Digite um número inteiro: "))
    if numeros % 2 == 0:
        numeros_pares.append(numeros)
    i = i + 1
print(numeros_pares)