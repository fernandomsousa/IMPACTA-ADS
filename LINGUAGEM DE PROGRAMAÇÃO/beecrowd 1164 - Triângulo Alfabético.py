# Entrada: Quantidade de repetições.
# Saída: Pirâmide de letras de acordo com a quantidade da entrada.

vezes = int(input())


alfabeto = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


for i in range(vezes):
    print(alfabeto[i]*(i+1))

# Resultado: aceito!!