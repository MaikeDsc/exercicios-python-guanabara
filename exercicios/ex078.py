numeros = list(map(int, input('informe n números : ').split()))

print(f'maior : { max(numeros) } na posição', end='')

for i, v in enumerate(numeros):
    if v == max(numeros):
        print(f' {i}... ', end='')

print(f'\nmenor: { min(numeros) } na posição', end='')

for i, v in enumerate(numeros):
    if v == min(numeros):
        print(f' {i}... ', end='')


