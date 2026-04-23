from database.database import dados

class Livros():

    def __init__(self):
        dados['livros'] = self.livros
    
    def adicionar_livro(self, livro):

        novo = {
            'titulo' : livro,
            'disponivel' : True,
        }

        self.livros.append(novo)
        print(f'{livro} salvo com sucesso!')

    def remover_livro(self, livro):

        self.livros.remove(livro)

        print(f'{livro} removido com sucesso!')

    
