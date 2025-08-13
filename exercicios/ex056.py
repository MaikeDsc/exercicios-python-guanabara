nome = []
idade= []
sexo =[]
somaid = 0
maisvelho = 0
idmaisvelho=0
mulheresd20= 0

for c in range(3):
    nome.append(str(input(f'informe o nome da {c+1}ª pessoa: ')))
    idade.append(int(input(f'informe a idade da {c+1}ª pessoa: ')))
    sexo.append(int(input(f'informe o sexo [1] masc [2] fem: ')))
    somaid += idade[c]

    if sexo[c] ==1:
        maisvelho = max(idade) #pega o nome do mais valho 
        idmaisvelho = idade.index(maisvelho) #pega a posição de onde esta o nome do mais velho
    elif sexo[c] ==2 and idade[c]<20:
        mulheresd20 = mulheresd20 + c

    
mediaid = somaid/3
print(f'média das idades: {mediaid:.1f}')
print(f'homen mais velho: ',nome[idmaisvelho])
print('mulheres com idade inferior a 20 anos: ',mulheresd20)
