'''
O método é emelhante a variável de classe (static)

Ambos não dependem do self, ou seja, não agem sobre o objeto,
 mas sobre a classe
'''
class Game:
    total_games = 0 # Variável de classe para contar o número total de jogos
    def __init__(self, name="", yearLaunch=0, multiplayer=0, note=0):
        self.name = name  
        self.yearLaunch = yearLaunch
        self.multiplayer = multiplayer
        self.note = note
        Game.total_games += 1
        self.totalEvaluation = 0
        self.evaluators = 0
        
    def __str__(self):
        return f"Game: {self.name}"
    
    def technical_sheet(self):
        print("###Dados do Jogo###")
        print(f"Nome do jogo: {self.name}")
        print(f"Ano de Lançamento: {self.yearLaunch}")
        print(f"Modo multiplayer?: {self.multiplayer}")
        print(f"Avaliação do Jogo: {self.note}\n")
        
    def evaluate(self, note):
        self.totalEvaluation += note
        self.evaluators += 1
        
    def average(self):
        print(f"Média do jogo {self.name}: {self.totalEvaluation / self.evaluators}")
    '''
    No método de classe, usamos o decorator @classmethod, e o 
    primeiro parâmetro deve ser 'cls' (representa a classe)

    Decorator -> Uma “função especial” que modifica ou estende o 
    comportamento de outra função/método
    '''
    @classmethod
    def print_total_games_stats(cls):
        print("####Estatísticas Gerais dos Jogos####")
        # cls.total_games -> Acessa variável da classe
        print(f"Total de jogos criados: {cls.total_games}")
        # Tenta usar método de instância (self) com classe (cls) 
        # que dá erro
        cls.average(cls)
        
game1 = Game("The Legend of Zelda", 2017, False, 9.5)
game2 = Game("Fortnite", 2017, True, 8.0)
game3 = Game("Red Dead Redemption 2", 2018, False, 10.0)

game1.technical_sheet()
game2.technical_sheet()
game1.evaluate(9.0)
game1.evaluate(7.5)
game2.evaluate(6.5)
game2.evaluate(7.5)

# Usando o método de classe
Game.print_total_games_stats()