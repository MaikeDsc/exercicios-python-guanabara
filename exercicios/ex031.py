dist = float(input('Informe a distancia a ser percorrida na viagem, em km: '))
if dist<=200:
    custo = dist*0.5
    print(f'a viagem é curta e vai custar R${custo:.2f} reais! pague no fim.')
else:
    custo= dist*0.45
    print(f'a viagem é longa e custará R${custo:.2f} reais, pague no fim.')