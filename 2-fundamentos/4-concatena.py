# Concatenar -> juntar strings com strings/variáveis
name = input("Digite o nome do filme:\n")
yearLaunch = int(input("Digite o ano de lançamento do filme:\n"))
noteMovie = float(input("Digite a nota do filme:\n"))

print("Dados do Filme")
print("==================================")

# Alternativa 1
# Ao usar vírgula, tô passando diferentes argumentos, que são 
# separados automaticamente por " "
print("Nome do filme:", name)
print("Ano de lançamento:", yearLaunch)
print("Nota do filme:", noteMovie)

# Alternativa 2
print("Nome do filme: {}".format(name))
print("Ano de lançamento: {}".format(yearLaunch))
print("Nota do filme: {}".format(noteMovie))
print("Qual é o nome do filme, que a nota foi de {1} e ele saiu em {0}?".format(
    yearLaunch, noteMovie))

# Alternativa 3
print("Nome do filme:", name, "\nAno de lançamento:",
      yearLaunch, "\nNota do filme:", noteMovie)

# Alternativa 4 - forma mais moderna e usada -> f-strings
# Permite colocar expressões, variáveis diretamente dentro 
# da string
print(f"Nome do filme: {name}\n"
      f"Ano de lançamento: {yearLaunch}\n"
      f"Nota do filme: {noteMovie}\n"
      )
