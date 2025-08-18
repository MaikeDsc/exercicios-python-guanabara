
print('O programa para e exibe a soma entre todos digitados quando vc digita 999')
loop = True

soma = 0
while loop == True:
    num = int(input('informe um número: '))

    if num != 999:
        soma += num
    elif num == 999:
        loop = False

print('SOMA: ', soma)