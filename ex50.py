som = 0
cont = 0
print('Números ímpares múltiplos de 3 no intervalo de 1 a 500:\n')
for c in range(1, 501, 2):
    if c % 3 == 0:
        print(c, '-', end='')
        som = som + c
        cont += 1
print('\n\nA soma dos {} valores obtidos é {}.'.format(cont, som))