numeros = list(map(int, input('informe n números : ').split()))

print(f'maior : { max(numeros) } na posição { numeros.index( max(numeros) ) } ')
print(f'menor: { min(numeros) } na posição { numeros.index( min(numeros) )}')


