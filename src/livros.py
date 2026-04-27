from database.database import dados #importação dos dados da db

class Livros(): #classe do gerenciamento dos livros

    def __init__(self): 
       self.livros = dados['livros']
    
    def adicionar_livro(self, livro): #função de adição de um livro, apenas para o adm

        novo = {
            'titulo' : livro,
            'disponivel' : True,
        }

        self.livros.append(novo)
        print(f'{livro} salvo com sucesso!')

    def remover_livro(self, livro): #mesma coisa, agora, para remoção

        self.livros.remove(livro)

        print(f'{livro} removido com sucesso!')
    
    def buscar_livro(self, titulo): #função para busca do livro, em O(n), olhando um por vez, levando em conta o método de armazenamento
        #lógica: para cada livro na lista, se o título for igual ao digitado, retorna o livro, caso contrário, retorna None
        for livro in self.livros: 
            if livro['titulo'] == titulo:
                return livro
        
        return None

    def listar_livros(self): #função para listar os livros, apenas para o adm, mostrando o título e a disponibilidade
        for livro in self.livros:
            print("-------Lista de Livros-------")
            print(f"\n{livro['titulo']}")
            if livro['disponivel']:
                print("~Disponível para empréstimo~")
                print("-------------")
            else:
                print("~Indisponível para empréstimo~")
                print("-------------")
                  