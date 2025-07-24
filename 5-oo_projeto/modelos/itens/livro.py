'''
modelos -> pacote base
itens -> subpacote
arquivo (módulo) -> item_biblioteca.py
'''
from modelos.itens.item_biblioteca import ItemBiblioteca

class Livro(ItemBiblioteca):
    def __init__(self, titulo, autor, preco, isbn):
        super().__init__(titulo, autor, preco) # chama o construtor da classe abstrata
        self.isbn = isbn #  # funcionalidade nova adicionada na subclasse
        
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.10) # 10% de desconto