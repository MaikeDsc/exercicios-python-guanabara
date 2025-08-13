op = int(input('escolha a opção de convesão [1]binário [2]octal [3]hexadecimal: '))
num = int(input('informe o numero que deseja converter : '))

if op == 1:
#    num = bin(num)
    print(f'conversão para binário: {num:b} ')
elif op == 2:
    num = oct(num)
    print(f'conversão  para octal: {num} ')
elif op == 3:
    num = hex(num)
    print(f'converçao para hexadecimal {num}')
else:
    print('opção inválida! tente novamente! :/')
    