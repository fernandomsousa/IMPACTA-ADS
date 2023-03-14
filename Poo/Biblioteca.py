# Aulas de POO com Python - Exercício: Biblioteca!

class Livro:
    def __init__(self, nome, autor):
        self.Nome = nome
        self.Autor = autor
        self.editora = 'Barroco'

    def identidade(self):
        return (f'Sou o livro {self.Nome}, do autor(a) {self.Autor} e estou salvo no'
        f' endereço de memória: {id(self)}')


if __name__ == '__main__':
    livro_1 =  Livro('Harry Potter', 'JK Rowling')
    livro_2 =  Livro('A Máquina do Tempo', 'HG Wells')

    print('Temos os seguintes titulos disponíveis:\n',livro_1.Nome, 'de',livro_1.Autor,'\n',livro_2.Nome, 'de', livro_2.Autor)
