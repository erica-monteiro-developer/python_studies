num1 = int(input("Digite o primeiro número:\n"))
num2 = int(input("Digite o segundo número:\n"))

# Aritméticos (matemáticos)
sum = num1 + num2
sub = num1 - num2
div = num1 / num2
mult = num1 * num2
mod = num1 % num2 # retorna resto da divisão
exp = num1 ** num2

# print(sum)
# print(sub)

print(f"Potência do número {num1} por {num2} é: {exp}")
print(f"Resto da divisão de {num1} por {num2} é: {mod}")

# Comparação
bigger = num1 > num2 # maior que
smaller = num1 < num2 # menor que
equal = num1 == num2 # igual a 
different = num1 != num2 # diferente de
bigger_equal = num1 >= num2 # maior ou igual que
smaller_equal = num1 <= num2 # menor ou igual que

print(f"Os números {num1} e {num2} são iguais? {equal}")
print(f"O número {num1} é maior que {num2}? {bigger_equal}")

# Atribuição ('=' -> receber valor)
num1 += 1  # num1 = num1 + 1
num1 -= 1  # num1 = num1 - 1
num1 *= 1  # num1 = num1 * 1
num1 /= 1  # num1 = num1 / 1
