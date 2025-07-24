'''
As collections extendem as funcionalidades das estruturas de daods que vimos antes
'''
from collections import Counter, namedtuple, deque
from operator import itemgetter

# 1 - Lista de Frutas (Contagem)
fruits = ["Maçã", "Banana", "Uva", "Pêra", "Banana",
          "Uva", "Maçã", "Laranja", "Banana",
          "Abacaxi", "Tangerina", "Uva", "Pêra", "Banana"]
print(fruits)
print(Counter(fruits))

# 2 - Utilizando tupla nomeada
# permite que a tupla tenha não só valores como 'chaves'
'''
namedtuple('game', ['name', 'price', 'note']) ->  cria uma classe personalizada imutável chamada game com os campos name, price e note
'''
# game = namedtuple('game', ['name', 'price', 'note'])
# g1 e g2 são instâncias dessa classe
# g1 = game("Fifa 23", 90.50, 8.5)
# g2 = game("Resident Evil 4 Remake", 300, 10.0)
# print(g1)
# print(g2)

# 3 - Ordenando dicionários 
# key = itemgetter(0) -> ordena pela chave, ou seja pelo nome, 
# em ordem alfabética
# key = itemgetter(1) -> ordena pelo valor (idade)
# students = {"Pedro": 23, "Ana": 22, "Ronaldo": 26, "Janaína": 25}
# a = sorted(students.items(), key = itemgetter(0))
# print(a)

# 4 - Utilizando uma fila em ambas extremidades
# É uma estrutura que permite adicionar/remover no fim e no 
# início
deq = deque([20, 40, 60, 80])
# Adiciona no início
deq.appendleft(10)
print(deq)
# Adiciona no fim
deq.append(90)
# Remove do início
deq.popleft()
# Remove do fim
deq.pop
print(deq)