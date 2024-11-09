idade = int(input("Digite a idade de uma pessoa: "))
if idade <= 11:
    print("Essa pessoa encontra-se na infância.")

elif idade <= 18:
    print("Essa pessoa encontra-se na adolescência.")

elif idade <= 40:
    print("Essa pessoa é um jovem adulto.")

elif idade <= 65:
    print("Essa pessoa é um adulto médio.")

else:
    print("Essa pessoa é um idoso.")