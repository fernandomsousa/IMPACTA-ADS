class Mae:
    def __init__(self, p1):
        print("Executando o init de Mae")
        self.p1 = p1

class Filha(Mae):
    def __init__(self, p1, p2):
        print("Executando o init de Filha")
        self.p2 = p2
        super().__init__(p1)

class Neta(Filha):
    def __init__(self, p1, p2, p3):
        print("Executando o init de Neta")
        self.p3 = p3
        super().__init__(p1, p2)
        