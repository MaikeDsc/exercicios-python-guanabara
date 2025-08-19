num = int(input('Qual número será o fatorial? '))

numa = num
numb = num #será usado para fazer o mesmo problema, mas usando o for 

#--------------Usando While---------------
print(f'{numa}! =', end = '')
fatorial = 1
numa = numa + 1

while numa > 1:
    numa -= 1
    fatorial  *= numa
    print(f' {numa} ', end = '')
    print('*' if numa > 1 else '= ', end='')

print(f'{fatorial}')

#-------------Usando for---------------------

print(f'{numb}! =', end='')

fatorb = 1
for c in range (numb, 0, -1):
    fatorb *= c
    print(f' {c} ', end='')
    print('*' if c > 1 else '= ', end='' )

print(f'{fatorb}')
