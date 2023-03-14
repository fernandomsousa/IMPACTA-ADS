from time import sleep

class Teste:
    def __init__(self):
        self._nome = ''


    @property
    def nome(self):
        print('Executando Properety...')
        sleep(1)
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        print("Executando o setter...")
        sleep(3)
        self._nome = novo_nome
