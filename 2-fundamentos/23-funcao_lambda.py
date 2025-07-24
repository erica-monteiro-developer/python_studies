'''
Uma função lambda é uma função anônima, ou seja, sem nome,
criada de forma rápida e compacta, geralmente em uma única 
linha.

Essa função é definida como se tivesse recebendo uma variável
'''

# Função de potência de um número
def power(num): return num ** 2

# Função que verifica se o número é par
def is_even(x): return x % 2 == 0


# Função que divide um número por outro
def div_num(x, y): return x / y

# Função que inverte uma string
def reverse_string(s): return s[::-1]

print(power(5))
print(power(9))
print(is_even(20))
print(is_even(37))
print(div_num(10, 2))
print(div_num(6, 2))
print(reverse_string("Python"))
print(reverse_string("JavaScript"))

# Funcionalidades relacionadas aos filmes:
movies_list = ["Titanic", "GodFather",
               "Inception", "Jurassic Park", "The Matrix"]
ratings = {
    "Titanic": [8.5, 9.0, 7.5],
    "The GodFather": [9.5, 9.8, 8.0],
    "Inception": [8.0, 7.0, 8.5],
    "Jurassic Park": [7.5, 7.0, 8.0],
    "The Matrix": [8.8, 9.2, 10],
}

# Função para calcular a média de avaliações de um filme
def average_rating(movie_name): return sum(
    ratings[movie_name]) / len(ratings[movie_name])

# Função que verifica se um filme está na lista
def check_movie(movie_name): return movie_name in movies_list

# Função para recomenda um filme com base na avaliação média
def recommend_movie(
    movie_name): return f"Recomendo assistir {movie_name} com média de {average_rating(movie_name):.2f} pontos."

print(
    f"Média de Avaliação do filme The Matrix: {average_rating("The Matrix")}")
print(f"Inception está na lista? {check_movie("Inception")}")
print(f"{recommend_movie("Titanic")}")
