import bd

class Funcionario():
    def __init__(self, matricula, cargo, idUsuario):
        self.matricula = matricula
        self.cargo = cargo
        self.idUsuario = idUsuario
    
    def atualizarFuncionarioIdUsuario(self):
        try:
            # Conectando ao banco
            conn = bd.conexao()
            if conn is None:
                return

            with conn.cursor() as cursor:
                sql_atualizar_aluno = "UPDATE Funcionarios SET Usuarios_idUsuario = %s WHERE matriculaFuncionario = %s"
                cursor.execute(sql_atualizar_aluno, (self.idUsuario, self.matricula))

            # Confirmar a transação
            conn.commit()

            print("Funcionário adicionado ao sistema da biblioteca!")

        except Exception as e:
            print(f"Erro ao adicionar funcionário ao sistema da biblioteca: {e}")
        finally:
            # Fechar a conexão
            conn.close()
            
    @classmethod
    def retornaFuncionario(cls, matricula):
        try:
            # Conectando ao banco
            conn = bd.conexao()
            if conn is None:
                return None
            
            # Comando SQL para recuperar as informações do funcionário pela matrícula
            sql = "SELECT cargo, Usuarios_idUsuario FROM funcionarios WHERE matriculaFuncionario = %s"
            
            with conn.cursor() as cursor:
                cursor.execute(sql, (matricula,))
                resultado = cursor.fetchone()
                
                if resultado:
                    cargo, idUsuario = resultado[0], resultado[1]
                    return cls(matricula, cargo, idUsuario)
                else:
                    return None
        except Exception as e:
            print(f"Erro ao recuperar funcionário: {e}")
        finally:
            conn.close()
            
    def __str__(self):
        # Pego o nome da classe e depois uma lista de chave e valores dos atributos
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"