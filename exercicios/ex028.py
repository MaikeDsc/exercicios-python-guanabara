import random 
numus = int(input('Tente adivinhar um número entre 0 e 5: '))
num = random.randint(0, 5)

if num==numus:
    print(f'Parabéns {num} é o número que escolhi!!')
else:
    print(f'O número era {num}, tente novamente! :(')
print('----FIM----')