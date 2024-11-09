num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))
ordem = input("Digite em qual ordem você quer os números: crescente(c) ou  decrescente(d): ").lower()

if ordem == 'c':
    if num1 < num2:
        print(f"Ordem crescente: {num1}, {num2}")
    else:
        print(f"Ordem cresente: {num2}, {num1}")
        
if ordem == 'd':
    if num1 > num2:
        print(f"Ordem decrescente: {num1}, {num2}")
    else:
        print(f"Ordem decrescente: {num2}, {num1}")
    
    
