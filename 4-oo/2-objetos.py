class Game:
    name = ""
    yearLaunch = 0
    multiplayer = False
    note = 0

# Primeiro jogo -> Primeira Instância (Objeto)
game1 = Game() # Instancio como se fosse uma função, noutras linguagens é com new Game alguma coisa

# Atribuindo valores diretamente aos atributos ->
game1.name = "The Legend of Zelda: Breath of the Wild"
game1.yearLaunch = 2017
game1.multiplayer = False
game1.note = 9.5

# Segundo jogo
game2 = Game()
game2.name = "Fortnite"
game2.yearLaunch = 2017
game2.multiplayer = True
game2.note = 8.0

# Terceiro
game3 = Game()
game3.name = "Minecraft"
game3.yearLaunch = 2013
game3.multiplayer = True
game3.note = 10

# Acessando os atributos do objeto
print("###Dados do Jogo###")
print(f"\nNome do jogo: {game1.name}\nAno de Lançamento: {game1.yearLaunch}")
print(f"\nNome do jogo: {game2.name}\nAno de Lançamento: {game2.yearLaunch}")
print(f"\nNome do jogo:{game3.name}\nAno de Lançamento: {game3.yearLaunch}\nNota do jogo: {game3.note}")