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
            # Conectando ao banco
            conn = bd.conexao()
            if conn is None:
                return None
            
            # Comando SQL para recuperar as informações do aluno pela matrícula
            sql = "SELECT nome, dataIngresso, dataPrevisaoConclusao, Usuarios_idUsuarios, Cursos_idCurso FROM aluno WHERE matriculaAluno = %s"
            
            with conn.cursor() as cursor:
                cursor.execute(sql, (matricula,))
                resultado = cursor.fetchone()
                
                if resultado:
                    nome, dataIngresso, dataPrevisaoConclusao, idUsuario, curso = resultado[0], resultado[1], resultado[2], resultado[3], resultado[4]
                    return cls(matricula, nome, dataIngresso, dataPrevisaoConclusao, idUsuario, curso)
                else:
                    return None             
        except Exception as e:
            print(f"Erro ao recuperar aluno: {e}")
        finally:
            conn.close()
            
    def __str__(self):
        # Pego o nome da classe e depois uma lista de chave e valores dos atributos
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"   