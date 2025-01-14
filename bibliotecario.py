# Comandos sql e métodos de um bibliotecario
import livroClasse, alunoClasse, funcionarioClasse
import bd

menuOpcoes = """
0- Para sair do programa
1- Cadastrar empréstimo
2- Remover empréstimo
"""

def opcaoEscolhida(numero):
    if numero == 1:
        cadastrarEmprestimo()
    elif numero == 2:
        removerEmprestimo()
        
    
def cadastrarEmprestimo():
    isbn = input("Digite o isbn do livro que deseja realizar o empréstimo: ")
    livro = livroClasse.Livro.retornarLivro(isbn)
    if livro.qtdCopias > 0:
        print("Para quem será realizado o empréstimo?")
        pessoa = input("Digite 'a' p/ aluno ou 'f' p/ funcionário: ")
        if pessoa == "a":
            matricula = input("Digite a matrícula do aluno: ")
            tupla = alunoClasse.Aluno.retornaAluno(matricula)
            aluno= tupla[0]
            # Conectando ao banco
            conn = bd.conexao()
            if conn == None:
                return
            # sql que adiciona um livro a tabela emprestimo pelo isbn e aluno.idUsuario
            sql = "INSERT INTO Livros_has_Usuarios (Livros_ISBN, Usuarios_idUsuario) VALUES (%s, %s)"
            values = (isbn, aluno.idUsuario) 
            try:
                with conn.cursor() as cursor:
                    cursor.execute(sql, values)
                    conn.commit()
                    livro.qtdCopias -= 1
                    livro.atualizarLivro()
                    print("Emprestimo realizado com sucesso")
            except Exception as e:
                    print(f"Erro ao realizar emprestimo: {e}")
            finally:
                    conn.close()
                
        elif pessoa == "f":
            matricula = input("Digite a matrícula do funcionário: ")
            funcionario = funcionarioClasse.Funcionario.retornaFuncionario(matricula)
            # Conectando ao banco
            conn = bd.conexao()
            if conn == None:
                return
            # sql que adiciona um livro a tabela emprestimo pelo isbn e aluno.idUsuario
            sql = "INSERT INTO Livros_has_Usuarios (Livros_ISBN, Usuarios_idUsuario) VALUES (%s, %s)"
            values = (isbn, funcionario.idUsuario)  
            try:
                with conn.cursor() as cursor:
                    cursor.execute(sql, values)
                    conn.commit()
                    livro.qtdCopias -= 1
                    livro.atualizarLivro()
                    print("Emprestimo realizado com sucesso")
            except Exception as e:
                    print(f"Erro ao realizar emprestimo: {e}")
            finally:
                conn.close()                    
        else:
            print("Opção inválida")

    
def removerEmprestimo():
    isbn = input("Digite o isbn do livro a ser removido: ")
    livro = livroClasse.Livro.retornarLivro(isbn)
    
    print("Para quem será removido o empréstimo?")
    pessoa = input("Digite 'a' p/ aluno ou 'f' p/ funcionário: ")
    
    if pessoa == "a":
        matricula = input("Digite a matrícula do aluno: ")
        tupla = alunoClasse.Aluno.retornaAluno(matricula)
        aluno= tupla[0]
        
        # Conectando ao banco
        conn = bd.conexao()
        if conn == None:
            return
        # sql que remove um livro da tabela emprestimo pelo isbn e aluno.idUsuario
        sql = "DELETE FROM Livros_has_usuarios WHERE livros_isbn = %s AND usuarios_idusuario = %s"
        values = (isbn, aluno.idUsuario)
            
        try:
            with conn.cursor() as cursor:
                    cursor.execute(sql, values)
                    conn.commit()
                    livro.qtdCopias += 1
                    livro.atualizarLivro()
                    print("Empréstimo removido com sucesso")
        except Exception as e:
                print(f"Erro ao remover empréstimo: {e}")
        finally:
            conn.close()
                
    elif pessoa == "f":
        matricula = input("Digite a matrícula do funcionário: ")
        funcionario = funcionarioClasse.Funcionario.retornaFuncionario(matricula)
        
        # Conectando ao banco
        conn = bd.conexao()
        if conn == None:
            return
        # sql que remove um livro da tabela emprestimo pelo isbn e funcionario.idUsuario
        sql = "DELETE FROM Livros_has_usuarios WHERE livros_isbn = %s usuarios_idusuario = %s"
        values = (isbn, funcionario.idUsuario)
            
        try:
            with conn.cursor() as cursor:
                cursor.execute(sql, values)
                conn.commit()
                livro.qtdCopias += 1
                livro.atualizarLivro()
                print("Empréstimo removido com sucesso")
        except Exception as e:
            print(f"Erro ao remover empréstimo: {e}")
        finally:
            conn.close()
            
    else:
        print("Opção inválida")