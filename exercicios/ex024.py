cidade = input('informe o nome da cidade: ').strip()
cidade = cidade.upper().split()
cidade = cidade[0]
resp='SANTO'in cidade
print(f'é {resp} que a cidade começa com santo')