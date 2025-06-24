from time import sleep
n1 = int(input('Digite um primeiro valor: '))
n2 = int(input('Digite um segundo valor: '))
sair = False
while not sair:
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Menor e maior
    [ 4 ] Novos números 
    [ 5 ] Sair do programa''')
    sleep(0.5)
    op = int(input('>>>> Qual sua opção? '))
    if op == 1:
        print('A soma dos números é igual a {}.'.format(n1 + n2))
    elif op == 2:
        print('A multiplicação dos números é igual a {}.'.format(n1 * n2))
    elif op == 3:
        lista = [n1, n2]
        lista.sort()
        print('O menor valor que você digitou foi {} e o maior foi {}.'.format(lista[0], lista[1]))
    elif op == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Digite um primeiro valor: '))
        n2 = int(input('Digite um segundo valor: '))
    elif op == 5:
        sair = True
        print('Finalizando...')
    else:
        print('Opção inválida, tente novamente.')
    sleep(0.5)
    print('-' * 45)
print('Fim do programa. Volte sempre!')