n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
n3 = float(input('Terceira nota do aluno: '))
media = (n1 + n2 + n3) / 3
print('A média das três notas desse aluno foi \033[1m{:.1f}\033[m.'.format(media))
if media < 5.0:
    print('O aluno foi \033[1;31mreprovado\033[m na matéria.')
elif 5.0 <= media < 7.0:
    print('O aluno está de \033[1;33mrecuperação\033[m na matéria.')
elif media >= 7.0:
    print('O aluno foi \033[1;32maprovado\033[m na matéria.')