print('\033[1mVerificador de números primos\033[m')
n = int(input('Digite um número: '))
totdiv = 0
print('→', end='')
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[1;32m', end=' ')
        totdiv += 1
    else:
        print('\033[0;31m', end=' ')
    print(c, end=' ')
if totdiv == 2:
    print('\n\033[mO número {} foi divisível apenas 2 vezes;'.format(n, totdiv))
    print('Logo, ele é \033[1mprimo!')
else:
    print('\n\033[mO número {} foi divisível {} vezes;'.format(n, totdiv))
    print('Logo, ele \033[1mnão\033[m é primo.')