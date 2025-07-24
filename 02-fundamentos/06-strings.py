movie_name = "Top Gun"
movie_name2 = "top gun"

# Python é case sensitive (a != A)
print(movie_name == movie_name2)

movieDescription = """
    Top Gun Maverick é um filme de aviação e aventura
muito consagrado na indústria.
"""
print(movie_name)

# 1- Multiplicação de Strings
line = "="
print(line * 20)  # ao invés de digitar "========"
print(movieDescription)

# 2- Procurar uma palavra dentro de um texto
# in -> está em -> retorna True ou False
print("Top" in movie_name)
print("Top" not in movie_name)
