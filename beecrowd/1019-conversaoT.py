segif = int(input())

seg = segif%60
min = (segif%3600)//60
hora = segif//3600


print(f'{hora}:{min}:{seg}')

#hora seg*60