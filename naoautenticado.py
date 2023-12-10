import livroClasse, autorClasse

menuOpcoes = """
1- Consultar livros
2- Consultar autores
3- Consultar empréstimos
4- Consultar reserva
5- Realizar reserva
"""
def opcaoEscolhida(numero):
    if numero == 1:
        consultarLivros()
    elif numero == 2:
        consultarAutores()

def consultarLivros():
    livros = livroClasse.Livro.retornarTodosLivros() 
    for livro in livros:
        print(livro)

def consultarAutores():
    autores = autorClasse.Autor.retornaTodosAutores() 
    for autor in autores:
        print(autor)