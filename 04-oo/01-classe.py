'''
A programação orientada a objetos, é sem dúvida, um dos 
paradigmas mais importantes de qualquer linguagem de programação
e ela é muito utilizada em muitos projetos que se utiliza para 
desenvolvimento web e outros tipos de segmentos dentro das 
linguagens de programação. Portanto, é imprescindível ter 
conhecimento sobre esse paradigma.

Em cada aula será apresentado um dos pilares da orientação a 
objetos.

Uma classe nada mais é que um modelo que define como serão os 
objetos e dentro da classe vamos ter alguns atributos. Exemplo: 
numa loja de jogos online (como a Steam por ex.), uma imagem do 
produto seria um atributo, o título, o gênero, preço, enfim, 
todas essas características são um atributo. 

Então, quando um novo jogo é cadastrado na loja, eu tenho um 
objeto, é o produto real, final, feito a partir do molde 
(classe), uma instância daquela classe, e aí eu tenho que 
preencher os atributos definidos na classe.
'''
class Game:
    name = ""
    yearLaunch = 0 
    #multiplayer -> permite 2 ou mais pessoas jogarem juntas
    multiplayer = False
    note = 0