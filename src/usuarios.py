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

        data_obj = datetime.strptime(data, "%Y-%m-%d") #conversão da data de string para objeto do datetime para o cálculo
        prazo = data_obj + timedelta(days=7) #prazo de 7 dias para devolução, calculado com base no dia de hoje

        livro['disponivel'] = False #marca o livro como indisponivel

        usuario['Emprestimos'].append({
            'data': data_obj,
            'prazo': prazo,
            'livro': livro
        }) #adiciona o empréstimo a lista do usuário

        print("Livro emprestado com sucesso!")
        return True


    def devolver(self, usuario, data, livro): #método para devolução 

        hoje = datetime.today() #data de hoje para calcular o atraso, caso haja
        multa_total = 0

        for emp in usuario['Emprestimos']: #para cada empréstimo do usuário
            if emp['livro'] == livro: #se o livro for igual ao digitado

                prazo = emp['prazo'] #olha o prazo

                if hoje > prazo: #calcula a multa, sendo 1 real por dia
                    dias_atraso = (hoje - prazo).days
                    multa_total = dias_atraso * 1  # R$1 por dia

                usuario['Emprestimos'].remove(emp) #remove o empréstimo da lista

                livro['disponivel'] = True #marca o livro como disponível novamente

                print("Livro devolvido!")

                if multa_total > 0: #mostra a multa, caso haja
                    print(f"Multa por atraso: R${multa_total}")
                else:
                    print("Sem multa!")

                return

        print("Empréstimo não encontrado") #se não for encontrado, mostra mensagem de erro