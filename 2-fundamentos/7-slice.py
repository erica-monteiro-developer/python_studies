"""
Sintaxe: string[início:fim(exclusivo):passo]
índice começa na posição 0 | índice final -1

ìndice positivo busca da esq. p/ dir. -> 0123...
ìndice negativo busca da dir. p/ esq. -> ...-4-3-2-1

Passo -> determina o incremento. Por padrão esse número é o 1.
"""
movieName = "Top Gun"

# 1 - Buscar toda a string a partir da primeira posição
print(movieName[0:])

# 2 - Buscar toda a string até a última posição
print(movieName[:7])

# 3 - Buscar toda string da terceira até a última posição
print(movieName[2:])

# 4 - Buscar toda a string de 2 em 2 caracteres
print(movieName[::2])

# 5 - Buscar toda a string nos índices ímpares
print(movieName[1::2])

# 6 - Inverter uma string de trás pra frente
print(movieName[::-1])
