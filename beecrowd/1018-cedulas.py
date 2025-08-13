#notas de 100 50 20 10 5 2 1
valor = int(input())
print(valor)

n100 = valor//100
r100 = valor%100 
print(f'{n100} nota(s) de R$ 100,00')

n50 = r100//50
r50 = r100 % 50
print(f'{n50} nota(s) de R$ 50,00')

n20 = r50//20
r20 = r50%20
print(f'{n20} nota(s) de R$ 20,00')

n10 = r20//10
r10 = r20%10
print(f'{n10} nota(s) de R$ 10,00')

n5 = r10//5
r5 = r10%5
print(f'{n5} nota(s) de R$ 5,00')

n2 = r5//2
r2 = r5%2
print(f'{n2} nota(s) de R$ 2,00')

print(f'{r2} nota(s) de R$ 1,00')