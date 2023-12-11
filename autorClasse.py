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
            # Conectando ao banco
            conn = bd.conexao()
            if conn is None:
                return None
            # Comando usql que retorna informacoes de todos autores e os nomes de seus livros.
            sql = """
                SELECT Autores.idAutores, Autores.nome, Autores.cpf, Autores.nacionalidade, GROUP_CONCAT(Livros.titulo) as livros
                FROM Autores
                LEFT JOIN Livros_has_Autores ON Autores.idAutores = LivrosHasAutores.Autores_IdAutores
                LEFT JOIN Livros ON Livros_has_Autores.Livros_ISBN = Livros.ISBN
                GROUP BY Autores.idAutores
            """

            # Guarde cada autor em uma lista de objetos do tipo Autor e retorne essa lista (autores[])
            with conn.cursor() as cursor:
                cursor.execute(sql)
                autores = []

                for row in cursor.fetchall():
                    idAutor, nome, cpf, nacionalidade, livros = row
                    autor = cls(idAutor, nome, cpf, nacionalidade)
                    livros = livros.split(',') if livros else []
                    autores.append((autor, livros))
                # return autores
                return autores
            
        except Exception as e:
            print(f"Erro ao buscar autores: {e}")
        finally:
            conn.close()
    
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