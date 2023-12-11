import bd

class Usuario():
    def __init__(self, nickname, senha, tipo, grupo ):
        self.nickname = nickname
        self.senha = senha
        self.tipo = tipo
        self.grupo = grupo
    
    @staticmethod   
    def login(cls, nicknameFornecido, senhaFornecida):
        try:
            # Dois comandos sql: 
            # 1- para autenticar o login com base no nickname e senha fornecidos
            senha, tipo, grupo = "Comando sql que retorna dados do usuario (nickname, senha, tipo, grupo) para o nickname fornecido"
            # Compara se a senha fornecida está correta
            if senha != senhaFornecida:
                print("Credenciais inválidas")
            else:
                # 2- retornar as demais informacoes (tipo, grupo)
                return  tipo, grupo
        except:
            print("Nickname de usuário não encontrado")
    
    def cadastrarUsuario(self):
        try:
            # Comando sql que cadastra usuário
            print()
        except:
            print("Erro ao cadastrar usuario")
    
    @staticmethod
    def retornarIdUsuario(nickname, senha):
        conn = bd.conexao()
        if conn == None:
            return
        # sql que adiciona um livro a tabela emprestimo pelo isbn e aluno.idUsuario
        sql = "SELECT idUsuario FROM Usuarios WHERE nickname = %s and senha = %s"
        values = (nickname, senha)  
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
         
    @classmethod     
    def retornaUsuarioPeloId(cls, idUsuario): # Somente administrador usará esse método
        conn = bd.conexao()
        if conn == None:
            return
        # sql que retorna o idUsuario pela matricula
        sql = "SELECT nickname, senha, tipo, grupo FROM Usuarios WHERE idUsuario = %d"
        values = (idUsuario,)
        try:
            with conn.cursor() as cursor:
                cursor.execute(sql, values)
                resultado = cursor.fetchone()
                conn.commit()
        except Exception as e:
            print(f"Erro ao executar comando SQL: {e}")
        finally:
            conn.close()
            return cls(resultado[0], resultado[1], resultado[2], resultado[3])
                
    def atualizarUsuario(self, idUsuario):
        # Conectando ao banco
            conn = bd.conexao()
            if conn == None:
                return
            # Comando sql 
            sql = "UPDATE Usuarios SET nickname = %s, senha = %s, tipo = %s WHERE idUsuario = %d"
            values = (self.nickname, self.senha, self.tipo, idUsuario)  
            try:
                with conn.cursor() as cursor:
                    cursor.execute(sql, values)
                    conn.commit()
            except Exception as e:
                    print(f"Erro ao executar comando SQL: {e}")
            finally:
                conn.close()
                
    def removerUsuario(self):
        try:
            # Comando sql que remove usuário
            print()
        except:
            print("Error ao remover usuário")
            
    def __str__(self):
        # Pego o nome da classe e depois uma lista de chave e valores dos atributos
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"