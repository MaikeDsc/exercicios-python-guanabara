dados = []
soma = 0
for c in range (0,6):
    us = int(input(f'informe o {c+1}º número : '))
    dados.append(us)
    if dados[c] % 2 == 0:
        soma += dados[c]
print(f'a soma entre os pares é: {soma}')

#append adiciona um item na nultima posição daa lista