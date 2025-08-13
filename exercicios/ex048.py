print('somatório entre os ímapares multiplos de 3 no intervalo de 1 a 500')
somatorio = 0
for c in range(1, 501, 2):
    if c % 3 == 0 :
        somatorio += c
print('somatório = ',somatorio)