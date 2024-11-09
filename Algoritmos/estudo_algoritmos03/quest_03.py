x = float(input("Digite o valor do lado x de um triângulo: "))
y = float(input("Digite o valor do lado y de um triângulo: " ))
z = float(input("Digite o valor do lado z de um triângulo: "))

if x + y > z and x + z > y and y + z > x:
    print("É um triângulo.")
else:
    print("Não é um triângulo.")


if x == y and z == y:
    print("Triângulo equilátero: ",x, y, z)

elif x == y and z != y:
    print("Triângulo isósceles: ",x, y, z)
    if x != y and z == y:
        print("Triângulo isósceles: ",z, y, x)
        if x == z and y != x:
            print("Triângulo isósceles: ",x, z, y)

elif x != y and z != y:
    print("Triângulo escaleno: ",x, y, z)