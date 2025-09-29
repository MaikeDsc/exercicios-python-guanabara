dados = []

print('cadastro de notas de alunos')
while True:

    aluno = []
    aluno.append( str(input('Nome aluno: ')))
    na, nb = map(float, input('informe nota a e b respectivamente: ').split())
    aluno.append(na)
    aluno.append(nb)
    aluno.append((na+nb)/2)

    dados.append(aluno)

    op = str(input('Deseja continuar? [s/n]'))
    if op in 'Nn':
        break


print('-----------BOLETIM----------')

for aluno in dados:
    print(f'Nome: {aluno[0]} -> Nota: {aluno[3]}', end= ' ')
    print('(Aprovado)' if aluno[3] >=6 else '(Reprovado)')
    print('-'*30)

pesquisar = str(input('pesquisar aluno [S/N]: '))

'''if pesquisar in 'Nn':
    while pesquisar in 'Nn':
'''
    

