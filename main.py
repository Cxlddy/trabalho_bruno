from src.livros import Livros
from src.usuarios import Usuarios
from database.database import dados
import os

users = Usuarios()
livros = Livros()

usuario_atual = None

def clear():
    os.system('cls')

def  menu_adm():
    clear()
    print("=== Menu do Admin ===")
    print("\n[1] - Adicionar Livro")
    print("[2] - Remover Livro")
    print("[3] - Listar Livros")
    print("[0] - Sair")
    escolha = input("\nEscolha: ")
    if escolha == '1':
        clear()
        livro = input("Digite o nome do livro: ")
        livros.adicionar_livro(livro)
        input("Pressione [Enter] para continuar...")
    elif escolha == '2':
        clear()
        livro = input("Digite o nome do livro: ")
        livros.adicionar_livro()
        input("Pressione [Enter] para continuar...")
    elif escolha == '3':
        clear()
        print(dados['livros'])
    elif escolha == '0':
        usuario_atual = None
        clear()


def menu_user():
    clear()
    print("=== Menu do Usuário ===")
    print('\n[1] - Listar Livros')
    print('[2] - Pegar empréstimos')
    print('[3] - Ver empréstimos')
    print('[4] - Devolver livro')
    print('[0] - Sair')
    escolha = input(("\nEscolha: "))

    if escolha == '1':
        clear()
        print(dados['livros'])
    elif escolha == '2':
        clear()
        print("Digite o nome do livro que deseja emprestar: ")
        livro = input()
        users.emprestar(usuario_atual, livro)
        input("Pressione [Enter] para continuar...")
    elif escolha == '3':
        clear()
        print('Digite seu nome de usuário:')
        u = input()

        for user in dados['usuarios']:
            if user['nome'] == u:
                print(user['Emprestimos'])
        input("Pressione [Enter] para continuar...")
    elif escolha == '4':
        users.devolver(usuario_atual, livro)
        input("Pressione [Enter] para continuar...")
    elif escolha == '0':
        clear()
        usuario_atual = None



while True:
    print("===== MENU INICIAL =====")
    print('\n[1] - Fazer Login')
    print('\n[2] - Criar Conta')
    e = input("\nEscolha: ")

    if e == '1':
        print('=== Login ===')
        nome_usr = input("Digite seu nome de usuário: ")
        senha = input("Digite sua senha: ")
        users.logar(nome_usr, senha)
