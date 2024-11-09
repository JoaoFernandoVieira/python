num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro valor: "))

operacao = input("Qual operação deseja realizar?(soma (s), subtração(t), multiplicação(m) ou divisão(d)): ")

if operacao == 's':
    soma = num1 + num2
    print(f"O valor da soma é: {soma} ")
    
elif operacao == 't':
    subtracao = num1 - num2
    print(f"O valor da subtração é: {subtracao} ")
    
elif operacao == 'm':
    multiclicacao = num1 * num2
    print(f"O valor da multiplicação é: {multiclicacao}")
    
elif operacao == 'd':
    if num2 == 0:
        print("Divisão por zero não permitida.")
    else:
        divisao = num1 / num2
        print(f"O valor da divisão é: {divisao}")
        