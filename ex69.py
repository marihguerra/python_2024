op = 'S'
soma = cont = 0
valores = []
while op == 'S':
    n = int(input('Digite um número: '))
    valores.append(n)
    valores.sort(reverse=True)
    soma += n
    cont += 1
    op = str(input('Deseja continuar? (S/N) ')).upper()
print('Você digitou {} números e a média entre eles foi {:.2f}.'.format(cont, soma/cont))
print('O maior valor foi {} e o menor valor foi {}.'.format(valores[0], valores[len(valores)-1]))
