print(f'{'LOJAS DSC':=^40}')
preco = float(input('informe o valor do produto: '))
print('''Opções de pagamento:
    |[1] dinheiro à vista            |
    |[2] à vista no débito           |
    |[3] 2x no cartão                |
    |[4] 3x ou mais no cartão        |''')    
fp = int(input('informe a opção desejada: '))

if fp == 1:
    vlfinal = preco - (0.1*preco)
    print(f'nessa forma de pagamento vc recebe 10% de desconto. total a pagar R${vlfinal:.2f}')
elif fp == 2:
    vlfinal = preco - (0.05*preco)
    print(f'nessa forma de pagamento você ganha 5% de desconto> total a pagar R${vlfinal:.2f}')
elif fp ==3:
    print(f'total a pagar 2X DE R${preco/2:.2f}, sem descontos.')
elif fp == 4:
    vlfinal = preco + (0.2*preco)
    print(f'você terá que pagar 20% de juros. total a pagar 3X de R${vlfinal/3:.2f}')
else:
    print('informe uma opção válida.')