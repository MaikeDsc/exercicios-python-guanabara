pessoas = []

cont = 0
soma_peso = 0

while True: 
    dados =[]

    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    pessoas.append(dados)

    soma_peso += (pessoas[cont][1])
    cont +=1 

    op = input('quer continuar? [S/N]')
    if op in 'nN':
        break

   
media_peso = soma_peso / cont

print('-=' * 25)

print('Pessoas cadastradas: ', cont)

print('Mais pesadas: ', end= '')

for c in pessoas:
    if c[1] > media_peso:
        print(c[0], end=', ')

print('\nMais leves: ', end='')

for c in pessoas:
    if c[1]< media_peso:
        print(c[0], end=', ' )

print('/n')
print('=-' * 25)