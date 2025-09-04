geral = []
pares = []
impares = []
while True:
    n=0
    n = int(input('informe um número: '))
    geral.append(n)

    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

    op = input('quer continuar?[s/n]: ')
    if op in 'Nn':
        break
    else:
        while op not in 'Ss':
            op = input('opção inválida. Quer continuar? [s/n]: ')

print('-=' *25)
print(f'Números digitados: ',geral)
print(f'Impares: ', impares)
print(f'Pares: ', pares)
print('-=' *25)
