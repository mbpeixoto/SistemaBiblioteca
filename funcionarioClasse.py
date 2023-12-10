import bd, psycopg2

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
            
    def __str__(self):
        # Pego o nome da classe e depois uma lista de chave e valores dos atributos
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"