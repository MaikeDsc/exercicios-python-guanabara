r1 = float(input('informe o valor da reta 1: '))
r2 = float(input('informe o valor da reta 2: '))
r3 = float(input('informe o valor da reta 3: '))

if r1<r2+r3 and r2<r1+r3 and r3<r1+r2:
    
    if r1 == r2 == r3:
        print('as retas forman um triângulo equilátero.')
    elif r1 ==r2 or r1==r3 or r2==r3:
        print('as retas formam um triângulo isóceles. ')
    else:
        print('as retas forman um triângulo escaleno.')
else:
    print('as retas não podem formar um triângulo.')