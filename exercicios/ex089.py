dados = []

print('---------cadastro de notas de alunos-----------')
while True:
    print('-=' * 25)

    aluno = []
    aluno.append( str(input('Nome aluno: ')))
    na, nb = map(float, input('informe nota a e b respectivamente: ').split())
    aluno.append(na)
    aluno.append(nb)
    aluno.append((na+nb)/2)

    dados.append(aluno)
    print('-=' * 25)

    op = str(input('Deseja continuar? [s/n]'))
    if op in 'Nn':
        break


print(f'BOLETIM'.center(50, '/'))

for aluno in dados:
    print(f'Nome: {aluno[0]} -> Nota: {aluno[3]}', end= ' ')
    print('(Aprovado)' if aluno[3] >=6 else '(Reprovado)')

print('/'*57)

pesquisar = str(input('pesquisar aluno [S/N]: '))


while pesquisar in 'Ss':


    nome = str(input('nome: ').lower())

    for c in range(len(dados)):
        
        if nome in dados[c][0]:
            print(f'nota de {dados[c][0]} são: {dados[c][1]} e {dados[c][2]}')
            nao_encontrado= False
            break
        
        else: 
            nao_encontrado = True
    
    if nao_encontrado == True:
        print('nome não encontrado!')

    print('-=' * 25)
    pesquisar = str(input('pesquisar aluno [S/N]: '))

else: 
    print('-------------FIM-------------')
    

