'''
crie um programa que leia o nasacimento de 7 pessoas e 
no final mostre quantas atigiram a maoridade e quantas não. 
'''
from  datetime import date

anoat= date.today().year
idades=[]
qmaiores = []
qmenores = []

for c in range (7):
    idades.append(int(input(f'{c+1}° ano de nascimento: ')))
    idades[c] = anoat-idades[c]
    if idades[c]<=18:
        qmenores.append(idades[c])
    elif idades[c]>18:
        qmaiores.append(idades[c])  

#print(idades)

print(f'quantidade de menores de idade : {len(qmenores)}')
print(f'quantidade de maiores de idade: {len(qmaiores)}')

