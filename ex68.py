cont = 0
soma = 0
n = int(input('Digite um número (999 para parar): '))
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um número: '))
print('Você digitou {} números e soma deles é {}.'.format(cont, soma))
# ou
#cont = soma = n = 0
#while n != 999:
#    n = int(input('Digite um número (999 para parar): '))
#    if n != 999:
#        soma += n
#        cont += 1