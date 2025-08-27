valores = int(input()), int(input()), int(input()), int(input())

print(f'o número 9 foi digitado {valores.count(9)} vezes')

print(f'o número 5 aparece na {valores.index(5)+1}ª posição' if 5 in valores else 'o número 5 não aparece na lista')

print(f'são pares: ', end='' )
for c in valores:
    if c%2 == 0:
        print(f'{c} ', end = '' )
        
   