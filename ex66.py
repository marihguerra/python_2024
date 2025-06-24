print('='*35, '\n  GERADOR DE TERMOS DE UMA P.A.')
print('='*35)
n = int(input('Primeiro termo: '))
r = int(input('Razão: '))
termo = n
cont = 1
mais = 10
total = 0
while mais != 0:
    total += mais
    while cont < total + 1:
        print('Termo {} → {}'.format(cont, termo))
        termo += r
        cont += 1
    print('== PAUSA ==')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos.'.format(total))
print('='*40)
print(' FIM')