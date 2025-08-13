salario = float(input('informe o salário: '))
if salario <= 1518:
    aumento = salario + salario * 0.15
    print(f'o salario agora será R${aumento:.2f} reais.')
else:
    aumento = salario +salario * 0.10
    print(f'o slário agora será de R${aumento:.2f} reais.')