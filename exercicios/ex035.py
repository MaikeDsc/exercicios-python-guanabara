
print('-=-' * 20)
print('analizador de triângulos')
print('-=-' * 20)
r1 = int(input('Informe uma reta: '))
r2 = int(input('informe outra reta: '))
r3 = int(input('informe outra reta: '))

if r1 < r2+r3 and r2 < r1+r3 and r3 < r1+r2:
    print(f'\033[1;37;42m As retas podem formar um triângulo!\033[m')
else: 
    print('\033[1;37;41mé impossível montar um triângulo com essas retas!\033[m')
