#mostrar os n primeiros termos da sequencia de fibonacci

n = int(input('quantos números de fibonacci queres ver? '))

f1 = 0
f2 = 0
cont = 0
num = 0

while cont < n:
    num = f1 + f2
    print(num,end=' ') 

    if num == 0: 
        f2 = 1

    f1 = f2
    f2 =num
    cont += 1

print('\n| fim |\n')