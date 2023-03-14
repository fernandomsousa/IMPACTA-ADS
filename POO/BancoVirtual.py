# Aulas de POO com Python - Exercício: Banco Virtual!

class Conta:
    def __init__(self, numero, titular):
        self.Numero = numero
        self.Titular = titular
        self.__Saldo = 0

    # MÉTODOS:
    def ver_saldo(self):
        return self.__Saldo
    
    def depositar(self, valor):
        if valor < 0:
            return 'O valor de saque deve ser positivo!'
        self.__Saldo += valor
    
    def sacar(self, valor):
        if valor < 0:
            return 'O valor de saque deve ser positivo!'
        if valor > self.__Saldo:
            return 'Saldo insuficiente para esta transação!'
        self.__Saldo -= valor

if __name__ == '__main__':
    conta_1 = Conta(1, 'Fernando')
    conta_2 = Conta(2, 'Isabelle')