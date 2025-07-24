

from modelos.biblioteca import Biblioteca
from modelos.itens.livro import Livro
from modelos.itens.revista import Revista

biblioteca_cidade = Biblioteca("Biblioteca da Cidade")
biblioteca_shopping = Biblioteca("BIblioteca do Shopping")

livro1 = Livro("1984", "George Orwell", 30.0, "084-3245")
livro2 = Livro("Brave New WOrld", "Aldous Huxley", 25.0, "084-3245321")
revista1 = Revista("National Geographic", "John Doe", 15.0, "Quinta")

livro1.aplicar_desconto()
revista1.aplicar_desconto()

biblioteca_cidade.adicionar_item(livro1)
biblioteca_cidade.adicionar_item(revista1)
biblioteca_cidade.adicionar_item(livro2)

biblioteca_cidade.alterna_estado()
biblioteca_cidade.receber_avaliacao('Fulano', 8.5)
biblioteca_cidade.receber_avaliacao('Sicrano', 9.5)
biblioteca_cidade.receber_avaliacao('Sicrano', 6.5)

'''
A função main é a função principal que define o que o programa
deve fazer quando for executado diretamente.

if __name__ == "__main__" → executa o que está abaixo apenas se 
este arquivo for executado diretamente (via terminal, por 
exemplo),e **não** quando ele for importado por outro arquivo 
Python.

Quando executamos um arquivo .py, por baixo dos panos o Python 
atribui automaticamente o valor "__main__" à variável interna 
__name__ daquele script.

Se eu importar esse arquivo em outro lugar (ex: import app), o
__name__ **não será "__main__"**, será o nome do módulo 
(ex: "app"), então o bloco dentro do if não será executado.

Isso é útil para:
- Deixar o código mais organizado
- Permitir reuso sem rodar tudo automaticamente
-  if __name__ == "__main__" protege o script para que ele não
execute coisas automaticamente quando for importado.
'''
def main():
    # Biblioteca.listar_bibliotecas()
    biblioteca_cidade.exibir_itens()

if __name__ == "__main__":
    main()