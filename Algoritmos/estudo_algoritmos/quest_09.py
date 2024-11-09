valor_lapis = 2.0
valor_caneta = 2.50

lapis_comprados = int(input("Digite a quantidade de lápis comprados pelo cliente: "))
canetas_compradas = int(input("Agora digite a quantidade de canetas compradas pelo mesmo: "))

valor_lapis_comp = lapis_comprados * valor_lapis
print("O valor dos lápis comprados é: R$",valor_lapis_comp)

valor_caneta_comp = canetas_compradas * valor_caneta
print("O valor das canetas compradas é: R$",valor_caneta_comp)

valor_total = valor_caneta_comp + valor_lapis_comp
print("O valor total da compra foi: R$",valor_total)

 