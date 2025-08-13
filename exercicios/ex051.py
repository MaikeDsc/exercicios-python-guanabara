a1 = int(input('informe a primeiro termo da PA: '))
r = int(input('informe a razão da PA: '))

pa =[]

for c in range(1,11):
    pa.append(a1+(c-1)*r)
    soma = sum(pa)
print(f'aprogressão é = {pa}')
print(f'a soma entre os termos é = {soma}')