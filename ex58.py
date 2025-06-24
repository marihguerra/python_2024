totidade = 0
nomevelho = ''
idadevelho = 0
qtdnova = 0
nomenovas = []
for p in range(1, 5):
    print('-'*4, '{}ª PESSOA'.format(p), '-'*4)
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    genero = str(input('Gênero (M/F): ')).strip().upper()
    totidade += idade
    if genero == 'M':
        if p == 1:
            nomevelho = nome
            idadevelho = idade
        else:
            if idade > idadevelho:
                nomevelho = nome
                idadevelho = idade
    if genero == 'F' and idade < 20:
        qtdnova += 1
        nomenovas.append(nome)
print('\n→ A média de idade do grupo é de {:.0f} anos.'.format(totidade / 4))
print('   O homem mais velho se chama {} e tem {} anos.'.format(nomevelho, idadevelho))
print('   Ao todo são {} mulher(es) com menos de 20 anos, {}.'
      .format(qtdnova, ', '.join(nomenovas)))