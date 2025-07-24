"""
Estrutura de dados - Dicionário

- Mutável

- Ordenado (desde o Python 3.7)

- Não indexado por posição → usa chaves

- Não permite chaves repetidas (valores podem repetir)

- Usa estrutura chave: valor
"""

filmsInception = {
    "title": "Inception",
    "yearRelease": 2010,
    "imdbRating": 8.8,
    "genre": ["Sci-fi", "Action", "Thriller"]
}

print(filmsInception)
print(len(filmsInception))
print(type(filmsInception))

# 1 - Recuperar um elemento do dicionário
print(filmsInception["genre"])
print(filmsInception.get("imdbRating"))

# 2 - Buscar apenas as chaves do dicionário
print(filmsInception.keys())

# 3 - Buscar apenas os valores do dicionário
print(filmsInception.values())

# 4 - Buscar itens do dicionário com chave e valor
print(filmsInception.items())

# 5 - Adicionar itens no dicionário
filmsInception["director"] = "Christopher Nolan"
print(filmsInception)

# 6 - Atualizar itens no dicionário
filmsInception.update({"imdbRating": 8.7})
print(filmsInception)

# 7 - Remover item no dicionário
filmsInception.pop("director")
print(filmsInception)
