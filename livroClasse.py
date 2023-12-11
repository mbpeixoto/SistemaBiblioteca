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
        try:
            conn = bd.conexao()
            if conn == None:
                return
            # Comando sql que cadastra livro
            sql = "INSERT INTO Livros (titulo, ano, editora, qtdCopias, categoria) VALUES (%s, %d, %s, %d, %s)"
            values = (self.titulo, self.ano, self.editora, self.qtdCopias, self.categoria)  
            try:
                with conn.cursor() as cursor:
                    cursor.execute(sql, values)
                    conn.commit()
            except Exception as e:
                    print(f"Erro ao executar comando SQL: {e}")
            finally:
                conn.close()
        except:
            print("Erro ao cadastrar livro")
        else:
            print("Livro cadastrado com sucesso")
    
    def vincularLivroAutores(self, autores):
        conn = bd.conexao()
        if conn == None:
            return
        for autor in autores:
            idAutor = autorClasse.retornaIdAutor(autor)
            
            sql = "INSERT INTO Livros_has_Autores (Livros_ISBN, Autores_idAutores) VALUES (%d, %s)"
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
            sql = "SELECT titulo, ano, editora, qtdCopias, categoria FROM Livros SET WHERE ISBN = %d"
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
                SELECT Livros.isbn, Livros.titulo, Livros.ano, Livros.editora, Livros.qtdCopias, Livros.categoria, GROUP_CONCAT(Autores.nome) as autores
                FROM Livros
                LEFT JOIN Livro_has_Autores ON Livros.isbn = Livro_has_Autores.Livros_ISBN
                LEFT JOIN Autores ON Livro_has_Autores.Autores_IdAutores = Autores.idAutores
                GROUP BY Livros.isbn
            """
            
            # Guarde cada resultado e seu autor em uma lista de tuplas (livro, autores) chamada "resultados".
            # Sendo livro um objeto do da classe Livro e autores uma lista dos nomes.
            with conn.cursor() as cursor:
                cursor.execute(sql)
                resultados = []

                for row in cursor.fetchall():
                    isbn, titulo, ano, editora, qtdCopias, categoria, autores = row
                    livro = cls(isbn, titulo, ano, editora, qtdCopias, categoria)
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
            sql = "UPDATE Livros SET titulo = %s, ano = %d, editora = %s, qtdCopias = %d, categoria = %s WHERE ISBN = %d"
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