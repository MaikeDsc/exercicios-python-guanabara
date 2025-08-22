#o problema pede para quando o número informado for negativo o programa deve parar
while True:
    
    num  =  float(input('informe um número: '))
    if num >= 0:

        for c in range (1, 11):
            multiplicacao = num * c
            print(f'{num:.0f} x {c} = {multiplicacao:.0f}')
    
    else:
        break

print(f'FIM'.center(20,'='))
