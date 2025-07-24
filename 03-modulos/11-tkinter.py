'''
Por desse módulo conseguimos construir aplicações desktop na 
linguagem Python, é um módulo nativo.
'''
# as -> permite definir um alias (apelido) pro módulo
import tkinter as tk

# 1 - Criando a Janela
window = tk.Tk()
window.geometry("300x150")# largura e altura da janela (x+y)
window.title("Gerencia Frases") # título da barra de títulos

# 2 - Adiciona um Frame contido dentro da janela
frame = tk.Frame(window)
# padx=10, pady=10 → adiciona espaço (margem) ao redor do frame.
# fill='x' → faz o frame ocupar toda a largura.
# expand=True → faz o frame expandir se a janela crescer.

# pack() -> Coloca o widget embaixo do anterior (verticalmente 
# por padrão, ou horizontalmente com side=)
frame.pack(padx=10, pady=10, fill='x', expand=True)

# 3 - Adicionando o Label
# cria um rótulo no frame com o texto “Olá mundo”.
label = tk.Label(frame, text="Olá mundo")
# fill='x' → o label vai se esticar horizontalmente.
# expand=True → ajuda a centralizar e ocupar mais espaço, se 
# necessário.
label.pack(fill='x', expand=True)

# 4 - Adicionando o input text
frase_lab = tk.Label(frame, text="Frase")
frase_lab.pack(fill='x', expand=True)

# Entry -> um campo de entrada de texto (input) onde o usuário 
# pode digitar algo.
frase_inp = tk.Entry(frame)
frase_inp.pack(fill='x', expand=True)

# 5 - Função para alterar o texto do label
def click():
    # altera o texto da label pela entrada do usuário recebida
    label.config(text=frase_inp.get())

# 6 - Adicionando o Botão
# command=click -> quando clicado, chama a função click() que 
# muda o texto do label
button = tk.Button(frame, text="Enviar", command=click)
button.pack()

# Inicia o loop principal da interface gráfica, mantendo a 
# janela aberta até o usuário fechar.
window.mainloop()