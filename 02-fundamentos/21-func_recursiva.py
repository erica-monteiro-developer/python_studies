"""
Uma função recursiva é uma função que chama a si mesma para 
resolver um problema em partes menores.

Precisa ter um caso base - condição que interrompe a recursão

Fatorial de um número:
1 -> 1 + 1          1
2 -> 1 * 1          2 * factorial(1) = 2
3 -> 3 * 2 * 1      3 * 2 * 1 = 6
"""

# 1 - Fatorial de um número
def factorial(num):
    if num == 1:
        return 1
    else:
        return (num * factorial(num - 1))


number = int(input("Digite o número para o fatorial:\n"))
print(f"O fatorial de {number} é {factorial(number)}")

# 2 - Soma total de um número
def total_sum(num):
    if num == 1:
        return 1
    else:
        return (num + total_sum(num - 1))


num = int(input("Digite o número para soma:\n"))
print(f"A soma total {num} é {factorial(num)}")
