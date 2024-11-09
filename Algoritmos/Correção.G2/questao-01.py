maior_quantidade_homens = 0
total_gasto_mulheres = 0
quantidade_mulheres = 0

quantidade = int(input("Digite a quantidade comprada (0 para encerrar): "))

while quantidade != 0:
    sexo = input("Digite o sexo do cliente (m ou f): ")
    
    valor_gasto = quantidade * 10
    print("Valor gasto pelo cliente: R$ ", valor_gasto)
    
    if sexo == 'm' and quantidade > maior_quantidade_homens:
          maior_quantidade_homens = quantidade
    
    if sexo == 'f':
        total_gastos_mulheres = total_gasto_mulheres = valor_gasto
        quantidade_mulheres = quantidade_mulheres + 1
        
    quantidade = int(input("Digite a quantidade comprada (0 para encerrar): "))

media_gastos_mulheres = total_gasto_mulheres / quantidade_mulheres
print("Maior quantidade vendida para os homens: ", maior_quantidade_homens)
print("Média dos gastos das mulheres: R$ ", media_gastos_mulheres)