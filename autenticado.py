# Operações e métodos de um autenticado
import livroClasse, autorClasse
import bd, psycopg2

menuOpcoes = """
0- Para sair do programa
1- Consultar livros
2- Consultar autores
3- Consultar empréstimos
"""
def opcaoEscolhida(numero):
    if numero == 1:
        consultarLivros()
    elif numero == 2:
        consultarAutores()
    elif numero == 3:
        consultarEmprestimos()
    #elif numero == 4:
        #consultarReservas()
    #elif numero == 5:
        #realizarReserva()

def consultarLivros():
    livros = livroClasse.Livro.retornarTodosLivros() 
    for livro in livros:
        print(livro[0], livro[1])

def consultarAutores():
    autores = autorClasse.Autor.retornaTodosAutores() 
    for autor in autores:
        print(autor[0], autor[1])
        
def consultarEmprestimos():
    
    try:
        # Conectando ao banco
        conn = bd.conexao()
        if conn is None:
            return
        
        # Comando SQL para consultar os empréstimos
        sql = "SELECT * FROM Livros_has_Usuarios"
        
        with conn.cursor() as cursor:
            cursor.execute(sql)
            emprestimos = cursor.fetchall()
            
            if emprestimos:
                # Exibindo os resultados (ajuste conforme sua necessidade)
                for emprestimo in emprestimos:
                    print(emprestimo)
            else:
                print("Nenhum empréstimo encontrado.")
    
    except Exception as e:
        print(f"Erro ao consultar empréstimos: {e}")
    finally:
        conn.close()
    