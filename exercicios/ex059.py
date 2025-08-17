from time import sleep
num1 = float(input('informe um número: '))
num2 = float(input('informe outro número: '))

loop = True

while loop == True:
    print('-=-' * 20)
    print('Escolha euma operação:\n    [1] SOMA \n    [2] MULTIPLICAÇÃO \n    [3] SABER O MAIOR \n    [4] NOVOS NÚMEROS \n    [5] SAIR')
    op = int(input('sua opção: '))

    if op == 1:
        print(f'SOMA: {num1+num2}')
        
    elif op == 2:
        print(f'MULTIPLICAÇÃO: {num1*num2}')
       
    elif op == 3:
        maior = int(max(num1, num2))
        print(f'MAIOR: {maior:.2f}')

    elif op == 4:
        num1 = float(input('informe um número: '))
        num2 = float(input('informe outro número: '))

    elif op == 5:
        loop = False

    print('-=-' * 20)
    sleep(2)

print('--FIM--')
