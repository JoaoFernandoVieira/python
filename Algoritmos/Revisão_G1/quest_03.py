arroz = 8
feijao = 6
oleo = 7

qnt_arroz = int(input("Digite quantas unidades de arroz foram compradas: "))
qnt_feijao = int(input("Digite quantas unidades de feijão foram compradas: "))
qnt_oleo = int(input("Digite quantas unidades de óleo foram compradas: "))

pagar_arroz = qnt_arroz * arroz
if qnt_arroz > 10:
    pagar_arroz = pagar_arroz * 0.95
    
pagar_feijao = qnt_feijao * feijao    
if qnt_feijao > 10:
    pagar_feijao = pagar_feijao * 0.95

pagar_oleo = qnt_oleo * oleo    
if qnt_oleo > 10:
    pagar_oleo = pagar_oleo * 0.95
    
valor_total = pagar_arroz + pagar_feijao + pagar_oleo
if valor_total > 50:
    valor_total = valor_total - valor_total * 0.10

valor_total = valor_total + valor_total * 0.02
print("O valor total a ser pago é: ", valor_total)
    
