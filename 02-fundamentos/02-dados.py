'''
Variáveis -> espaços reservados na memória para armazenar 
dados, que podem ser usados e modificados ao longo do programa

1. Devem começar com letra ou underscore _
2. Pode ter números, letras e underscores
3. Não pode ter palavras reservadas
4. Python diferencia maiúsculas de minúsculas (case sensitive)
5. Não pode haver espaços nos nomes de variáveis. Para separar
palavras, usamos convenções de estilo (não obrigatórias, mas 
recomendadas).
- snake_case → Padrão oficial do Python (PEP 8) - recomendada 
para variáveis e funções
- camelCase → usado em outras linguagens (JavaScript, Java) - 
pode ser usado no Python, mas não é a convenção oficial p/ 
variáveis
-  PascalCase → padrão para nomes de classes
'''

# Pythonflix
# Tipos elementares (ou Primitivos/Valor)
# Tipos básicos que armazenam valores diretamente na variável
# Quando faço uma cópia desses valores, não há ligação entre
# variáveis
name = "Top Gun Maverick" # string -> texto
yearLaunch = 2023 # inteiro
noteMovie = 9.5 # float - número decimal
planIncluded = False # bool - valor lógico -> True ou False
print(name)
print(yearLaunch)

# type é uma função que identifica o tipo de dado da variável
print(type(name))
print(type(yearLaunch))
print(type(noteMovie))
print(type(planIncluded))
