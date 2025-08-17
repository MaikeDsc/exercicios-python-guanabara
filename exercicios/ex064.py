
print('O programa para e exibe a soma entre todos digitados quando vc digita 999')
loop = True

while loop == True:
    num = int(input('informe um número: '))

    if num != 999:
        num += num
    elif num == 999:
        loop = False

print('SOMA: ', num)