#palimdromo 

frase = str(input('digite uma frase: ')).strip().upper()
frase = ''.join(frase).split()

pjuntas = []

for sep in frase:
    pjuntas += sep


invertida = pjuntas[::-1]

if (pjuntas)==(invertida):
    print('A frase é um palímdromo.')
else:
    print('a frase NÃO é um palímdromo')