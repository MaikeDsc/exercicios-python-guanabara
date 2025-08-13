vlc = float(input('Informe a velocidad do carro: '))
if vlc>=80.0:
    print(f'Voçê está a {vlc}km/h, você excedeu o limite da via!!')
    multa= (vlc-80.0)*7.0
    print(f'VOCÊ TERÁ QUE PAGAR R${multa:.2f} AO DETRAN!!!')
else:
    print('Você está dentro dos limites da via!')