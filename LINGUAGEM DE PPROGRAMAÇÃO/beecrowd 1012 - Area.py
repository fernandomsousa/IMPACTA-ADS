pi = 3.14159
Valores = input() .split() 
A = float (Valores [0]) 
B = float (Valores [1])
C = float (Valores [2])

tri = (A * C)/2
cir = C**2 * pi
tra = ((A + B)*C)/2
qua = B**2
ret = A * B
print(f"TRIANGULO: {tri:.3f}")
print(f"CIRCULO: {cir:.3f}")
print(f"TRAPEZIO: {tra:.3f}")
print(f"QUADRADO: {qua:.3f}")
print(f"RETANGULO: {ret:.3f}")
