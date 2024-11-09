maior = -1
menor = 1001
i = 0

while i < 20:
    num = int(input("Digite um número entre (0 e 1000):"))
    if num > maior:
        maior = num
    
    if num < menor:
        menor = num
    i = i + 1
print("O maior número é: ", maior)
print("O menor número é :  ", menor)