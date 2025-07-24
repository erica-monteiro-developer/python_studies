"""
Estrutura de Dados - Set (Conjunto)

-  Mutável

- Não ordenado (sem ordem garantida)

- Não indexado (não dá para acessar por set[0])

- Não permite elementos repetidos
"""

filmsSet = {"Inception", "The Shawshank Redemption",
            "The Dark Knight", "Pulp Fiction", "Interstellar"}

print(type(filmsSet))

# 1 - Buscar o tamanho do set
print(len(filmsSet))

# 2 - True e 1 são considerados o mesmo valor
# Imprime só True, não imprime 1
exempleSet = {"Inception", True, 1, 8.7}
print(exempleSet)

# 3 - Adicionar item de outro set
filmsSet.update(exempleSet)
print(filmsSet)

# 4 - Remover um item no set
filmsSet.remove(True)
filmsSet.remove(8.7)
print(filmsSet)
