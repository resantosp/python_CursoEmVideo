print(('='*10), ' ALUGEL DE CARROS ', ('='*10))
dias = int(input('Por quantos dias foi alugado? '))
km = float(input('Quantos quilômetros foram percorridos? '))
vtotal = (dias*60) + (km*0.15)
print('\n', ('='*45), '\n O valor total a ser pago é de R${:.2f}.'.format(vtotal), '\n', ('='*45))