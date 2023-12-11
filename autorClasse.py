import bd

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
            
            # Comando sql que pega as informacoes do livro (titulo, ano, editora, qtdCopias, categoria) 
            sql = "SELECT cpf, nacionalidade FROM Autores WHERE nome = %s"
            values = (nome,)
            try:  
                with conn.cursor() as cursor:
                    cursor.execute(sql, values)
                    resultado = cursor.fetchone()
                    conn.commit()
            except Exception as e:
                    print(f"Erro ao executar comando SQL: {e}")
            finally:
                conn.close()
                
            return cls(nome, resultado[0], resultado[1]) 
        except:
            print("Autor não encontrado na biblioteca!")
     
    @staticmethod
    def retornaIdAutor(nome):
        # Conectando ao banco
            conn = bd.conexao()
            if conn == None:
                return
            
            # Comando sql que pega as informacoes do livro (titulo, ano, editora, qtdCopias, categoria) 
            sql = "SELECT idAutores FROM Autores WHERE nome = %s"
            values = (nome,)
            try:  
                with conn.cursor() as cursor:
                    cursor.execute(sql, values)
                    resultado = cursor.fetchone()
                    conn.commit()
            except Exception as e:
                    print(f"Erro ao executar comando SQL: {e}")
            finally:
                conn.close()
                
            return resultado[0]
                  
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
                    autor = Autor(idAutor, nome, cpf, nacionalidade)
                    livros = livros.split(',') if livros else []
                    autores.append((autor, livros))
                # return autores
                return autores
            
        except Exception as e:
            print(f"Erro ao buscar autores: {e}")
        finally:
            conn.close()
    
    def cadastrarAutor(self):
        conn = bd.conexao()
        if conn == None:
            return
        
        # Comando sql que cadastra autor
        sql = "INSERT INTO Autores (nome, cpf, nacionalidade) VALUES (%s, %s, %s)"
        values = (self.nome, self.cpf, self.nacionalidade)  
        try:
            with conn.cursor() as cursor:
                cursor.execute(sql, values)
                conn.commit()
                
        except Exception as e:
            print(f"Erro ao executar comando SQL: {e}")
        finally:
            conn.close()
            
    def atualizarAutor(self, nomeAntigo):
        # Conectando ao banco
        conn = bd.conexao()
        if conn == None:
            return
        # Comando sql que busca pelo "nomeantigo" e atualiza as informações do autor
        sql = "UPDATE Autores SET nome = %s, cpf = %s, nacionalidade = %s WHERE nome = %s"
        values = (self.nome, self.cpf, self.nacionalidade, nomeAntigo)  
        try:
            with conn.cursor() as cursor:
                cursor.execute(sql, values)
                conn.commit()
        except Exception as e:
            print(f"Erro ao executar comando SQL: {e}")
        finally:
            conn.close()