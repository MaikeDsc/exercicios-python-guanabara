num = int(input('informe um numero: '))
primo=0
for c in range(2, num):
    if num % c == 0:
        primo = 1

if primo == 1:
    print('o número não é primo')
elif primo==0:
    print('o número é primo')