import math 
num = int(input('informe um número: '))

un = num % 10
dz = num//10 % 10
ct = num//100 %10
ml = num//1000 %10
print(f'unidade : {un}')
print(f'dezena : {dz}')
print(f'centena: {ct}')
print(f'milhar: {ml}')


