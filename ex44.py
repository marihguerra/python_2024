from time import sleep
print('='*4, 'LOJAS PERNAMBUCO', '='*4)
preco = float(input('Preço do produto: R$'))
print('Selecione a formas de pagamento: ')
sleep(0.5)
print('''[ 1 ] À vista em dinheiro
[ 2 ] À vista no cartão
[ 3 ] Em até 2x no cartão sem juros
[ 4 ] 3x ou mais no cartão com juros
[ 5 ] Cheque ''')
sleep(1)
opcao = int(input('Sua opção: '))
if opcao == 1:
    desconto = preco * 0.1
    sleep(0.5)
    print('A forma de pagamento escolhida garante 10% de desconto, o equivalente a R${:.2f}.\n'
          'O valor final de sua compra é de R${:.2f}.'.format(desconto, preco - desconto))
elif opcao == 2:
    desconto = preco * 0.05
    sleep(0.5)
    print('A forma de pagamento escolhida garante 5% de desconto, o equivalente a R${:.2f}.\n'
          'O valor final de sua compra é de R${:.2f}.'.format(desconto, preco - desconto))
elif opcao == 3:
    parcela = preco / 2
    sleep(0.5)
    print('Sua compra será parcelada em 2x de R${:.2f} SEM descontos ou juros.\n'
          'O valor final de sua compra é de R${:.2f}.'.format(parcela, preco))
elif opcao == 4:
    nparcelas = int(input('Número de parcelas: '))
    precojuros = preco * 1.2
    parcela = precojuros / nparcelas
    sleep(0.5)
    print('Sua compra será parcelada em {}x de R${:.2f} COM juros.\n'
          'O valor final de sua compra é de R${:.2f}.'.format(nparcelas, parcela, precojuros))
elif opcao == 5:
    desconto = preco * 0.1
    sleep(0.5)
    print('A forma de pagamento escolhida garante 10% de desconto, o equivalente a R${:.2f}.\n'
          'O valor final de sua compra é de R${:.2f}.'.format(desconto, preco - desconto))
else:
    print('Opção inválida. Tente novamente.')