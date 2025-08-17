#os 10 primeiros termos de uma PA com while 
a1 = int(input('primeiro termo: '))
r = int(input('razão: '))

an = 0
cont = 0

while cont < 10:
    cont += 1
    an += r
    print(an, end=' ')

