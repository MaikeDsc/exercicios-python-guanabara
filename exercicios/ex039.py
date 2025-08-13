from datetime import date
print('###'*15)
print('Programa de alistamento militar Brasileiro.')
print('###'*15)
anasc = int(input('Informe a seu ano de nascimento: '))

anoatual = date.today().year
idade = anoatual-anasc

if idade == 18:
    print('este ano você completa 18 anos, é hora de se alistar!')
elif idade < 18:
    print(f'você ainda não tem 18 anos falta(am) {18-idade} ano(os) para você se alistar, mantenha a calma.')
elif idade >19:
    print(f'você ja estrapolou a idade obrigatória a {idade-18} anos, procure uma base militar próxima e pague a multa.')
