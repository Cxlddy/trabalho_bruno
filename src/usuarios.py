from database.database import dados
from datetime import date, datetime, timedelta
date = date.today()

class Usuarios():

    def __init__(self):
        self.usuarios = dados['usuarios']

    def criar_novo(self, nome_usr, senha):

        novo = {
            'nome': nome_usr,
            'senha': senha,
            'tipo' : 'usuario',
            'Emprestimos' : [],
        }

        self.usuarios.append(novo)

    def logar(self, nome_usr, senha):

        for usuario in self.usuarios:

            if usuario['nome'] == nome_usr and usuario['senha'] == senha:
                print(f"Logado com sucesso, seja bem vindo, {nome_usr}")
                return usuario
        
        print("Nome ou senha incorreto(s)")
        return None
    
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