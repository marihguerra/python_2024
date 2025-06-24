sp = 0
si = 0
for c in range(0, 6):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        sp = sp + n
    else:
        si = si + n
print('A soma dos números \033[1mpares\033[m digitados é {} e a soma dos números \033[1mímpares\033[m é {}.'
      .format(sp, si))