# Entradas: Dois números inteiros, um em cada linha.
# Saídas: Valores da tabuada dentro do intervalo e separados por hifen.

primeiroNum = int (input())
segundoNum = int (input())

if segundoNum >= primeiroNum:
  while primeiroNum < segundoNum+1:
    for i in range(1, 11):
      mult = primeiroNum * i
      print(primeiroNum, "x", i, "=", mult)
    primeiroNum = primeiroNum + 1
    print("----------")
else:
  print("Nenhuma tabuada no intervalo!")

# Resultado: aceito!!