import random 
al1 = str(input('informe o aluno 1: '))
al2 = str(input('informe o aluno 2: '))
al3 = str(input('informe o aluno 3: '))
al4 = str(input('informe o aluno 4: '))

lista = [al1, al2, al3, al4]
novalista = random.sample(lista, k=4)
print(f'a ordem do trabalho será : {novalista}')