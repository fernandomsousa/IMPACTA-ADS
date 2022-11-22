# Entradas: Diversos valores inteiros, um por linha. Entrada finalizada com um valor negativo.
# Saídas: A media desses valores inteiros e abaixo, os tempos de corrida abaixo do valor da média, na ordem que foram adicionados.

valores = [] # Lista vazia para adicionar os valores em segundos.
total = 0

while True:
    tempos = int (input())
    if tempos > 0:
        valores.append(tempos) # Adicionando os valores de entrada em minha lista.
    else:
        break

for x in valores:
    total += x

media = total / len(valores)
print(f"MEDIA: {media:.2f}")

for x in valores:
    if x < media:
        print(x)

# Resultado: aceito!!