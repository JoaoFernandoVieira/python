qnt_melancia = int(input("Quantidade de melancia comprada: "))
qnt_abacaxi = int(input("Quantidade de abacaxi comprada: "))
qnt_morango = int(input("Quantidade de morango comprada: "))

valor_total = qnt_melancia * 10 + qnt_abacaxi * 5 + qnt_morango * 1

if qnt_melancia + qnt_abacaxi + qnt_morango > 10:
    valor_total = valor_total * 0.9

print("O valor com desconto será: R$ ", valor_total)