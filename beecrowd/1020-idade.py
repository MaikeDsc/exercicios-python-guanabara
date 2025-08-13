'''Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias

Obs.: apenas para facilitar o cálculo, considere todo ano com 365 dias e todo mês com 30 dias. Nos casos de teste nunca haverá uma situação que permite 12 meses e alguns dias, como 360, 363 ou 364. Este é apenas um exercício com objetivo de testar raciocínio matemático simples.

Exemplo de Entrada	    Exemplo de Saída
        400             1 ano(s)
                        1 mes(es)
                        5 dia(s)'''

idias = int(input())

anos = idias//365
meses= (idias%365)//30
dias = (idias%365)%30

print(f'{anos} ano(s)')
print(f'{meses} mes(es)')
print(f'{dias} dia(s)')