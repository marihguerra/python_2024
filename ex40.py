from time import sleep
num = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão: ')
print('''[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
sleep(1)
base = int(input('Sua opção: '))
if base == 1:
    print('{} convertido para BINÁRIO é igual a {} .'.format(num, bin(num)[2:]))
elif base == 2:
    octal = 2
    print('{} convertido para OCTAL é igual a {} .'.format(num, oct(num)[2:]))
elif base == 3:
    hexa = 3
    print('{} convertido para OCTAL é igual a {} .'.format(num, hex(num)[2:]))
else:
    print('Opção inválida. Tente novamente.')