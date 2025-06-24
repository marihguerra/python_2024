from time import sleep
print('='*4, 'CALCULADORA DE IMC', '='*4)
print('( índice de massa corporal )')
sleep(1)
massa = float(input('Insira a massa corporal (Kg): '))
altura = float(input('Insira a altura (m): '))
imc = massa / (altura ** 2)
print('O IMC dessa pessoa corresponde à {:.1f}. Ela está '.format(imc), end='')
if imc < 18.5:
    print('ABAIXO DO PESO')
elif 18.5 <= imc < 25:
    print('dentro do PESO IDEAL')
elif 25 <= imc < 30:
    print('com SOBREPESO')
elif 30 <= imc <= 40:
    print('com OBESIDADE')
elif imc > 40:
    print('com OBESIDADE MÓRBIDA')
