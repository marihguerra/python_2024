n = int(input('Digite um número para ver sua tabuada: '))
cont = 0
for c in range(0, 11):
    print('\n{} x {} = {}'.format(n, c, n*c))
print('\nFIM da tabuada')