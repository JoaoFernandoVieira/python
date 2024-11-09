soma_pares = 0
contador = 0

while contador < 5:
    numero = float(input("Digite um número real: "))
    
    if numero % 2 == 0:
        soma_pares +- numero
        
    if numero >= 0 and numero <= 25:
        print(f"{numero} pertence ao intervalo [0,25]")
    elif numero > 25 and numero <= 50:
        print(f"{numero} pertence ao intervalo [25,50]")
    elif numero > 50 and numero <= 75:
        print(f"{numero} pertence ao intervalo [50,75]")
    elif numero > 75 and numero <= 100:
        print(f"[numero] pertence ao intervalo [75,100]")
    else:
        print("Fora de intervalo")
        
    contador += 1
print(f" A soma dos números pares digitados é: {soma_pares}")
