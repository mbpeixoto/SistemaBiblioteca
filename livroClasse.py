import bd
import autorClasse

class Livro():
    def __init__(self, isbn, titulo, ano, editora, qtdCopias, categoria):
        self.isbn = isbn
        self.titulo = titulo
        self.ano = ano
        self.editora = editora
        self.qtdCopias = qtdCopias
        self.categoria = categoria
    
    def cadastrarLivro(self):
        conn = bd.conexao()
        if conn == None:
            return
        # Comando sql que cadastra livro
        sql = "INSERT INTO Livros (isbn, titulo, ano, editora, qtdCopias, categoria) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (self.isbn, self.titulo, self.ano, self.editora, self.qtdCopias, self.categoria)  
        try:
            with conn.cursor() as cursor:
                cursor.execute(sql, values)
                conn.commit()
                print("Livro cadastrado com sucesso")
        except Exception as e:
            print(f"Erro ao executar comando SQL: {e}")
        finally:
            conn.close()
    
    def vincularLivroAutores(self, idsAutores):
        conn = bd.conexao()
        if conn == None:
            return
        for idAutor in idsAutores:
            sql = "INSERT INTO Livros_has_Autores (Livros_ISBN, Autores_idAutores) VALUES (%s, %s)"
            values = (self.isbn, idAutor)
            try:
                with conn.cursor() as cursor:
                    cursor.execute(sql, values)
                    conn.commit()
            except Exception as e:
                print(f"Erro ao executar comando SQL: {e}")
            finally:
                conn.close()
        
    @classmethod
    def retornarLivro(cls, isbn):
        try:
            # Conectando ao banco
            conn = bd.conexao()
            if conn == None:
                return
            
            # Comando sql que pega as informacoes do livro (titulo, ano, editora, qtdCopias, categoria) 
            sql = "SELECT titulo, ano, editora, qtdCopias, categoria FROM Livros SET WHERE ISBN = %s"
            values = (isbn,)
            try:  
                with conn.cursor() as cursor:
                    cursor.execute(sql, values)
                    resultado = cursor.fetchone()
                    conn.commit()
            except Exception as e:
                    print(f"Erro ao executar comando SQL: {e}")
            finally:
                conn.close()
                
            return cls(isbn, resultado[0], int(resultado[1]), resultado[2], int(resultado[3]), resultado[4])
        
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
            sql = """
                SELECT Livros.ISBN, Livros.titulo, Livros.ano, Livros.editora, Livros.qtdCopias, Livros.categoria, Autores.nome
                FROM Livros
                JOIN Livros_has_Autores ON Livros.ISBN = Livros_has_Autores.Livros_ISBN
                JOIN Autores ON Livros_has_Autores.Autores_IdAutores = Autores.idAutores
                GROUP BY Livros.ISBN, Autores.nome
            """
            
            # Guarde cada resultado e seu autor em uma lista de tuplas (livro, autores) chamada "resultados".
            # Sendo livro um objeto do da classe Livro e autores uma lista dos nomes.
            with conn.cursor() as cursor:
                cursor.execute(sql)
                resultados = []

                for row in cursor.fetchall():
                    isbn, titulo, ano, editora, qtdCopias, categoria, autores = row
                    livro = Livro(isbn, titulo, ano, editora, qtdCopias, categoria)
                    resultados.append((livro, autores.split(',')))

                return resultados
        except Exception as e:
            print(f"Erro ao buscar livros: {e}")
        finally:
            conn.close()
            # retorne "resultados" que é a (lista de tuplas)
                
    def atualizarLivro(self):
        try:
            # Conectando ao banco
            conn = bd.conexao()
            if conn == None:
                return
            # Comando sql que busca pelo "self.isbn" e atualiza as demais informações (titulo, ano, editora, qtdCopias, categoria)
            sql = "UPDATE Livros SET titulo = %s, ano = %s, editora = %s, qtdCopias = %s, categoria = %s WHERE ISBN = %s"
            values = (self.titulo, self.ano, self.editora, self.qtdCopias, self.categoria, self.isbn)  
            try:
                with conn.cursor() as cursor:
                    cursor.execute(sql, values)
                    conn.commit()
            except Exception as e:
                    print(f"Erro ao executar comando SQL: {e}")
            finally:
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