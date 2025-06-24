from datetime import date
maior = 0
menor = 0
for c in range(1, 7):
    ano = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    if ano <= date.today().year - 18:
        maior += 1
    else:
        menor += 1
print('\nAo todo temos {} pessoas maiores de idade e {} menores de idade.'.format(maior, menor))
