numeros = []
while True:
    n = int(input('informe um número[-1 para encerrar]: '))
    if n == -1:
        break
    elif n not in numeros:
        numeros.append(n)
numeros.sort()
print(numeros)
