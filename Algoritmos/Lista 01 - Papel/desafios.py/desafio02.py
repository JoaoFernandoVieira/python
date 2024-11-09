def main():
    algo = input("Digite algo: ")

    # Exibe o tipo primitivo da entrada
    print(f"O tipo primitivo de '{algo}' é: {type(algo)}")

    
    print(f"É um número? {algo.isnumeric()}")
    print(f"É alfabético? {algo.isalpha()}")
    print(f"É alfanumérico? {algo.isalnum()}")
    print(f"Está em maiúsculas? {algo.isupper()}")
    print(f"Está em minúsculas? {algo.islower()}")
    print(f"Está capitalizado (primeira letra maiúscula)? {algo.istitle()}")
    print(f"É um espaço? {algo.isspace()}")

    # Se for um número, verificar se é decimal
    if algo.isnumeric():
        print(f"É um número decimal? {algo.isdecimal()}")
    
    # Verifica se é um identificador válido em Python
    print(f"É um identificador válido? {algo.isidentifier()}")

    # Verifica se é imprimível
    print(f"É imprimível? {algo.isprintable()}")

if __name__ == "__main__":
    main()
