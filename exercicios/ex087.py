matriz = [[0,0,0],[0,0,0],[0,0,0]]

spares = terceira = 0

for i  in range(0,3):
    for j in range(0,3):
        matriz[i][j] = int(input(f'informe o {i, j}: '))

        if matriz[i][j] % 2 == 0:
            spares += matriz[i][j]
        if j== 2:
            terceira += matriz[i][j]

for i in matriz:
    for j in i:
        print(f'| {j:^5}', end='|')
    print()

print('-'*30)
print('soma dos pares: ', spares)
print('soma terceira coluna: ', terceira)
print('maior da segunda fileira: ', max(matriz[1]))
print('-'*30)