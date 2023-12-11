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
            # Comando usql que retorna informacoes de todos autores e os nomes de seus livros.
            print()
            # Guarde cada autor em uma lista de objetos do tipo Autor e retorne essa lista (autores[])
            
            # return autores
        except:
            print("Error ao buscar autores")
    
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