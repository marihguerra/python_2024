op = ''
maiores = homens = novas = 0
print('-' * 25)
print('   CADASTRE UMA PESSOA')
while True:
    print('-'*25)
    idade = int(input('Idade: '))
    genero = str(input('Gênero (F/M): ')).strip()
    if idade >= 18:
        maiores += 1
    if genero in 'Mm':
        homens += 1
    elif genero in 'Ff':
        if idade < 20:
            novas += 1
    op = str(input('Quer cadastrar mais uma pessoa? (S/N) ')).strip()
    if op in 'Nn':
        break
print('\n-DADOS-')
print(f'Total de pessoas maiores de 18: {maiores}.')
print(f'Ao todo temos {homens} homem(ns) cadastrado(s).')
print(f'Ao todo temos {novas} mulher(es) com menos de 20 anos.')