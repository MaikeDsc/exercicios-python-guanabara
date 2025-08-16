from random import randint

print("=-"*20)
print('Jogo da advinhação \nTente advinhar um número de 1 a 10')
print("=-"*20)

num = int(input('informe um número: '))
cpu = randint(1, 10)
cont = 1
while num != cpu:
    cont += 1
    print('Você errou tente novamente! :( ')
    num = int(input('informe um número: '))
    cpu = randint(1, 11)

print(f'Parabés você acertou!!! após {cont} tentativas ;)')
