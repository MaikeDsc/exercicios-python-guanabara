x, y, z = map(int, input().split())

maiorxy = (x+y+abs(x-y))/2
maiorxycomz = (maiorxy+z+abs(maiorxy-z))/2
maior = int(maiorxycomz)
print(f'{maior} eh o maior')
