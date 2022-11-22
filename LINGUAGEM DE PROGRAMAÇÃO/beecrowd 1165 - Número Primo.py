# Entradas: número de casos teste; 3 números inteiros primos ou não.
# Saídas: Número é ou não é primo.

escolha = int (input())

for i in range (0, escolha):
    n = int(input())
    if n == 2:
        print("2 eh primo")
    elif n % 2 == 0:
        print(f"{n} nao eh primo")
    else:
        x = 3
        while(x < n):
            if n % x == 0:
                break
            x = x + 2
        if x == n:
            print(f"{n} eh primo")
        else:
            print(f"{n} nao eh primo")
            
# Resultado: Aceito!