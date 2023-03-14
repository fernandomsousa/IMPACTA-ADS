class Mae:
    def __init__(self, p1):
        print("Executando o init de Mae")

class Filha(Mae):
    def __init__(self, p1, p2):
        print("Executando o init de Filha")
        self.p2 = p2
        Mae.__init__(self, p2)

class Neta(Filha):
    def __init__(self, p1, p2, p3):
        print("Executando o init de Neta")