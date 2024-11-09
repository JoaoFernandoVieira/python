lista = [20,31,42,46,54,55,66,77,58,29,30]
par = []
impar = []

i = 0
while i < len(lista):
    if lista[i] % 2 == 0:
        print(f"O número {lista[i]} é par.")
        par.append(lista[i])
    else:
        print(f"O número {lista[i]} é ímpar")
        impar.append(lista[i])
    i = i + 1

print("Lista original: ", lista)
print("Lista de números pares: ", par)
print("Lista de número ímoares: ", impar)