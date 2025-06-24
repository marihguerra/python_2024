print('='*25)
print('{:^25}'.format('BANCO MHG'))
print('='*25)
ced = 100
totced = 0
dinheiro = int(input('Quanto dinheiro você quer sacar? R$'))
while True:
    if dinheiro >= ced:
        dinheiro -= ced
        totced += 1
    else:
        if totced > 0:
            print('Total de {} cédulas de R${}.'.format(totced, ced))
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 2
        elif ced == 2:
            ced = 1
        totced = 0
        if dinheiro == 0:
            break
print('='*30)
print('Tenha um bom dia! Volte Sempre ao Banco MHG!')