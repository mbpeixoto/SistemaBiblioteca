import bd

class Aluno():
    def __init__(self, matricula, nome, dataIngresso, dataPrevisaoConclusao, idUsuario):
        self.matricula = matricula
        self.nome = nome
        self.dataIngresso = dataIngresso
        self.dataPrevisaoConclusao = dataPrevisaoConclusao
        self.idUsuario = idUsuario
    
    @classmethod
    def retornaAluno(cls, matricula):
        try:
            # Comando sql que recupera as informacoes dos aluno pela matricula
            # return cls(matricula, nome, dataIngresso, dataPrevisaoConclusao, idUsuario)
            print()
        except:
            print("Error ao achar aluno")
    
    def atualizarAlunoIdUsuario(self):
        # Conectando ao banco
        conn = bd.conexao()
        if conn == None:
            return
            # Comando sql 
        sql = "UPDATE Alunos SET Usuarios_idUsuario = %d WHERE matricula = %d"
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