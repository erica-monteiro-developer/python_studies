'''
Classe abstrata e uma classe base para outras classes.
- Cria uma uma estrutura mínima, um esqueleto que todas as outras
subclasses devem seguir, como se fosse um contrato
- Não pode ser instanciada diretamente
- Pode ser métodos abstratos, ou seja, métodos sem implementação,
que devem ser obrigatoriamente implementados pelas subclasses.

ABC -> Abtract Base Class - não pode ser instanciada diretamnete


@abstractmethod -> força todas as subclasses a implementarem o
método aplicar_descontos

pass -> instrução nula, nãp faz nada, apenas preenche o corpo 
de blocos de código obrigatórios que ainda não foram 
implementados
'''

from abc import ABC, abstractmethod

class ItemBiblioteca(ABC):
    def __init__(self, titulo, autor, preco):
        self._titulo = titulo
        self._autor = autor
        self._preco = preco
    

    @abstractmethod
    def aplicar_desconto(self):
        pass