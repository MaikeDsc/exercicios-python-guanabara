nome = str(input('informe o seu nome: '))
sexo= str(input('informe o sexo [M/F]: ').upper().strip())#coloca em aiuscula, tira os espaços


while  sexo != 'M' and  sexo != 'F':      
    sexo = str(input('informe o sexo [M/F]: ').upper().strip())

print(f'Nome: {nome} \nSexo: {sexo}')
