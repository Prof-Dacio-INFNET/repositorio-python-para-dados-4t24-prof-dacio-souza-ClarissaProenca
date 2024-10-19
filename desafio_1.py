matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

for linha, _ in enumerate(matriz):
    for coluna, _ in enumerate(matriz[linha]):
        matriz[linha][coluna] = matriz[coluna][linha]

print(matriz)