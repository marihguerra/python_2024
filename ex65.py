from math import factorial
n = int(input('Digite um número para calcular sua fatorial: '))
f = factorial(n)
print('{}! = '.format(n), end='')
while n > 0:
    print(n, end='')
    print(' x ' if n > 1 else ' ', end='')
    n -= 1
print('= {}'.format(f))