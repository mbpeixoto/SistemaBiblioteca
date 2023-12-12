# Comandos sql e métodos de um administrador

"""
– Cadastrar, atualizar e remover livros (Tabela livros + Livros_has_autores)
– Cadastrar, atualizar e remover autores (Tabela autores + tabela Livros_has_autores)

– Cadastrar, atualizar e remover usuários (Tabela usarios +  aluno ou funcionario+bibliotecario ou funcionario + professor ou funcionario):
A lógica aqui é verificar quem ele quer cadastrar no sistema (alunos ou funcionarios), ver se encontrar ou não, depois ver se já está ou não
cadastrado como usuário.
OBS: não foi pedido a funcionalidade de cadastrar alunos ou funcionários, logo isso irá partir de um banco de dados populado nessas tabelas.
Devo fazer as devidas checagem, exemplo  se tiver cadastrando um administrador não pode ser um aluno.

– Cadastrar, atualizar e remover empréstimos. (Livro.qtd + tabela emprestimos)
"""
import livroClasse,autorClasse, usuarioClasse, alunoClasse, funcionarioClasse
import bd


menuOpcoes = """
0- Para sair do programa
1- Cadastrar livro
2- Atualizar livro
3- Cadastrar autores
4- Atualizar autores
5- Cadastrar usuário
6- Atualizar usuário
7- Cadastrar empréstimo
8- Remover empréstimo
"""
def opcaoEscolhida(numero):
    if numero == 1:
        cadastrarLivro()
    elif numero == 2:
        atualizarLivro()
    elif numero == 3:
        cadastrarAutor()
    elif numero == 4:
        atualizarAutor()
    elif numero == 5:
        cadastrarUsuario()
    elif numero == 6:
        atualizarUsuario()
    elif numero == 7:
        cadastrarEmprestimo()      
    elif numero == 8:
        removerEmprestimo()
            
def cadastrarLivro():
    isbn, titulo, ano, editora, qtdCopias, categoria = input("""
Digite (separado por espaço) as seguintes informações do livro:
ISNB, título, ano, editora, qtdCopias e categoria: """).split()
    isbn, ano, qtdCopias = isbn, int(ano), int(qtdCopias)
    livro = livroClasse.Livro(isbn, titulo, ano, editora, qtdCopias, categoria)
    
    qtdAutores = int(input("Quantos autores tem o livro? "))
    nomesAutores = []
    for i in range(qtdAutores):
        nome = input(f"Digite o nome do {i+1} autor: ")
        nomesAutores.append(nome)
    
    idsAutores = []
    for nome in nomesAutores:
            idAutor = autorClasse.Autor.retornaIdAutor(nome)
            idsAutores.append(idAutor)
            
    livro.cadastrarLivro()
    livro.vincularLivroAutores(idsAutores)
    
    
def atualizarLivro():
    isbn = input("Digite o ISBN do livro que deseja atualizar: ")
    livro = livroClasse.Livro.retornarLivro(isbn)
    print("Informações atuais: ")
    print(livro)
        
    titulo, ano, editora, qtdCopias, categoria = input("""
    Digite (separado por espaço) as novas informações do livro:
    título, ano, editora, qtdCopias e categoria: """).split()
    livro.titulo, livro.ano, livro.editora, livro.qtdCopias, livro.categoria = titulo, ano, editora, qtdCopias, categoria
    livro.atualizarLivro()

def removerLivro():
    isbn = input("Digite o ISBN do livro que deseja remover: ")
    livroClasse.Livro.removerLivro(isbn)
    

def cadastrarAutor():
    nome, cpf, nacionalidade = input("""
Digite (separado por espaço) as seguintes informações do autor:
nome, cpf, nacionalidade: """).split()
    autor = autorClasse.Autor(nome, cpf, nacionalidade)
    autor.cadastrarAutor()
    
def atualizarAutor():
    nomeAntigo = input("Digite o nome do autor que deseja atualizar: ")
    autor = autorClasse.Autor.retornarAutor(nomeAntigo)
    print("Informações atuais: ")
    print(autor)
    
    nomeNovo, cpf, nacionalidade = input("""
Digite (separado por espaço) as novas informações do autor:
nome, cpf e nacionalidade: """).split()
    autor.nome, autor.cpf, autor.nacionalidade= nomeNovo, cpf, nacionalidade
    
    autor.atualizarAutor(nomeAntigo)
    
