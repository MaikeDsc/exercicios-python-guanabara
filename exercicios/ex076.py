produtos = ('Notebook',2500, 'Mouse',300, 'Teclado',250,'Mouse Pad',  50)
print('-=-'*20)
for c in range (8):
    if c % 2 == 0:
        print(produtos[c],end='')
        print('-'*20,end='')
    else:
        print(f'R${produtos[c]},00')

    
print('-=-'*20)