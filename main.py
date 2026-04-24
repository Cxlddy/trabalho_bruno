import os #chama os pra limpar a tela
from datetime import datetime #datetime para calcular os dias de atraso e a multa
from src.livros import Livros #importa a classe Livros do módulo src.livros
from src.usuarios import Usuarios #'' Usuarios do módulo src.usuarios
from database.database import dados #importa os dados do vetor contido em database, a fim de manipular os dados separadamente, com o intuito de melhorar a organização do projeto.

users = Usuarios() #chamada da classe para criar um objeto
livros = Livros() #''

usuario_atual = None #define o usuario como nome, funciona como uma espécie de status, para saber qual tipo de usuário está logado
 
def clear(): #função para limpar a tela, como grande parte dos computadores rodam Windows, fizemos uso do cls
    os.system('cls')

def menu_adm():
    global usuario_atual #fazendo uso da variável global para manipular o status do usuário logado
    clear()
    print("=== Menu do Admin ===")
    print("\n[1] - Adicionar Livro")
    print("[2] - Remover Livro")
    print("[3] - Listar Livros")
    print("[0] - Sair")
    escolha = input("\nEscolha: ")
    if escolha == '1': #estrutura simples de decisão para gerenciar as opções do menu
        clear()
        livro = input("Digite o nome do livro: ")
        livros.adicionar_livro(livro) #chamada do método da classe para adicionar um livro
        input("Pressione [Enter] para continuar...")
    elif escolha == '2':
        clear()
        livro = input("Digite o nome do livro: ")
        livros.remover_livro(livro) #'' para remover um livro
        input("Pressione [Enter] para continuar...")
    elif escolha == '3':
        clear()
        print(dados['livros']) #mostrando a lista completa de livros, com os dados importados do vetor
        input("Pressione [Enter] para continuar...")
        clear()
    elif escolha == '0':
        usuario_atual = None  
        clear()


def menu_user():
    global usuario_atual #mesma coisa do adm
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
        print(dados['livros']) #idêntico ao do menu do admin, mostrando o vetor completo
        input("Pressione [Enter] para continuar...")
        clear()
    elif escolha == '2':
        clear()
        livro_nome = input("Digite o nome do livro: ") #solicitação do nome do livro para pegar o empréstimo
        data = input("Digite a data do empréstimo (YYYY-MM-DD): ") #solicitação da data, está sendo feito assim para calcularmos a multa caso a tenha, caso contrário seria necessário passar os dias
        livro = livros.buscar_livro(livro_nome) #chamada do método para buscar o livro por nome
        if not livro:
            print("Livro não encontrado")
            return
        users.emprestar(usuario_atual, data, livro) #chamada do método do empréstimo
        input("Pressione [Enter] para continuar...")
    elif escolha == '3':
        clear()
        print("Seus empréstimos:\n")

        hoje = datetime.today()  #importação do dia de hoje para calcular o atraso
        for emp in usuario_atual['Emprestimos']: #laço lógico para mostrar os empréstimos e calcular a multa, se hoje for maior que o prazo do empréstimo, o atraso é cobrado com R$1 por cada dia atrasado
            atraso = 0
            if hoje > emp['prazo']:
                atraso = (hoje - emp['prazo']).days #conta dos dias de atraso, subtraindo a data de hoje do prazo da entrega do livro, e pegando apenas os dias
            multa = atraso * 1 #calculo da multa, bem simples
            print(f"{emp['livro']['titulo']}")
            print(f"Data: {emp['data'].date()}")
            print(f"Prazo: {emp['prazo'].date()}")
            if multa > 0: #se multa maior que zero, mostra multa
                print(f"Multa atual: R${multa}")
            else:
                print("Sem multa")
            print("-" * 20) #linha de separação para vizualização melhor
            input("Pressione [Enter] para continuar...")
            clear()

    elif escolha == '4':
        clear()
        livro_nome = input("Digite o nome do livro: ") #solicitacao do nome do livro para devolução
        livro = livros.buscar_livro(livro_nome) #chamada do método de busca
        if not livro: #se o livro não for encontrado, mostra mensagem de erro
            print("Livro não encontrado")
            return
        for emp in usuario_atual['Emprestimos']: #para cada empréstimo do usuário, se o título for igual, remove, deixa como disponível e mostra mensagem de sucesso
            if emp['livro']['titulo'] == livro_nome:
                usuario_atual['Emprestimos'].remove(emp)
                livro['disponivel'] = True
                print("Livro devolvido com sucesso!")
                break
        else:
            print("Você não tem esse livro emprestado.")        
        input("Pressione [Enter] para continuar...")
        clear()
    elif escolha == '0':    
        clear()
        usuario_atual = None  


while True: #loop para manter o programa rodando, apenas mostra coisas visuais, evitamos colocar lógica
    clear()
    print("===== MENU INICIAL =====")
    print('\n[1] - Fazer Login')
    print('[2] - Criar Conta')
    e = input("\nEscolha: ")

    if e == '1':
        print('=== Login ===')
        nome_usr = input("Digite seu nome de usuário: ")
        senha = input("Digite sua senha: ")
        usuario_atual = users.logar(nome_usr, senha) #chamada do método de login
        input("Pressione [Enter] para continuar...")
        clear()
        
    elif e == '2':
        print('=== Criar Conta ===')
        nome_usr = input("Digite seu nome de usuário: ")
        senha = input("Digite sua senha: ")
        users.criar_novo(nome_usr, senha) #chamada do método para criar um novo usuário, o tipo é definido como user por padrão
        input("Pressione [Enter] para continuar...")
        clear()

    while usuario_atual:
        if usuario_atual.get('tipo') == 'admin': #comparando o tipo do usuário logado, se for admin, mostra o menu do admin, se for user, mostra o menu do user
            menu_adm()
        else:
            menu_user()