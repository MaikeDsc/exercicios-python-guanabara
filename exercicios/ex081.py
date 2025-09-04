numeros = []
while True:
    numeros.append(int(input('Informe um número: ')))
    op = str(input('Quer continuar? [s/n]').upper())

    if op == 'N':
        break
    while op != 'S':
        op = str(input('Quer continuar? [s/n]').upper())
        if op == 'N':
            break

print('-='*25)
print(f'Foram digitados {len(numeros)} numeros')
print(f'Em ordem crescente ficam {sorted(numeros)}')
print(f'5 está na lista!' if 5 in numeros else '5 não está na lista!')
print('-='*25)