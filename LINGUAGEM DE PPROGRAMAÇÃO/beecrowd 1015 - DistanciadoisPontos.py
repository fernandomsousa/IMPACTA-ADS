valores1 = input() .split()
valores2 = input() .split()

X1 = float (valores1[0])
Y1 = float (valores1[1])
X2 = float (valores2[0])
Y2 = float (valores2[1])

distancia = (X2 - X1)**2 + (Y2 - Y1)**2
distanciaf = distancia**0.5

print(f"{distanciaf:.4f}")
