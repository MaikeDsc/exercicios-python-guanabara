'''-ler n números 
    - exibir a média entre todos 
    - o maior e o menor 
    -perguntar se quer ou não continuar digitando
'''
loop = True
cont = 0
soma = 0
numeros = []
while loop == True:
    num = int(input('informe um número: '))
    numeros.append(num)
    soma += num
    cont += 1 

    opcao = str(input('Quer continuar a digitar?[S/N] ').upper())

    if opcao == 'N':
        loop = False

media = soma/cont
maior = max(numeros)
menor = min(numeros)

print('MEDIA: ', media)
print('MAIOR: ', maior)
print('MENOR: ', menor)