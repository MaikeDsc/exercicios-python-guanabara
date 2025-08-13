from math import hypot
cad = float(input('informe o cateto adjacente: '))
cop = float(input('informe o cateto oposto: '))
hip = hypot(cad, cop)
print(f'a hipotenusa é : {hip:.3f}')
