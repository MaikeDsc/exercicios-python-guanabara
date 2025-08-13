from datetime import date
ano = int(input('informe um ano ou digite 1 para saber se o ano atual pé bissexto: '))
if ano==1:
     ano= date.today().year
if ano%4 ==0 and ano%100 !=0 or ano%400==0:

     print(f'o ano {ano} é bissexto!!')
   
else:
    print(f'o ano {ano} NÃO é bissexto!!')