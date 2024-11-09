animais = 0
femeas_mais_5 = 0
maior_peso = 0
macho_maior100 = 0
idade_f_mais_5 = 0

especie = input('Espécie do animal: ')
while especie != 'encerrar':
    sexo = input('Qual o sexo do animal? ')
    idade = int(input('Qual a idade do animal? '))
    peso = float(input('Qual o peso do animal? '))
    animais = animais + 1
    if sexo == 'F' and idade > 5:
        femeas_mais_5 = femeas_mais_5 + 1
        idade_f_mais_5 = idade_f_mais_5 + idade
    if peso > maior_peso:
        maior_peso = peso
        mais_pesado = especie
    if sexo == 'M' and peso > 100:
        macho_maior100 = macho_maior100 + 1
        especie = input('Espécie do animal: ')
print ('A quantidade total de animais é: ', animais)
print ('A média de idade dos animais fêmeas com mais de 5 anos é: ',idade_f_mais_5/femeas_mais_5)
print ('A espécie do animal mais pesado do zoológico é: ', mais_pesado)
print ('A porcentagem de animais machos com peso acima de 100 kg é: ',macho_maior100/animais)
