from datetime import date
anasc = int(input('informe a data de nascimento do atleta: '))

idade = (date.today().year) - anasc

if idade <= 9:
    print(f'o atlea possui {idade} anos e competirá na categotria MIRIM')
elif idade <=14:
    print(f'o atlea possui {idade} anos e competirá na categotria INFANTIL')
elif idade <=19:
    print(f'o atlea possui {idade} anos e competirá na categotria JUNIOR')
elif idade <=25:
    print(f'o atlea possui {idade} anos e competirá na categotria SÊNIOR')
elif idade >25:
    print(f'fo atlea possui {idade} anos e competirá na categotria MASTER')