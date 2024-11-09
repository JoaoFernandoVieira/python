import random
numeros = [random.randint(1, 200) for _ in range(50)]

numeros = []
i = 0
while i < 50:
    numero = int(input(f"Digite o número {i + 1}: "))
    numeros.append(numero)
    i = i + 1
print(numeros)

i + 5
while i <= 20:
    numeros[i] = numeros[i] * 2
    i = i + 1

soma = 0
contador = 0
i = 0

while i < 50:
    if numeros[i] > 100:
        soma = soma + numeros[i]
        contador = contador + 1
    i = i + 1

if contador > 0:
    media = soma / contador
else:
    media = 0

print("Média dos números maiores que 100: ", media)