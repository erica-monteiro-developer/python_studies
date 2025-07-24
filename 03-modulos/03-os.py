'''
OS -> Operational System
Esse módulo eprmite acessar algumas funções do sistema 
operacional
'''
import os
import platform

# Consultar funcionalidades do módulo os
# help('os')

# 1 - Retornar a pasta atual
print(os.getcwd())

# 2 - Listar arquivos e pastas
print(os.listdir())

# 3 - Versão do SO
#os.system('ver') -> no Windows
# No Linux há módulos como platform, distro, e essas do OS
os.system("uname -a") # Exibe informações do kernel
os.system("lsb_release -a")  # Exibe informações da distribuição 

# 4 - Configurações da Máquina
# os.system("systeminfo") -> no Windows
print("Sistema:", platform.system())

# 5 - Limpar a tela do terminal
os.system("clear") # cls no Windows

# 6 - Desligar o computador]
# por padrão em 60 segundos # -> Windows
# os.system('shutdown /s') 
# no Linux é em minutos, não em segundos
os.system('shutdown -h +1') # -> Linux

# Desliga o computador imediatamente
# os.system('shutdown /s /t 0') # -> Windows
os.system("shutdown -h now") # -> Linux

# Cancela o desligamento
# os.system('shutdown /a') # -> Windows
os.system("shutdown -c") # -> Linux

def turn_off_one_hour():
    os.system("shutdown -h +60") # 1h

def turn_off_half_an_hour():
    os.system('shutdown -h +30') # 30 minutos

def cancel_shutdown():
    os.system('shutdown -c')

# turn_off_one_hour()
cancel_shutdown()