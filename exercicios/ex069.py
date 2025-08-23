cmulher = chomem = maiores= 0

while True:
    print('-'*25)
    sexo = str(input('Informe o sexo[M/f]: ').strip().upper())
    idade = int(input('Iforme a idadde: ').strip())

    if idade > 18:
        maiores += 1
    if  sexo == 'M':
            chomem += 1
    elif sexo == 'F' and idade < 20:
        cmulher += 1
    print('-'*25)
    op = str(input('Quer cotinuar? [S/N] : ').strip().upper())
    if op == 'N':
        break
    while op != 'S':
        print('Opção inválida. ')
        op = str(input('Quer cotinuar? [S/N] : ').strip().upper())
        if op == 'N':
            break
print('-=-'*20)
print('maiores de 18 anos: ', maiores)
print('homens cadastrados: ', chomem)
print('mulheres menores que 20 anos: ', cmulher)
print('-=-'*20)