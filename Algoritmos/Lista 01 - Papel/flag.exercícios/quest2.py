obras = []
nome_artista = input("Digite o nome de um artista: ")

while nome_artista != 0:
    obras = input("Digite o nome da obra do {nome_artista}: ")
    categoria = input("Digite a categoria da obra (Escultura ou quadro): ")
    preco = float(input("Digite o valor da obra: "))

#nome do artista da obra mais cara e categoria da obra mais barata

    if preco > 0:
        obras = {"nome_artista": nome_artista, "preco": preco, "categoria": categoria}
        obras.append(obras)
    
    if obras:
        esculturas = [obra for obra in obras if obra["categoria"].lower() == "escultura"]
        escultura_mais_cara = max(esculturas, key=lambda x: x["preco"])

# Encontra a obra mais barata
        obra_mais_barata = min(obras, key=lambda x: x["preco"])

#resultados
    print(f"\nArtista da escultura mais cara: {escultura_mais_cara['nome_artista']}")
    print(f"Categoria da obra mais barata: {obra_mais_barata['categoria']}")
else:
    print("Nenhuma obra foi informada.") 