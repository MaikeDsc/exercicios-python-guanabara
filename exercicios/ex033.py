import math
a = int(input('informe um valor: '))
b = int(input('informe um valor: '))
c = int(input('informe um valor: '))
menor = a
if b < a and b < c:
    menor =b
if  c < b and c < a:
    menor = c
print (f'menor numero: {menor}')

maior = a
if b > c and b > a:
    maior = b
if c > b and c > a:
    maior = c 
print(f'maior  número: {maior }')