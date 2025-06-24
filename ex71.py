cont = 0
while True:
    n = int(input('Digite um número para ver sua tabuada: '))
    print('-'*40)
    if n < 0:
        break
    for cont in range(0, 11):
        print('{} x {} = {}'.format(n, cont, n*cont))
    print('-' * 40)
print('Programa tabuada encerrado. Volte Sempre!')