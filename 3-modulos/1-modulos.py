'''
Para criar um módulo no Python basta criar um arquivo e colocar
nele a codificação que você acha necessária para aquele módulo.
É um arquivo com instruções, variáveis, funções, classes..., 
reutilizável

Os frameworks organizam seus códigos por meio de módulos

Ao digitar help('modules') no interpretador do python no terminal, 
ele retorna uma lista de módulos nativos (já vem na instalação do
python)
'''

# Programa Principal

# importa tudo
import math_operations

''' 
importa somente a função multiply e divide

E ai não precisa usar 'math_operations.sum()', basta digitar o nome da 
função
'''
from math_operations import multiply, divide

import string_utils

print(math_operations.sum(5,3))
print(math_operations.subtract(5,3))
print(multiply(5, 3))
print(divide(5, 3))

print(string_utils.capitalize("hello"))
print(string_utils.reverse_string("python"))
print(string_utils.count("apple"))