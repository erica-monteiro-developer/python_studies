"""
1. Escreva um programa que lê dois nomes e retorne uma string formatada no formato "ÙltimoNome, PrimeiroNome",
2. Inverta a ordem das palavras em uma string fornecida.
3. Verifique se uma string fornecida é um palíndromo (pode ser lida da mesma forma de trás para frente).
"""

# Ex. 1:
primeiroNome = input("Digite o nome:\n")
segundoNome = input("Digite o sobrenome:\n")

nomeFormatado = f"{segundoNome} {primeiroNome}"
print(nomeFormatado)

# Ex. 2:
texto = "Python é muito legal"
palavras = texto.split()
textoInvertido = " ".join(palavras[::-1])
print(textoInvertido)

# Ex. 3:
texto1 = "arara"
texto2 = "python"

# Remove espaço e deixa nome em minúsculo
texto1_format = texto1.lower().replace(" ", "")
texto2_format = texto2.lower().replace(" ", "")

# Verifica se texto original é igual ao seu reverso
palindromo1 = texto1_format == texto1[::-1]
palindromo2 = texto2_format == texto2[::-1]

print(palindromo1)
print(palindromo2)
