nome = input('informe seu nome completo:').strip()

print(nome.upper())
print(nome.lower())

nome=nome.split()
todos=''.join(nome)
print(f'ao todo seu nome tem {len(todos)} letras')
primeiro = nome[0]
print(f'o primeiro nome tem {len(primeiro)} letras')
