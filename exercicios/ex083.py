expressao = str(input())
abrindo = fechando = 0
for c in expressao:
    if c  in '(':
        abrindo += 1
    if c in ')':
        fechando += 1
 
print('Expressão válida' if abrindo == fechando else 'Expressão inválida' )
