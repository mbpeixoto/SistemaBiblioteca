import bd, psycopg2

class Livro():
    def __init__(self, isbn, titulo, ano, editora, qtdCopias, categoria):
        self.isbn = isbn
        self.titulo = titulo
        self.ano = ano
        self.editora = editora
        self.qtdCopias = qtdCopias
        self.categoria = categoria
    
    def cadastrarLivro(self):
        try:
            conn = bd.conexao()
            if conn == None:
                return
            # Comando sql que cadastra livro
            conn.close()
        except:
            print("Erro ao cadastrar livro")
        else:
            print("Livro cadastrado com sucesso")
    
    @classmethod
    def retornarLivro(cls, isbn):
        try:
            # Conectando ao banco
            conn = bd.conexao()
            if conn == None:
                return
            
            # Comando sql que pega as informacoes do livro (titulo, ano, editora, qtdCopias, categoria)
            
            conn.close()
            # return cls(isbn) 
        except:
            print("Livro não encontrado na biblioteca!")
            
    
    @staticmethod    
    def retornarTodosLivros():
        try:
            # Conectando ao banco
            conn = bd.conexao()
            if conn == None:
                return
            # Comando usql que retorna informacoes de todos livros e o nome do autor.
            print()
            # Guarde cada resultado e seu autor em uma lista de tuplas (livro, autores) chamada "resultados".
            # Sendo livro um objeto do da classe Livro e autores uma lista dos nomes.
            
            conn.close()
            # retorne "resultados" que é a (lista de tuplas)
        except:
            print("Error ao buscar livros")
                
    def atualizarLivro(self):
        try:
            # Conectando ao banco
            conn = bd.conexao()
            if conn == None:
                return
            # Comando sql que busca pelo "self.isbn" e atualiza as demais informações (titulo, ano, editora, qtdCopias, categoria)
            conn.close()
        except:
            print("Erro ao atualizar livro")
    
    @staticmethod            
    def removerLivro(isbn):
        try:
            # Conectando ao banco
            conn = bd.conexao()
            if conn == None:
                return
            # Comando sql que remove livro pelo isbn (devemos remover das demais tabelas relacionadas)
            conn.close()
        except:
            print("Erro ao remover livro")
        else:
            print("Livro removido com sucesso")
            
    def __str__(self):
        # Pego o nome da classe e depois uma lista de chave e valores dos atributos
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"