from datetime import date
from time import sleep
print('== VERIFICAÇÃO DE ALISTAMENTO AO SERVIÇO MILITAR ==')
nasc = int(input('Insira seu ano de nascimento: '))
idade = date.today().year - nasc
alistamento = nasc + 18
sleep(1)
print('Você tem {} anos atualmente ({}).'.format(idade, date.today().year))
if idade < 18:
    diferenca = 18 - idade
    print('Ainda faltam {} ano(s) para seu alistamento, desse modo seu alistamento será em {}.'
          .format(diferenca, alistamento))
elif idade == 18:
    print('Você deverá se alistar no serviço militar \033[4mimediatamente\033[m antes que complete 19 anos.')
else:
    diferenca = idade - 18
    print('Você deveria ter se alistado há {} ano(s), no ano de {}.'.format(diferenca, alistamento))