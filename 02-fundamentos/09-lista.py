"""
Estrutura de Dados - Lista

- Armazena valores heterogêneos
(pode misturar int, str, float, etc.)

- É mutável
(pode adicionar, remover, modificar valores)

- Índice começa do 0
(lista[0] acessa o primeiro item)

- Permite usar slice
(como toda sequência iterável)

"""
filmMatrix = []
print(type(filmMatrix))

filmsList = ["Inception", "The Shawshank Redemption",
             "The Dark Knight", "Pulp Fiction", "Interstellar"]

# 1 - Buscar os dois primeiros itens da lista
print(filmsList[:2])

# 2 - Buscar o último item da lista
print(filmsList[-1])

# 3 - Buscar filmes até uma determinada posição
print(filmsList[:3])

# 4 - Buscar filmes de uma posição em diante
print(filmsList[1:4])
