usnum = int(input('digite o número que deseja saber a tabuada: '))
print('''informe a operação desejada: 
      [1] ADIÇÃO
      [2] SUBTRAÇÃO
      [3] MULTIPLICAÇÃO
      [4] DIVISÃO''')
op = int(input('sua escolha aqui: '))

if op == 1:
    for c in range(1, 11):
        print(f'{usnum} + {c} = {c+usnum}')

elif op == 2:
    for c in range(1,11):
        print(f'{usnum} - {c} = {usnum-c}')

elif op== 3:
    for c in range(1,11):
        print(f'{usnum} * {c} = {usnum*c}')

elif op == 4:
    for c in range(1,11):
        print(f'{usnum} / {c} = {usnum/c:.1f}')

else: 
    print('opção inválida!')
