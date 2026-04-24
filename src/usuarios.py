from database.database import dados
from datetime import date, datetime, timedelta
date = date.today() #importação do dia de hoje para calcular o atraso

class Usuarios(): #classe do gerenciamento dos usuários

    def __init__(self):
        self.usuarios = dados['usuarios']

    def criar_novo(self, nome_usr, senha): #método para criar um novo usuário

        novo = {
            'nome': nome_usr,
            'senha': senha,
            'tipo' : 'usuario',
            'Emprestimos' : [],
        }

        self.usuarios.append(novo)

    def logar(self, nome_usr, senha): #método para login

        for usuario in self.usuarios: #para cada usuário na lista, se o nome e senha forem iguais, mostra mensagem de sucesso e retorna o usuario logado

            if usuario['nome'] == nome_usr and usuario['senha'] == senha:
                print(f"Logado com sucesso, seja bem vindo, {nome_usr}")
                return usuario
        
        print("Nome ou senha incorreto(s)")
        return None
    
    def emprestar(self, usuario, data, livro): #método para emprestar um livro

        if not livro['disponivel']: #se o livro não estiver disponível, mostra mensagem de erro e retorna falso
            print('Livro já emprestado!')
            return False

        data_obj = datetime.strptime(data, "%Y-%m-%d")
        prazo = data_obj + timedelta(days=7)

        livro['disponivel'] = False

        usuario['Emprestimos'].append({
            'data': data_obj,
            'prazo': prazo,
            'livro': livro
        })

        print("Livro emprestado com sucesso!")
        return True


    def emprestar(self, usuario, data, livro):

        if not livro['disponivel']:
            print('Livro já emprestado!')
            return False

        data_obj = datetime.strptime(data, "%Y-%m-%d")
        prazo = data_obj + timedelta(days=7)

        livro['disponivel'] = False

        usuario['Emprestimos'].append({
            'data': data_obj,
            'prazo': prazo,
            'livro': livro
        })

        print("Livro emprestado com sucesso!")
        return True