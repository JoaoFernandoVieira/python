maior = 0
cont_num = 0
soma = 0
num = int(input("Digite um número: "))
while num != -1:
    soma = soma + num
    cont_num = cont_num + 1
    
    if num > maior:
        maior = num
    num = int(input("Digite um número: "))