import datetime

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
        input("Pressione [Enter] para continuar...")
        clear()
    elif escolha == '2':
        clear()
        livro_nome = input("Digite o nome do livro: ")
        data = input("Digite a data do empréstimo (YYYY-MM-DD): ")
        livro = livros.buscar_livro(livro_nome)

        if not livro:
            print("Livro não encontrado")
            return

        users.emprestar(usuario_atual, data, livro)
        input("Pressione [Enter] para continuar...")
    elif escolha == '3':
        clear()
        print("Seus empréstimos:\n")

        hoje = datetime.today()

        for emp in usuario_atual['Emprestimos']:
            atraso = 0

            if hoje > emp['prazo']:
                atraso = (hoje - emp['prazo']).days

            multa = atraso * 1

            print(f"{emp['livro']['titulo']}")
            print(f"Data: {emp['data'].date()}")
            print(f"Prazo: {emp['prazo'].date()}")

            if multa > 0:
                print(f"Multa atual: R${multa}")
            else:
                print("Sem multa")

            print("-" * 20)
            input("Pressione [Enter] para continuar...")
            clear()

    elif escolha == '4':
        clear()
        livro_nome = input("Digite o nome do livro: ")
        livro = livros.buscar_livro(livro_nome)

        if not livro:
            print("Livro não encontrado")
            return

        for emp in usuario_atual['Emprestimos']:
            if emp['livro']['titulo'] == livro_nome:
                usuario_atual['Emprestimos'].remove(emp)
                livro['disponivel'] = True
                print("Livro devolvido com sucesso!")
                break
        else:
            print("Você não tem esse livro emprestado.")
        
        input("Pressione [Enter] para continuar...")

    elif escolha == '0':    
        clear()
        usuario_atual = None



while True:
    clear()
    print("===== MENU INICIAL =====")
    print('\n[1] - Fazer Login')
    print('[2] - Criar Conta')
    e = input("\nEscolha: ")

    if e == '1':
        print('=== Login ===')
        nome_usr = input("Digite seu nome de usuário: ")
        senha = input("Digite sua senha: ")
        usuario_atual = users.logar(nome_usr, senha)
        input("Pressione [Enter] para continuar...")
        clear()
        
    elif e == '2':
        print('=== Criar Conta ===')
        nome_usr = input("Digite seu nome de usuário: ")
        senha = input("Digite sua senha: ")
        users.criar_novo(nome_usr, senha)
        input("Pressione [Enter] para continuar...")
        clear()

    while usuario_atual:
        if usuario_atual == 'admin':
            menu_adm()
        else:
            menu_user()