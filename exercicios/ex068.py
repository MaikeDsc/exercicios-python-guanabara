from random import randint 
vitorias = 0

while True:
    escolha = 'c'
    ncpu = randint(1,10)

    while  escolha not in 'IP':
        escolha = str(input('Você é ímpar ou par? [I/P]: ').upper())
    
    nplayer = int(input('informe número de 1 a 10: '))

    soma = ncpu + nplayer 
    if (soma % 2 == 1) and (escolha == 'I'):
        print('Voce veenceu!')
        vitorias += 1 
    elif (soma % 2 == 0) and (escolha == 'P'):
        print('Você venceul!')
        vitorias += 1
    
    else:
        break 

print(f'você perteu :/ após {vitorias} vitórias')