def removerAutor():
    print()  

            
def cadastrarUsuario():
    # Obs: não deixar cadastrar alguém de um grupo do tipo errado (checar pela matricula)
    opcao = int(input("""
    Digite o numero do grupo do usuário a ser cadastrado:
    1- Aluno
    2- Funcionarios
    """))
    
    matricula = input("""
    Digite o numero da matricula: 
    """)
    try:    
        if opcao == 1:
            tupla = alunoClasse.Aluno.retornaAluno(matricula)
            aluno, curso = tupla[0], tupla[1]
            print("Informações do aluno: ")
            print(aluno, curso)
            if aluno.idUsuario:
                print("Já é um usuário")
            else:
                grupo = "aluno"
                tipo = input("""
Digite o tipo do usuário: 
'autenticado' ou 'nao-autenticado' """)
                nickname, senha = input("""
Digite (separado por espaço) as seguintes informações do aluno:
nickname, senha: """).split()
                usuario = usuarioClasse.Usuario(nickname, senha, tipo, grupo)
                usuario.cadastrarUsuario()
                aluno.idUsuario = usuarioClasse.Usuario.retornarIdUsuario(nickname, senha)
                aluno.atualizarAlunoIdUsuario()
                    
        elif opcao == 2:
            funcionario = funcionarioClasse.Funcionario.retornaFuncionario(matricula)
            print("Informações do funcionário: ")
            print(funcionario)
            if funcionario.idUsuario:
                print("Já é um usuário")
            else:
                grupo = "funcionario"
                tipo = input("""
Digite o tipo do usuário:
'administrador', 'bibliotecario', 'autenticado' ou 'nao-autenticado': """)
                nickname, senha = input("""
Digite (separado por espaço) as seguintes informações do livro:
nickname, senha: """).split()
                usuario = usuarioClasse.Usuario(nickname, senha, tipo, grupo)
                usuario.cadastrarUsuario()
                funcionario.idUsuario = usuarioClasse.Usuario.retornarIdUsuario(nickname, senha)
                funcionario.atualizarFuncionarioIdUsuario()
                
    except:
        print("Erro ao cadastrar usuário")
        
        
def atualizarUsuario():
    
    opcao = int(input("""
    Digite o numero do grupo do usuário a ser atualizado:
    1- Aluno
    2- Funcionarios
    """))
    
    matricula = input("""
    Digite o numero da matricula: 
    """)
    try:    
        if opcao == 1:
            tupla = alunoClasse.Aluno.retornaAluno(matricula)
            aluno, curso = tupla[0], tupla[1]
            print("Informações do aluno: ")
            print(aluno, curso)
            if not aluno.idUsuario:
                print("Não é um usuário")
            else:
                usuario = usuarioClasse.Usuario.retornaUsuarioPeloId(aluno.idUsuario)
                print("Informações atuais:")
                print(f"Nickname: {usuario.nickname}, Senha: {usuario.senha}, Tipo: {usuario.tipo}")
                
                nickname, senha, tipo = input("""
Digite (separado por espaço) as novas informações do usuario: 
nickname, senha, tipo """).split()
                usuario.nickname, usuario.senha, usuario.tipo = nickname, senha, tipo
                usuario.atualizarUsuario(aluno.idUsuario)
                    
        elif opcao == 2:
            funcionario = funcionarioClasse.Funcionario.retornaFuncionario(matricula)
            if not funcionario.idUsuario:
                print("Não é um usuário")
            else:
                usuario = usuarioClasse.Usuario.retornaUsuarioPeloId(funcionario.idUsuario)
                print("Informações atuais:")
                print(f"Nickname: {usuario.nickname}, Senha: {usuario.senha}, Tipo: {usuario.tipo}")
                
                nickname, senha, tipo = input("""
Digite (separado por espaço) as novas informações do usuario: 
nickname, senha, tipo """).split()
                usuario.nickname, usuario.senha, usuario.tipo = nickname, senha, tipo
                usuario.atualizarUsuario(funcionario.idUsuario)
                
    except:
        print("Erro ao atualizar usuário")
    
    
def removerUsuario():
    print()

   
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
        sql = "DELETE FROM Livros_has_usuarios WHERE livros_isbn = %s AND usuarios_idusuario = %s"
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