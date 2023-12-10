"""
Esse será o arquivo do programa que vai conter:
1- Interface com o usuário
2- Irá importar os outros arquivos
"""
from pyfiglet import Figlet
import time
import usuarioClasse
import administrador, bibliotecario, autenticado, naoautenticado

# Login e autenticação

# Menu de opcoes de acordo com o tipo de usuario (administrador, bibliotecario, autenticado e nao autenticado)

# De acordo com a escolha chamar os métodos dos outros arquivos

try:
    print("---------------------------------------------------------------------------")
    f = Figlet(font='slant')
    print(f.renderText('Super Biblioteca'), end="")
    print("---------------------------------------------------------------------------")
except:
    print("Sistema de informações biblioteca")

# login
tipo, grupo = None
while(1):
    try:
        time.sleep(1)
        print("LOGIN:") 
        nickname = input("Digite nickname: ")
        senha = input("Digite a senha: ")
        tipo, grupo = usuarioClasse.Usuario.login()
    except:
        continue
    else:
        break

if tipo == "administrador":
    while(True):
        print(administrador.menuOpcoes)
        numOpcao = int(input())
        if numOpcao == 0:
            break
        administrador.opcaoEscolhida(numOpcao)

elif tipo == "bibliotecario":
    while(True):
        print(bibliotecario.menuOpcoes)
        numOpcao = int(input())
        if numOpcao == 0:
            break
        bibliotecario.opcaoEscolhida(numOpcao)

if tipo == "autenticado":
    while(True):
        print(autenticado.menuOpcoes)
        numOpcao = int(input())
        if numOpcao == 0:
            break
        autenticado.opcaoEscolhida(numOpcao)

if tipo == "nao autenticado":
    while(True):
        print(naoautenticado.menuOpcoes)
        numOpcao = int(input())
        if numOpcao == 0:
            break
        naoautenticado.opcaoEscolhida(numOpcao)
    


