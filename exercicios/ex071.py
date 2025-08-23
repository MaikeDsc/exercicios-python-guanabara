
while True:
    
    valor = int(input('valor a ser sacado: R$ '))
    

    if (valor // 100) >= 1:
        print(f'Notas de RS 100.00 = {valor//100}')

    r100 = valor % 100
    if(r100// 50) >= 1:
        print(f'Notas de R$ 50.00 = {r100//50}')

    r50 = r100 % 50
    if(r50 // 20) >= 1:
        print(f'Notas de R$ 20.00 = {r50//20}')

    r20 = r50 % 20
    if(r20 // 10) >= 1:
        print(f'Notas de R$ 10.00 = {r20//10}')
    
    r10 = r20 % 10
    if (r10 // 5) >= 1:
        print(f'Notas de R$ 5.00 = {r10//5}')

    r5 = r10%5
    if r5 >= 1:
        print(f'Notas de R$ 1.00 = {r5}')


    print('-'*25)
    op = str(input('deseja continuar? [s/n] ').upper())

    if op == 'N':
        break
    while op != 'S':
        print('Opção inválida!')
        op = str(input('deseja continuar? [s/n] ').upper())
        if op == 'N':
            break      

print('FIM'.center(25, '-')) 