risco = input('Digite BX ou AL para o grau de risco: ')
if risco != 'BX' and risco != 'AL':
    print(f'{risco} digite novamente')
    risco
    
else:
    valor = float(input('Digite o valor: '))
    if risco == 'BX':
        if valor < 1000.0:
            tip = 'Poupanca'
        else:
            tipo = 'Renda Fixa'
    else:
        if valor < 1000.00:
            tipo = 'Biticoins'
        else:
            tipo = "acoes"
    print(f'Vocew deve investir em {tipo}')
