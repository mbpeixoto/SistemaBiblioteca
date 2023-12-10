# Comandos sql e métodos de um bibliotecario
import livroClasse, alunoClasse, funcionarioClasse
import bd, psycopg2

menuOpcoes = """
1- Cadastrar empréstimo
2- Atualizar empréstimo
3- Remover empréstimo
"""

def opcaoEscolhida(numero):
    if numero == 1:
        cadastrarEmprestimo()
    elif numero == 2:
        atualizarEmprestimo()
    elif numero == 3:
        removerEmprestimo()
        
    
def cadastrarEmprestimo():
    try:
        isbn = input("Digite o isbn do livro que deseja realizar o empréstimo: ")
        livro = livroClasse.Livro.retornarLivro(isbn)
        if livro.qtdCopias > 0:
            print("Para quem será realizado o empréstimo?")
            pessoa = input("Digite 'a' p/ aluno ou 'f' p/ funcionário")
            if pessoa == "a":
                matricula = int(input("Digite a matrícula do aluno: "))
                aluno = alunoClasse.Aluno.retornaAluno(matricula)
                # Conectando ao banco
                conn = bd.conexao()
                if conn == None:
                    return
                # sql que adiciona um livro a tabela emprestimo pelo isbn e aluno.idUsuario
                conn.close()
                
                livro.qtdCopias -= 1
                livro.atualizarLivro()
                
            elif pessoa == "f":
                matricula = int(input("Digite a matrícula do funcionário: "))
                funcionario = funcionarioClasse.Funcionario.retornaFuncionario(matricula)
                if funcionario.cargo == "professor":
                    # Conectando ao banco
                    conn = bd.conexao()
                    if conn == None:
                        return
                    # sql que adiciona um livro a tabela emprestimo pelo isbn e aluno.idUsuario
                    conn.close()
                    
                    livro.qtdCopias -= 1
                    livro.atualizarLivro()
                else:
                    print("Somente funcionário professores podem receber empréstimos de livros!")
            else:
                print("Opção inválida")
                
                              
    except:
        print("Erro ao cadastrar empréstimo")
    else:
        print("Empréstimo cadastrado com sucesso")

def atualizarEmprestimo():
    conn = bd.conexao()
    if conn == None:
        return

    conn.close()
    
def removerEmprestimo():
    isbn = input("Digite o isbn do livro a ser removido: ")
    livro = livroClasse.Livro.retornarLivro(isbn)
    
    print("Para quem será removido o empréstimo?")
    pessoa = input("Digite 'a' p/ aluno ou 'f' p/ funcionário")
    
    if pessoa == "a":
        matricula = int(input("Digite a matrícula do aluno: "))
        aluno = alunoClasse.Aluno.retornaAluno(matricula)
        
        # Conectando ao banco
        conn = bd.conexao()
        if conn == None:
            return
        # sql que remove um livro da tabela emprestimo pelo isbn e aluno.idUsuario
        conn.close()
                
        livro.qtdCopias += 1
        livro.atualizarLivro()
                
    elif pessoa == "f":
        matricula = int(input("Digite a matrícula do funcionário: "))
        funcionario = funcionarioClasse.Funcionario.retornaFuncionario(matricula)
        
        # Conectando ao banco
        conn = bd.conexao()
        if conn == None:
            return
        # sql que remove um livro da tabela emprestimo pelo isbn e funcionario.idUsuario
        conn.close()
        
        livro.qtdCopias += 1
        livro.atualizarLivro()
    else:
        print("Opção inválida")