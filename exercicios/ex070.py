total = 0
maiores1000 = 0
lnomes = []
lprecos= []
cont = 0

while True:
    cont += 1

    print('-'*20)
    nome = str(input('- Informe o nome do produto:').capitalize())
    lnomes.append(nome)
    preco = float(input('- Informe o preço: R$ '))
    lprecos.append(preco)

    total += preco

    if preco > 1000.00:
        maiores1000 += 1
    
    print('-'*20)
    op = str(input('quer continuar [s/n] ? ').upper())
    if op == 'N':
        break
    while op != 'S':
        print('Opção inválida!')
        op = str(input('Quer continuar [s/n?').upper())
        
        if op == 'N':
            break
    
menorpreco = min(lprecos)
idmenor = lprecos.index(menorpreco)

nomemenor = lnomes[idmenor]

print('SUA COMPRA'.center(30, '-'))
print(f'TOTAL GASTO = R$ {total:.2f}')
print(f'CUSTAM MAIS DE R$ 1000.00 = {maiores1000}')
print(f'MAIS BARATO = {nomemenor} custando R$ {menorpreco:.2f}')
print('-'*40)
