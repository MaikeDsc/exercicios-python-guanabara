pesos = []
for c in range(5):
    pesos.append(int(input(f'informe o peso da {c+1}ª pessoa:')))
print('menor peso:', min(pesos))
print('maior peso:', max(pesos))