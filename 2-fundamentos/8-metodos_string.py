movieName = "Top Gun"
movieDescription = """
    Top Gun Maverick é um filme de aviação e aventura
muito consagrado na indústria.
"""
# Tudo maiúsculo
print(movieName.upper())

# Tudo minúsculo
print(movieName.lower())

# Primeira letra maiúscula
print(movieName.capitalize())

# Primeira letra maiúscula de todas as palavras
print(movieName.title())

# Retorna string centralizada com caractere de preenchimento
print(movieName.center(10, '-'))

# Retorna a posição da substring/caractere
print(movieName.find("u"))

# Conta caracteres
print(movieName.count("u"))

# Altera um elemento por outro
print(movieName.replace("Top", "Matrix"))

# retorna o tamanho (comprimento) 
print(len(movieName))

# Divide texto em lista [] de substrings, com base no
# separador (neste caso ',')
print(movieDescription.split(','))

# Junta elementos de uma lista ou iterável em uma única
# string, usando um separador definido
nomes = ["Ana", "Carlos", "Zezin"]
resultado = ", ".join(nomes)
print(resultado)
