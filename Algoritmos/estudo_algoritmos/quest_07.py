cx_plastico = 5
cx_metal = 10
qnt_cx_plastico = int(input("Digite a quantidade de caixas de clips de plástico vendidas: "))
qnt_cx_metal = int(input("Digite a quantidade de caixas clips de metal vendidas: "))

valor_cx_plastico = qnt_cx_plastico * cx_plastico
print("O valor arrecadado com os clips de plástico é: R$",valor_cx_plastico)

valor_cx_metal = qnt_cx_metal * cx_metal
print("O valor arrecadado com os clips de metal é: R$",valor_cx_metal)

valor_total = valor_cx_plastico + valor_cx_metal 
print("o valor total arrecadado é: R$",valor_total)

