ordenados = []
for c in range (5):
    num = int(input(f'informe o {c+1}º número: '))

    if c == 0 or num > ordenados [-1]:
        ordenados.append(num)
    
    else:
        pos =  0
        while pos <= len(ordenados):
            if num <= ordenados[pos]:
                ordenados.insert(pos, num)
                break 
            pos += 1
print('-=-'*15)
print(f'lista ordenada sem usar .sort()',ordenados)
print('-=-'*15)