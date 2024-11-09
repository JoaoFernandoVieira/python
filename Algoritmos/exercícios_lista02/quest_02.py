lista = [1,2,10,5,20]
print(lista)
escolha = int(input("Qual número deseja saber a posição: "))

i = 0
while i < len(lista):
    if lista[i] == escolha:
        print(f"o número {escolha} está no elemento de índice {i}")
        print(f"essa é a {i + 1} posição.")
    i = i + 1