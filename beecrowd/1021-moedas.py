'''Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário. A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. A seguir mostre a relação de notas necessárias.
'''
total = float(input())

n100 = int(total // 100)
sobra100 = total % 100

n50 = int(sobra100 // 50)
sobra50 = sobra100 % 50

n20 = int(sobra50 // 20)
sobra20 = sobra50 % 20

n10 = int(sobra20 // 10)
sobra10 = sobra20 % 10

n5 = int(sobra10 // 5)
sobra5 = sobra10% 5

n2 = int(sobra5//2)

print('NOTAS:')
print(f'{n100} nota(s) de R$ 100.00')
print(f'{n50} nota(s) de R$ 50.00')
print(f'{n20} nota(s) de R$ 20.00')
print(f'{n10} nota(s) de R$ 10.00')
print(f'{n5} nota(s) de R$ 5.00')
print(f'{n2} nota(s) de R$ 2.00')

m1 = int(sobra5%2)


partf= int((total-int(total))*100)



m50= partf//50
restom50=partf%50

m25= restom50//25
restom25 = restom50%25

m10 = restom25//10
restom10 = restom25%10

m5 = restom10//5
restom5=restom10%5

print('MOEDAS:')
print(f'{m1} moeda(s) de R$ 1.00')
print(f'{m50} moeda(s) de R$ 0.50')
print(f'{m25} moeda(s) de R$ 0.25')
print(f'{m10} moeda(s) de R$ 0.10')
print(f'{m5} moeda(s) de R$ 0.05')
print(f'{restom5} moeda(s) de R$ 0.01')
