print('===Conversor de Medidas===')
m = float(input('Digite uma medida em metros: '))
km = m * 10 ** -3
hm = m * 10 ** -2
dam = m * (10 ** -1)
dm = m * 10
cm = m * 10 ** 2
mm = m * 10 ** 3
print('A medida de {:.2f} corresponde a: '.format(m))
print('-' * 15, ' \n{} quilômetros \n{} hectômetros \n{} decâmetros \n{} decímetros \n'
      '{} centímetros \n{} milímetros'.format(km, hm, dam, dm, cm, mm))