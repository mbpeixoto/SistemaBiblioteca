# Operações e métodos de um autenticado
import livroClasse, autorClasse
import bd, psycopg2

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
    elif numero == 3:
        consultarEmprestimos()
    elif numero == 4:
        consultarReservas()
    elif numero == 5:
        realizarReserva()

def consultarLivros():
    livros = livroClasse.Livro.retornarTodosLivros() 
    for livro in livros:
        print(livro)

def consultarAutores():
    autores = autorClasse.Autor.retornaTodosAutores() 
    for autor in autores:
        print(autor)
        
def consultarEmprestimos():
    
    # Conectando ao banco
        conn = bd.conexao()
        if conn == None:
            return
        # sql que remove um livro da tabela emprestimo pelo isbn e aluno.idUsuario
        conn.close()
    
def consultarReservas():
    print()
    
def realizarReserva():
    print()