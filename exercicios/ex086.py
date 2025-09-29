matriz = [[0, 0, 0],[0, 0, 0,],[0, 0, 0]]

for i in range(3):
   for j in range(3):
       n  =  int(input(f'informe a {i+1,j+1}: '))
       matriz[i][j] = n

print('_'*30)

for i in matriz:
    for j in i:
        print(f'| {j:^5} ', end='|')
    print()

