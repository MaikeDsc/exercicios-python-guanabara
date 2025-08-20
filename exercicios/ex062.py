a1 = int(input('primeiro termo: '))
r = int(input('razão: '))

an = a1
cont = 0

while cont < 10:
    cont += 1
    print(an, end=' ')
    an += r

loop = True
while loop == True:
    termamais = int(input('\n pretende ver mais quantos termos? '))
    limitloop = cont + termamais

    if termamais > 0:
        while cont < limitloop:
            cont += 1
            print(an, end=' ')
            an += r
            
    elif termamais == 0:
        loop = False
    
print('')
print(f'fim'.center(30,'='))
print('')