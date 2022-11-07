# Entrada: Valor inteiro N, apresentar cada um dos pares até atingir o valor de N, inclusive ele mesmo.
# Apresentar o quadrado de cada um dos valores pares.
# Saída: Valores quadrados dos pares com resultado.

n = int (input())

for i in range(1,n+1): # Como quero contar o próprio número, coloco a condição de n + 1.
    if(i%2==0):
        cal = i ** 2 
        print(f"{i}^2 = {cal}")

# Resultado: Aceito!!