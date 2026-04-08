matriz_a = [
    [1,0,3],
    [2,5,7],
    [4,9,8],
]

matriz_b = [
    [4,5,1],
    [2,7,9],
    [0,6,7],
]
#Las matrices deben de ser del mismo tamaño
#Primero se recorren los elementos de la primera fila, sumando cada elemento uno a uno, luego, se recorre la segunda fila y asi sucesivamente
#len(matriz_a) = Dimensión de las filas
#len(matriz_a[0]) = Dimensión de las columnas

suma_matrices = [[matriz_a[i][j] + matriz_b[i][j] for i in range(len(matriz_a))] for j in range(len(matriz_a[0]))]

print(f"la matriz resultante de la suma es {suma_matrices}")

matriz_c = [
    [1,4,],
    [7,8,],
]

#En una matriz [[a, b], [c, d]] el determinante es a*d - b*c

determinante_c = (matriz_c[0][0] * matriz_c[1][1]) - (matriz_c[0][1] * matriz_c[1][0])

print(f"El determinante de la matriz c es {determinante_c}")

lista = ["a", "b", "c", "d"]

for letra in lista:
    print(letra)

