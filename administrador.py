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
import livroClasse,autorClasse, usuarioClasse, alunoClasse
import bd, psycopg2


menuOpcoes = """
1- Cadastrar livro
2- Atualizar livro
3- Remover livro
4- Cadastrar autores
5- Atualizar autores
6- Remover autores
7- Cadastrar usuário
8- Remover usuário
9- Cadastrar empréstimo
10- Atualizar empréstimo
11- Remover empréstimo
"""
def opcaoEscolhida(numero):
    if numero == 1:
        cadastrarLivro()
    elif numero == 2:
        atualizarLivro()
    elif numero == 3:
        removerLivro()
    elif numero == 4:
        cadastrarAutor()
    elif numero == 5:
        atualizarAutor()
    elif numero == 6:
        removerAutor
    elif numero == 7:
        cadastrarUsuario()
    elif numero == 8:
        atualizarUsuario()
    elif numero == 9:
        removerUsuario()
        
        
def cadastrarLivro():
    isbn, titulo, ano, editora, qtdCopias, categoria = input("""
    Digite (separado por espaço) as seguintes informações do livro:
    ISNB, título, ano, editora, qtdCopias e categoria: 
    """).split()
    isbn, ano, qtdCopias = int(isbn), int(ano), int(qtdCopias)
    livro = livroClasse.Livro(isbn, titulo, ano, editora, qtdCopias, categoria)
    livro.cadastrarLivro()
    
def atualizarLivro():
    isbn = input("Digite o ISBN do livro que deseja atualizar: ")
    livro = livroClasse.Livro.retornarLivro(isbn)
    print("Informações atuais: ")
    print(livro)
        
    titulo, ano, editora, qtdCopias, categoria = input("""
    Digite (separado por espaço) as novas informações do livro:
    ISNB, título, ano, editora, qtdCopias e categoria: 
    """).split()
    livro.titulo, livro.ano, livro.editora, livro.qtdCopias, livro.categoria = titulo, ano, editora, qtdCopias, categoria
    livro.atualizarLivro()

def removerLivro():
    isbn = input("Digite o ISBN do livro que deseja remover: ")
    livroClasse.Livro.removerLivro(isbn)
    

def cadastrarAutor():
    nome, cpf, nacionalidade = input("""
    Digite (separado por espaço) as seguintes informações do autor:
    nome, cpf, nacionalidade: 
    """).split()
    autor = autorClasse.Autor(nome, cpf, nacionalidade)
    autor.cadastrarAutor()
    
def atualizarAutor():
    nomeAntigo = input("Digite o nome do autor que deseja atualizar: ")
    autor = autorClasse.Autor.retornarAutor(nomeAntigo)
    print("Informações atuais: ")
    print(autor)
    
    nomeNovo, cpf, nacionalidade = input("""
    Digite (separado por espaço) as novas informações do autor:
    nome, cpf e nacionalidade: 
    """).split()
    autor.nome, autor.cpf, autor.nacionalidade= nomeNovo, cpf, nacionalidade
    
    autor.atualizarAutor(nomeAntigo)
    
def removerAutor():
    print()
  
            
def cadastrarUsuario():
    # Obs: não deixar cadastrar alguém de um grupo do tipo errado (checar pela matricula)
    opcao = int(input("""
    Digite o grupo do usuário a ser cadastrado:
    1- Aluno
    2- Professor
    3- Outros Funcionários
    """))
        
    nickname, senha = input("""
    Digite (separado por espaço) as seguintes informações do livro:
    nickname, senha: 
    """).split()
        
    if opcao == 1:
        grupo = "aluno"
        opcao = input("""
                        Digite o tipo do usuário:
                        1- Autenticado
                        2- Não autenticado""")
        
    elif opcao == 2:
        grupo = "funcionario"
        opcao = input("""
                        Digite o tipo do usuário:
                        1- Autenticado
                        2- Não autenticado""")
        
    usuario = usuarioClasse.Usuario(nickname, senha, tipo, grupo)
    usuario.cadastrarUsuario()
        
def atualizarUsuario():
    nickname = input("Digite o nickname do usuario que deseja atualizar: ")
    usuario = usuarioClasse.Usuario.retornaInformacoesNickname(nickname)
    print("Informações atuais: ")
    print(usuario)
        
    nickname, senha, tipo = input("""
    Digite (separado por espaço) as novas informações do usuario:
    nickname, senha, tipo 
    """).split()
    usuario.atualizarUsuario(nickname, senha, tipo)
    
def removerUsuario():
    print()

    
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
    print()
    
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