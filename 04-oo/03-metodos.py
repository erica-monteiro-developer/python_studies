class Game:
    # método construtor 'def __init__' -> ele é chamado 
    # automaticamente toda vez que você cria um novo objeto
    # com ele definimos os atributos já na criação do objeto

    # self -> representa o próprio objeto que está sendo criado 
    # ou usado. Seria como 'esse objeto'

    # esse método tá recebendo parametros com valor padroa, ou 
    # seja, pode instanciar mesmo sem passar nada
    def __init__(self, name="", yearLaunch=0, multiplayer=0, note=0):
        # self.name -> atributo da classe
        # name -> valor passado como parâmetro 
        self.name = name  
        self.yearLaunch = yearLaunch
        self.multiplayer = multiplayer
        self.note = note
    
    '''
    __str__ -> método especial que define que o objeto será
    exibido como texto e não como endereço de memória
    '''
    def __str__(self):
        return f"Game: {self.name}"

# Instanciando a classe
game1 = Game("The Legend of Zelda", 2017, False, 9.5)
game2 = Game("Fortnite", 2017, True, 8.0)

print("###Dados do Jogo###")
print(f"\nNome do jogo: {game1.name}\nAno de Lançamento: {game1.yearLaunch}")
print(f"\nNome do jogo: {game2.name}\nAno de Lançamento: {game2.yearLaunch}")

# print(game1) # Saída -> Game: The Legend of Zelda