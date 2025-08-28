palavras = ('maquiavel','quadrado','cubo','carteira','rap','musica','video')

for c in palavras:
    print(f'A palavra {c.upper()} contemém as vogais: ',end ='')
    for letra in c:
        if letra in 'aeiou':
            print(letra, end=' ')

    print()         

        
    