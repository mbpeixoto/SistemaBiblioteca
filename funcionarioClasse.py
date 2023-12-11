import bd

class Funcionario():
    def __init__(self, matricula, cargo, idUsuario):
        self.matricula = matricula
        self.cargo = cargo
        self.idUsuario = idUsuario
    
    @classmethod
    def retornaFuncionario(cls, matricula):
        try:
            # Comando sql que recupera as informacoes do funcionario pela matricula
            # return cls(matricula, cargo, idUsuario)
            print()
        except:
            print("Error ao achar aluno")
    
    def atualizarFuncionarioIdUsuario(self):
        # Conectando ao banco
        conn = bd.conexao()
        if conn == None:
            return
            # Comando sql 
        sql = "UPDATE Funcionarios SET Usuarios_idUsuario = %d WHERE matricula = %d"
        values = (self.idUsuario, self.matricula)  
        try:
            with conn.cursor() as cursor:
                cursor.execute(sql, values)
                conn.commit()
        except Exception as e:
            print(f"Erro ao executar comando SQL: {e}")
        finally:
            conn.close()
                 
    def __str__(self):
        # Pego o nome da classe e depois uma lista de chave e valores dos atributos
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"