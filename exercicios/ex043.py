peso = float(input('informe seu peso(kg): '))
altura = float(input('informe sua altura(m): '))

imc= peso/altura**2
print(f'seu imc é {imc:.2f}, ',end='')
if imc < 18.5:
    print('você está abaixo do peso:')
elif imc >= 18.5 and imc < 25:
    print('você está no peso ideal')
elif imc >= 25 and imc < 30:
    print('você está sobrepeso')
elif imc >= 30 and imc < 40:
    print('você está  obeso')
else:
    print('você está em obesidade mórbida')