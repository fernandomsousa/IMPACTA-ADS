# Sobrecarga = mesmo método com mais de uma forma

def sobrecarga(nome, numero = None):
    print(nome)
    if numero:
        print(numero)

print('primeira execução')
sobrecarga('Rafael')

print('\nsegunda execucao')
sobrecarga('Rafael', 10)
