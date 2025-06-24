op = 'S'
soma = 0
while op == 'S':
   num = int(input('Digite um número inteiro para somar: '))
   soma += num
   print('Soma: ', soma)
   op = str(input('Deseja continuar? (S/N) ')).upper()
print('FIM')