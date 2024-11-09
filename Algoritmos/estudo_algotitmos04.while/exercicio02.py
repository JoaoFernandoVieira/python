nome = ''
nota = 0
alunos = 0
while alunos < 4:
    aluno = input("Digite o nome de um aluno: ")
    nota = float(input("Digite a nota do aluno: "))
    if nota >= 6:
        print("Aluno aprovado!")
    else:
        print("Aluno reprovado!")
    alunos = alunos + 1