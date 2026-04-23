from database.database import dados
from datetime import date
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
    
    def emprestar(self, usuario, livro):

        if not livro['disponivel'] == True:
            print('Livro já emprestado!')
            return False

        livro['disponivel'] = False
        usuario['Emprestimos'].append((date, livro))
        return True

    def devolver(self, usuario, livro):
        if not livro['disponivel'] == False:
            print("Este livro não foi emprestado")
        livro['disponivel'] = True
        usuario['Emprestimo'].remove((date, livro))