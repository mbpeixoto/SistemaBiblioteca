import livroClasse, autorClasse

menuOpcoes = """
0- Para sair do programa
1- Consultar livros
2- Consultar autores
"""
def opcaoEscolhida(numero):
    if numero == 1:
        consultarLivros()
    elif numero == 2:
        consultarAutores()

def consultarLivros():
    livros = livroClasse.Livro.retornarTodosLivros() 
    for livro in livros:
        print(livro[0], livro[1])

def consultarAutores():
    autores = autorClasse.Autor.retornaTodosAutores() 
    for autor in autores:
        print(autor[0], autor[1])