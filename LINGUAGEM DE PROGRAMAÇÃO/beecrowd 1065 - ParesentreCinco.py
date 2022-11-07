quantidade = 0

A = int (input())
B = int (input())
C = int (input())
D = int (input())
E = int (input())

parA = A % 2
parB = B % 2
parC = C % 2
parD = D % 2
parE = E % 2

if parA == 0:
    quantidade = quantidade + 1
if parB == 0:
    quantidade = quantidade + 1
if parC == 0:
    quantidade = quantidade + 1
if parD == 0:
    quantidade = quantidade + 1
if parE == 0:
    quantidade = quantidade + 1

print(f"{quantidade} valores pares")

# Resultado: aceito!!
