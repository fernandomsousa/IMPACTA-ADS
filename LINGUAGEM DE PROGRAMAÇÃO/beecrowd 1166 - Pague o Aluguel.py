# Entrada: Valor inteiro total referente à divida; Valor total que pode pagar.
# Saída: Qual mês é o pagamento, valor antes e valor depois.

valortotal = int (input())
podepagar = int (input())
contador = 0

while valortotal > 0:
    contador += 1
    depois = valortotal - podepagar
    print(f"pagamento: {contador}")
    print(f"antes = {valortotal}")
    if depois < 0:
        depois = 0
    print(f"depois = {depois}")
    print("-----")
    valortotal = valortotal - podepagar

# Resultado: aceito!!