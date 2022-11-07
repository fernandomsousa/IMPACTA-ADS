# Entrada: valores continuos até detectar -1.
# Saída: valor digitado e obtido com total.

carteira = []
total = 0
while True:
    vcs = float(input())
    if vcs > 0:
        carteira.append(vcs)
    else:
        break
for x in carteira:
    total += x
print(f'VC$ {total:.2f}')
print(f'R$ {(total * 2.5):.2f}')

# Resultado: aceito!!