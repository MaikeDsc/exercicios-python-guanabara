def sep():
    print('-=-'*25)


times = ('Flamengo','Cruzeiro','Palmeiras', 'Bahia', 'Botafogo', 'Mirassol', 'São Paulo', 'Red Bull Bragantino', 'Fluminense', 'Ceará', 'Corinthians', 'Atlético-MG', 'Internacional', 'Grêmio', 'Santos', 'Vasco da Gama', 'Vitória', 'Juventude', 'Fortaleza', 'Sport Recife')
sep()
print(f'    5 primeiros colocados: {times[:5]}')
sep()
print(f'    4 ultimos: {times[16:21]}')
sep()
print(f'    Em ordem alfabética: {sorted(times)}')
sep()

idvasco = times.index('Vasco da Gama')
print(f'    Vasco está na posição {idvasco}')
sep()