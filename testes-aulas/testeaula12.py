nome = str(input('informe seu nome: ')).strip()
nome = nome.upper()
if nome == 'MAQUIAVEL':
    print(f'seu nome é bonito!')
elif nome == 'MAIKE':
    print('bonnito, seria o seu apelido?')
else:
    print('seu nome é bem normal :/')

print(f'Bom dia, {nome.title()} ')