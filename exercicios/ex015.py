dias = int(input('quantos dias o carro foi alugado? '))
km = float(input('quantos km foram rodados? '))

total = (dias*60)+(km*0.15)

print(f'o total a pagar é: R${total:.2f}')