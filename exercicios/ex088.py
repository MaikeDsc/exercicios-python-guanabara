from random import randint
qtd_jogos = int(input('informe quantos jogos serão gerados: '))

jogos = []
for c in range(0, qtd_jogos):
    numeros = []
    for i in range (0,6):
        
        numeros.append(randint(0,60))
    
    jogos.append(numeros)

for c in range(qtd_jogos):
    print(f'jogo {c+1}: ', ' '.join(map(str, jogos[c])))
