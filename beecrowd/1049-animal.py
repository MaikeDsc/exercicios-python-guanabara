
tipo = str(input().upper())
subtipo = str(input().upper())
alimento=str(input().upper())

if tipo == 'VERTEBRADO':

    if subtipo == 'AVE':
        if alimento == 'CARNIVORO':
            print('aguia')
        elif alimento == 'ONIVORO':
             print('pomba')

    elif subtipo == 'MAMIFERO':
        if alimento == 'ONIVORO':
            print('homem')
        elif alimento =='HERBIVORO':
            print('vaca')
           
elif tipo =='INVERTEBRADO':
    if subtipo == 'INSETO':
        if alimento == 'HEMATOFAGO':
            print('pulga')
        elif alimento == 'HERBIVORO':
            print('lagarta')
    elif subtipo == 'ANELIDEO':
        if alimento == 'HEMATOFAGO':
            print('sanguessuga')
        elif alimento == 'ONIVORO':
            print('minhoca')
        