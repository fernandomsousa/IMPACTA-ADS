# Entrada: Valor indeterminado de inteiros, sendo ecerrada quando um valor negativo for adicionado.
# Saída: Média entre todas as idades indicadas com 2 casas decimais.

contador = 0
soma = 0
idade = int (input())

while idade > 0:
    soma += idade
    contador +=1
    idade = int (input())

media = soma / contador
print(f"{media:.2f}")

# Resultado: Aceito!!