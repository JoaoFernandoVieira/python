hamburguer = 20
pizza = 40
sushi = 50

qnt_hamburguer = int(input("Digite quantos hamburgueres foram pedidos: "))
qnt_pizza = int(input("Digite quantas pizzas foram pedidas: "))
qnt_sushi = int(input("Digite quantos sushis foram pedidos: "))

valor_total = qnt_hamburguer * hamburguer + qnt_pizza * pizza + qnt_sushi * sushi
if valor_total > 150:
    valor_total = valor_total - valor_total * 0.15
    valor_total = valor_total + 10
print("O valor total a ser pago é: R$", valor_total)