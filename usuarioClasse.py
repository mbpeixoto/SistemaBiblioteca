class Usuario():
    def __init__(self,nickname, senha, tipo, grupo ):
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
    
    @staticmethod
    def cadastrarUsuario(nickname, senha, tipo, grupo):
        try:
            # Comando sql que cadastra usuário
            print()
        except:
            print("Erro ao cadastrar usuario")
            
    @classmethod     
    def retornaInformacoesNickname(cls, nicknameFornecido): # Somente administrador usará esse método
        try:
            # Dois comandos sql: 
            # 1- retornar
            nickname, senha, tipo, grupo = "Comando sql que retorna dados do usuario (idUsuario, senha, tipo, grupo) para o nickname fornecido"
            return cls(nickname, senha, tipo, grupo) 
        except:
            print("Nickname de usuário não encontrado")
                
    def atualizarUsuario(self, nickname, senha, tipo):
        try:
            self.nickname, self.senha, self.tipo, self.grupo = nickname
            
            # Comando sql que cadastra usuário
            print()
        except:
            print("Erro ao cadastrar usuário")
                
    def removerUsuario(self):
        try:
            # Comando sql que remove usuário
            print()
        except:
            print("Error ao remover usuário")
            
    def __str__(self):
        # Pego o nome da classe e depois uma lista de chave e valores dos atributos
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"