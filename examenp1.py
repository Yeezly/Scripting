import numpy as np
print("De que tamaño quieres que sea tu matriz?")
x = int(input(""))
y = x
matriz = [[False for j in range(y)]for i in range(x)]
if x % 2 == 0:
    print("el numero es par intenta de nuevo")
else:
    for i in range(x):
        matriz[i][i] = True
print(np.array(matriz))