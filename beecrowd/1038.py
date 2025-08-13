num, quant = map(int, input().split())

hd = 4
xsalad = 4.5
xbacon = 5
tor = 2
refr = 1.5
prodprec = [0, 4, 4.5, 5, 2, 1.5]

if num == 1:
    preco = hd * quant
    print(f'Total: R$ {preco:.2f}')
elif num ==2:
    preco = xsalad * quant
    print(f'Total: R$ {preco:.2f}')
elif num == 3:
    preco = xbacon * quant
    print(f'Total: R$ {preco:.2f}')
elif num == 4:
    preco = tor * quant
    print(f'Total: R$ {preco:.2f}')
elif num == 5:
    preco = refr * quant
    print(f'Total: R$ {preco:.2f}')