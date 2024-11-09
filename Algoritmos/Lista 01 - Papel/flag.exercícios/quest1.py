salarios = []
nome_funcionario = input("Digite o nome de um funcionário ou 'fim' para encerrar: ")

while nome_funcionario.lower() != "fim":
    salario = float(input("Digite o salário de {nome_funcionario}: "))
    salarios.append(salario)
    nome_funcionario = input("Digite o nome do próximo funcioário ou 'fim' para encerrar: ")
    
#Média,salário mais altoe salário mais baixo
    
if len(salario) > 0:
    media = sum(salarios) / len(salarios)
    salario_max = max(salarios)
    salario_min = min(salarios)
    
    print(f"Média salarial: R${media:.2f}")
    print(f"Salário maximo: R${salario_max:.2f}")
    print(f"Salário mínimo: R${salario_min:.2f}")

else:
    print("Nenhum salário foi inserido")