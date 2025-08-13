from random import choice
al1 = str(input('informe o nome do aluno 1: '))
al2 = str(input('informe o nome do aluno 2: '))
al3 = str(input('informe o nome do aluno 3: '))
al4 = str(input('informe o nome do aluno 4: '))

sorteado = [al1, al2, al3, al4]

print(f'o aluno sorteado da vêz é {choice(sorteado)}!!')