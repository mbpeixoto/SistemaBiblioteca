import bd, psycopg2

class Autor:
    def __init__(self, nome, cpf, nacionalidade):
        self.nome = nome
        self.cpf = cpf
        self.nacionalidade = nacionalidade
     
    @classmethod
    def retornarAutor(cls, nome):
        try:
            # Conectando ao banco
            conn = bd.conexao()
            if conn == None:
                return
            
            # Comando sql que pega as informacoes do autor (nome, cpf, nacionalidade)
            # pelo nome
            conn.close()
            # return cls(nome, cpf, nacionalidade) 
        except:
            print("Autor não encontrado na biblioteca!")
               
    @staticmethod    
    def retornaTodosAutores():
        try:
            # Comando usql que retorna informacoes de todos autores e os nomes de seus livros.
            print()
            # Guarde cada autor em uma lista de objetos do tipo Autor e retorne essa lista (autores[])
            
            # return autores
        except:
            print("Error ao buscar autores")
    
    def cadastrarAutor(self):
        try:
            conn = bd.conexao()
            if conn == None:
                return
            # Comando sql que cadastra autor
            conn.close()
        except:
            print("Erro ao cadastrar livro")
        else:
            print("Livro cadastrado com sucesso")
            
    def atualizarAutor(self, nomeAntigo):
        try:
            # Conectando ao banco
            conn = bd.conexao()
            if conn == None:
                return
            # Comando sql que pelo nomeAntigo atualiza as demais 
            # informacoes (self.nome, self.cpf e self.nacionalidade)
            
            conn.close()
        except:
            print("Erro ao atualizar autor")