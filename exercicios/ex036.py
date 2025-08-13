print('\033[1;32m-<->-'*10)
print('SIMULE SEU EMPRÉSTIMO AGORA E COMPRE A SUA CASA')
print('-<->-'*10)

vcasa = float(input('Informe o valor da casa: '))
vsalario = float(input('Informe o valor do seu salário: '))
anos = int(input('Informe em quantos anos voce pretende pagar: \033[m'))

prest = vcasa/(anos*12)
if prest < 0.3*vsalario:
    print(f'parabés o empréstimo foi aprovado! em parcelas de R${prest:.2f} ao mês!')
else:
    print(f'infelizmente o emprestimo não foi aprovado. ',end='')
    print(f'O valor da prestaçaõ de R${prest:.2f} é maior que 30% do seu salário.')