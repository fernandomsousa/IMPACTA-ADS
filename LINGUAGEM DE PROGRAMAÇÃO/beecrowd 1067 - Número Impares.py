# Entrada: Arquivo de entrada com 1 valor inteiro qualquer,
# Saída: Todos os valores impares que antecedem a entrada.

x = int (input())

for i in range (1, x+1):
    if i % 2 != 0:
        print(i)
        
# Resultado: Aceito!!