from time import sleep
print('-'*5, 'CATÁLOGO DE FILMES', '-'*5)

catalogo = [['The Matrix', 'Lilly e Lana Wachowski', '1999', ' Estados Unidos/ Austrália', '136min'],
            ['O Auto da Compadecida', 'Guel Arraes', '2000', 'Brasil', '157min'],
            ['Meia Noite em Paris', 'Woody Allen', '2011', 'Estados Unidos/ Espanha', '94min'],
            ['Shrek Para Sempre', 'Mike Mitchell', '2010', 'Estados Unidos', '93min']]
op = 0

while op != 6:

    sleep(0.5)
    print('''\nMenu.
1. Adicionar filme
2. Remover filme
3. Buscar filme por nome
4. Buscar filme por diretor
5. Listar catálogo completo
6. Fechar programa''')
    sleep(1)
    op = int(input('Entre uma opção: '))
    print('\n', end='')

    if op == 1:
        nome_add = input('Digite o nome do filme: ')
        dir_add = input('Digite o(a) diretor(a): ')
        ano_add = input('Digite o ano: ')
        pais_add = input('Digite o país: ')
        dur_add = input('Digite a duração: ')
        catalogo.append([nome_add, dir_add, ano_add, pais_add, dur_add])
        print('Filme adicionado!')

    elif op == 2:
        nome_remov = input('Digite o nome do filme a ser removido: ')
        for c in range(0, len(catalogo)):
            if catalogo[c][0] == nome_remov:
                del (catalogo[c])
                break
        print('Filme removido!')

    elif op == 3:
        nome_busc = input('Digite o nome do filme buscado: ')
        for c in range(0, len(catalogo)):
            if catalogo[c][0] == nome_busc:
                print('''Filme: {}
    Diretor(a): {}
    Ano: {}
    País: {}
    Duração: {}'''.format(catalogo[c][0], catalogo[c][1], catalogo[c][2], catalogo[c][3], catalogo[c][4]))

    elif op == 4:
        dir_busc = input('Digite o nome do(a) diretor(a) filme buscado: ')
        for c in range(0, len(catalogo)):
            if catalogo[c][1] == dir_busc:
                print('''Filme: {}
            Diretor(a): {}
            Ano: {}
            País: {}
            Duração: {}'''.format(catalogo[c][0], catalogo[c][1], catalogo[c][2], catalogo[c][3], catalogo[c][4]))

    elif op == 5:
        for c in range(0, len(catalogo)):
            print('''Filme: {}
    Diretor(a): {}
    Ano: {}
    País: {}
    Duração: {}'''.format(catalogo[c][0], catalogo[c][1], catalogo[c][2], catalogo[c][3], catalogo[c][4]))

print('Fim do programa.')