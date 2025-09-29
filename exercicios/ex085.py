numeros  = [[],[]]

for c in range(8):
    
    n = int(input(f'informe o {c+1}º número:'))

    if n % 2 == 0:
        numeros[0].append(n)
    else:
        numeros[1].append(n)

print('Pares:', ', '.join( map(str, sorted(numeros[0])) ) ) 
print('Inpares:', ', '.join( map(str, sorted(numeros[1])) ) )
 