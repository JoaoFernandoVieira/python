mes = ''
ano = 0
valor_vendido = 0
categoria = ''
opc = 'S'
categoria_menor_venda = ''
menor_venda = 999999999
valor_venda_total = 0
qtd_venda = 0

while opc != 'N':
    mes = input("Digite o mês da venda: ")
    ano = int(input("Digite o ano da venda: "))
    valor_vendido = float(input("Digite o valor da venda: "))
    categoria = input("Digite a categoria: ")
    
    if categoria == "eletronicos" and valor_vendido > 3500:
        valor_vendido = valor_vendido - (valor_vendido * 0.10)
        print(f"Valor com desconto: {valor_vendido}")
    elif categoria == "roupas" and valor_vendido > 200:
        valor_vendido = valor_vendido - (valor_vendido * 0.10)
        print(f"Valor com desconto: {valor_vendido}")
    else: 
        print(f"Valor e categoria não se aplicam em descontos. Valor da venda: {valor_vendido}")
        
    if valor_vendido < menor_venda:
        categoria_menor_venda = categoria
        
    qtd_venda += 1
    valor_venda_total += valor_vendido
        
    opc = input("Deseja continuar? (S - Sim ou N - Não)")
    

print(f"Categoria do produto que teve o menor valor de venda: {categoria_menor_venda}")
print(f"Média dos valores das venda realizadas: {valor_venda_total/qtd_venda}")