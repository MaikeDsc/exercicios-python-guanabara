nome = str(input('informe o seu nome: '))
sexo= str(input('informe o sexo [M/F]: ').upper)

loop = 1
while loop == 1:
    if sexo == "M" or sexo == "F":
        loop = 0
        
    else:
        sexo = str(input('informe o sexo condizente [M/F]: ').upper())

print(f'Nome: {nome} \nSexo: {sexo}')
