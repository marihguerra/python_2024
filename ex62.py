genero = str(input('Informe seu gênero (M/F): ')).strip().upper()[0]
while genero not in 'MF':
    genero = str(input('Dados inválidos. Informe seu gênero (M/F): ')).strip().upper()[0]
print('Obrigado! seu gênero {} foi registrado com sucesso.'.format(genero))