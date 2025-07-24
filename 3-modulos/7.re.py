''' 
Trabalha com expressões regulares

Expressões regulares (regular expressions - regex) ->
São padrões que você define para buscar, filtrar, validar... 
partes de uma string
'''
import re

text = "Udemy - uma plataforma com muitos cursos"

# search(padrão, string) -> procura em qualquer parte da string

# - O 'r' significa uma raw string (string bruta)
# A raw string ignora caracteres de escape como \n \t \\ e etc
# Isso é importante poque muitas exp. regulares usam barras
#  invertidas \
match = re.search(r'uma plataforma', text)
# start e end são métodos usados no OBJETO DE CORRESPONDÊNCIA 
# que é retornado por re.match(), re.search(), ou re.finditer()
# - start() -> índice onde a correspondência começou
# - end() -> índice onde a correspondência terminou
print(f"Índice inicial: {match.start()}")
print(f"Índice final: {match.end()}")

# 2- Buscando o índice que possui o ponto
# \. -> procura o caractere ponto '.'
# ponto sozinho em regex significa "qualquer caractere"
site = 'https://udemy.com'
match = re.search(r'\.', site)
print(match)

# 3- Buscando uma lista de caracteres dentro de uma frase
# [g-m] -> encontra todas as letras de g a m na string text
# findall(padrão, string) -> Procura TODAS AS OCORRÊNCIAS DO 
# PADRÃO NA STRING INTEIRA e retorna uma lista com os resultados.
pattern = "[g-m]"
result = re.findall(pattern, text)
print(result)

# 4- Verificando o início de uma string
# ^A -> o início da string (^) deve ter o caractere A
# match(padrão, string) -> Procura correspondência com o padrão 
# APENAS NO INÍCIO da string
rule = r'^A'
phrases = ['A casa está suja', 'O dia está lindo', 'Vamos passear']
for f in phrases:
    if re.match(rule, f):
        print(f"Corresponde: {f}")
    else:
        print(f"Não Corresponde: {f}")
        
# 5 - Verificando o final de uma string
# !$ -> Verifica se o final da string $ tem !
rule_end = r'!$'
phrase2 = "O dia está lindo!"
match = re.search(rule_end, phrase2)
if match:
    print("Sim, corresponde")
else:
    print("Não corresponde")