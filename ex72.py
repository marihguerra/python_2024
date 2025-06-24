from random import randint
print('        \033[1mPAR OU ÍMPAR\033[m')
vitorias = 0
while True:
    print('=-='*9)
    op = str(input('PAR ou ÍMPAR? (P/I) ')).upper().strip()
    escolha = ''
    if op == 'P':
        escolha = 'par'
    elif op == 'I':
        escolha = 'ímpar'
    njogador = int(input(f'Digite o número {escolha}: '))
    ncomputador = randint(0, 10)
    print('-'*30)
    print('Você jogou {} e o computador jogou {}.'.format(njogador, ncomputador))
    soma = njogador + ncomputador
    if soma % 2 == 0:
        print('{} + {} = {}, que é PAR!'.format(njogador, ncomputador, soma))
        if op == 'P':
            vitorias += 1
            print('\033[1mVOCÊ VENCEU!!\033[m')
            print('Vamos jogar novamente...')
        elif op == 'I':
            print('\033[1mGAME OVER\033[m.')
            break
    else:
        print('{} + {} = {}, que é ÍMPAR!'.format(njogador, ncomputador, soma))
        if op == 'I':
            vitorias += 1
            print('\033[1mVOCÊ VENCEU!!\033[m')
            print('Vamos jogar novamente...')
        elif op == 'P':
            print('\033[1mGAME OVER\033[m.')
            break
print(f'Você venceu {vitorias} vezes.')
print('=-='*9)