# Módulo Operações Matemáticas
def sum(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        # gera erro
        raise ValueError("Não é permitido divisão por zero.")