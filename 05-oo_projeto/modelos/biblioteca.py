# Classe instanciada no GET da classe Biblioteca
from modelos.avaliacao import Avaliacao
# Classe Abstrata
from modelos.itens.item_biblioteca import ItemBiblioteca

class Biblioteca:
    bibliotecas = []
    def __init__(self, nome):
        # _ -> atributo é "protegido" ou "privado". É uma 
        # convenção, não uma regra rígida
        # não se deve acessar esse atributo diretamente de fora 
        # da classe.
        self.nome = nome
        self._ativo = False
        self._avaliacao = []
        self._itens = []
        # self no append -> adicione essa instância atual da 
        # classe (representada por self) à lista de bibliotecas 
        # da classe 
        Biblioteca.bibliotecas.append(self)
        
    def __str__(self):
        return self.nome
    
    @classmethod
    def listar_bibliotecas(cls):
        # ljust ->  alinha o texto à esquerda, preenchendo com 
        # espaços até o tamanho desejado
        print(f"{'Nome da biblioteca'.ljust(25)} | {'Nota média'.ljust(25)} | {'Status'}")
        for biblioteca in Biblioteca.bibliotecas:
            print(f"{biblioteca.nome.ljust(25)} | {str(biblioteca.media_avaliacoes).ljust(25)} {biblioteca.ativo}")
    
    def alterna_estado(self):
        self._ativo = not self._ativo

    '''
    O Encapsulamento visa proteger informações que sejam 
    importantes, para que elas não possam ser alteradas 
    diretamente. Analogia: como a capsula de um remédio protege 
    a pessoa de sentir o gosto amargo do pózinho, ou mesmo que 
    aquilo agrida a garganta , paladar, enfim.

    Getter (get) → método usado para acessar um atributo 
    “privado”.

    Setter (set) → método usado para modificar um atributo 
    “privado”.

    Em Python, usamos os decoradores @property e @nome.setter.
    'nome' deve ser o nome do atributo que quero manipular

    '''   
    @property
    def ativo(self):
       return "ativada" if self._ativo else "desativada" 
   
    def receber_avaliacao(self, cliente, nota):
        # gerando instancia da classe Avaliação
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)
    
    @property    
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'
        soma = sum(avaliacao._nota for avaliacao in self._avaliacao)
        # round(numero, casas_decimais) -> arredonda numeros
        media = round(soma / len(self._avaliacao), 1)
        return media
    
    def adicionar_item(self, item):
        if isinstance(item, ItemBiblioteca):
            self._itens.append(item)

    def exibir_itens(self):
        print(f"Itens da Biblioteca {self.nome}\n")
        # enumerate -> função que permite iterar sobre uma lista 
        # ao mesmo tempo em que gera um contador automático
        for i, item in enumerate(self._itens, start=1):
            if hasattr(item, "isbn"):
                msg_livro = f"{i}. (Livro) -> Título: {item._titulo} | Autor: {item._autor} | Preço: {item._preco} | ISBN: {item.isbn}"
                print(msg_livro)
            else: 
                msg_revista = f"{i}. (Revista) -> Título: {item._titulo} | Autor: {item._autor} | Preço: {item._preco} | Edição: {item.edicao}"
                print(msg_revista)

'''
vars() -> retorna o dicionário __dict__ de uma objeto.
'''