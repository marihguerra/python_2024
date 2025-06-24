print('='*35, '\n  10 PRIMEIROS TERMOS DE UMA P.A.')
print('='*35)
n = int(input('Primeiro termo: '))
r = int(input('Razão: '))
for c in range(1, 11):
    a = n + (c - 1) * r
    print('Termo {} → {}'.format(c, a))
print('='*35)
# or for c in range(n, n *(r * 10), r):
#   print('Termo → {}'.format(c))
