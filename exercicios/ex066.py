num = soma = n = 0

while True:
    num = int(input('informe um numero: '))
    if num == 999:
        break
    soma += num
    n += 1

print(f'A soma dos {n} números digitados é {soma}')