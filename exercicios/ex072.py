#impprimir numeros por extenso usando tuplas
numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',  'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = float(input('inoforme um número: '))
    if 0 <= num <= 20:
        break
print('-'*20)
print(f'Você digitou o número {numeros[int(num)]}')
print('-'*20)