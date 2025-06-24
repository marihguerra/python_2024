print('~'*25, '\n Sequência de Fibonacci')
print('~'*25)
termos = int(input('Quantos termos você deseja mostrar? '))
t1 = 0
t2 = 1
print(' {} → {} →'.format(t1, t2), end='')
cont = 3
while cont < termos + 1:
    t3 = t1 + t2
    print(' {} →'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' FIM')
print('~'*30)