print('Detector de palíndromos')
frase = str(input('Digite uma frase: ')).upper()
tudojunto = ''.join(frase.split())
inverso = ''
for c in range(len(tudojunto) - 1, -1, -1):
    inverso += tudojunto[c]
print('O inverso da frase {} é {}.'.format(tudojunto, inverso))
if tudojunto == inverso:
    print('Logo, ela É um PALÍNDROMO!')
else:
    print('Então ela NÃO É um palíndromo.')
#ou
#inverso = tudojunto[::-1]
