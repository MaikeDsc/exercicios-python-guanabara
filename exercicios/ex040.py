n1 = float(input('Informe a primeira nota do aluno N1: '))
p1 = float(input('informe o peso de N1: '))
n2 = float(input('Informe a segunda nota do aluno N2: '))
p2 = float(input('informe o peso de N2: '))
n3 = float(input('informe a terceira notanota 3 N3: '))
p3 = float(input('informe o peso de N3: '))

mediap = (n1*p1 + n2*p2 + n3*p3)/(p1+p2+p3)

if mediap >= 7:
    print(f'a sua média é {mediap:.2f}, parabéns você foi aprovado!')
elif 7> mediap  >= 5:
    print(f'sua média é {mediap:.2f}, você está na PF. Estude bastante!')
elif mediap < 5:
    print(f'sua média é {mediap:.2f}, infelizmente você foi reprovado! :(')
