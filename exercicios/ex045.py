#jokenpô
from random import randint
from time import sleep
print('°°°°'*15)
print('Jokenpô player vs CPU \nEscolha a sua opção:\n[1]Pedra \n[2]Papel \n[3]Tesoura')
#o\n é sequela do c++ eu poderia ter usado aspas triplas 
print('°°°°'*15)
op = int(input('Sua escolha aqui aqui: '))
print('°°°°'*15)

print('JO')
sleep(1)
print('KEN')
sleep(1)
print(f'PÔ')
sleep(1)

#1 == pedra 2 == papel 3 == tesoura 
#cpu = [1,2,3] eu ia usar com o choise() mas é mais prático usar on randint
opcpu = randint(1,3)

if opcpu == op:
    if opcpu == 1:
        print('CPU jogou: pedra') 
    elif opcpu == 2:
        print('CPU jogou: papel') 
    elif opcpu == 3:
        print('CPU jogou: tesoura' )
    print('Deu empate!!! tente novamente' )

elif op == 1  and opcpu == 2:
    print('CPU jogou: papel')
    print('CPU venceu!!')
elif op == 1 and opcpu == 3:
    print('CPU jogou: tesoura')
    print('Você venceu!!!')

elif op == 2 and opcpu == 1:
     print('CPU jogou: pedra')
     print('você venceu!!!')
elif op == 2 and opcpu == 3:
     print('CPU jogou: tesoura')
     print('CPU venceu!!!')

elif op == 3 and opcpu == 1:
     print('CPU jogou: pedra')
     print('CPU venceu!!')
elif op ==3 and opcpu == 2:
     print('CPU jogou: papel')
     print('você venceu!!!')

else:
    print('digite uma opção váalida ou verifique as probabilidades')

print('°°°°'*15)
