"""
While -> loop

sintaxe: 
variavel_de_controle = 0
enquanto condicao_com_variavel_de_controle_for_true: 
    faça X
    variavel_de_controle += Y # ou -=

Ao contrário do for, precisa de um índice, uma variável de
controle (se não haver incremento/decremento nela, o loop é infinito)
"""

# Lista de Filmes
moviesList = ["Titanic", "The Godfather", "Inception", "Jurassic Park"]

# 1 - Iterando valores de uma lista de filmes usando while
index = 0
while index < len(moviesList):
    print(moviesList[index])
    index += 1

# 2 - Quando a condição for atendida, o loope será encerrado
index = 0
while index < len(moviesList):
    if moviesList[index] == "Inception":
        break
    print(moviesList[index])
    index += 1

# 3 - Quando a condição for atendida, o loop vai para a próxima
# iteração
index = 0
while index < len(moviesList):
    if moviesList[index] == "Inception":
        index += 1
        continue
    print(moviesList[index])
    index += 1

# 4 - Avaliação do filme com while:
movieName = input("Digite o nome do filme:\n")
movieRating = int(input("Digite quantas avaliações deseja fazer:\n"))

total = 0
count = 0

while count < movieRating:
    note = float(input("Digite a nota para o filme:\n"))
    total += note
    count += 1

if movieRating > 0:
    average = total / movieRating
else:
    average = 0

print(f"Média de avaliação do filme {movieName} é: {average:.2f}")
