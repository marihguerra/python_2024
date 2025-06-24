import random
num = random.randint(0, 10)
tentativas = 1
print('Sou seu computador...\nAcabei de pensar em um número de 0 a 10.')
adivinha = int(input('Você consegue adivinhar qual foi? '))
while adivinha != num:
    if adivinha < num:
        adivinha = int(input('Mais...Tente mais uma vez: '))
    elif adivinha > num:
        adivinha = int(input('Menos...Tente mais uma vez: '))
    tentativas += 1
print('Parabéns, você conseguiu adivinhar! Eu pensei no número {}!\nForam necessárias {} tentativa(s) para você '
      'acertar.'.format(num, tentativas))