print('-'*32)
print('       LOJA SUPER BARATÃO')
print('-'*32)
p = total = caros = 0
maisbarato = ''
precomaisbarato = 0
while True:
    produto = str(input('Nome do produto: ')).strip()
    preco = float(input('Preço: R$'))
    p += 1
    total += preco
    if p == 1 or preco < precomaisbarato:
        maisbarato = produto
        precomaisbarato = preco
    if preco > 1000.0:
        caros += 1
    op = str(input('Deseja adicionar mais produtos? (S/N) ')).upper().strip()
    if op == 'N':
        break
print('\n', '-'*8, 'FIM DA COMPRA', '-'*8)
print(f'O total da compra foi de R${total:.2f}.')
print(f'Temos {caros} produto(s) custando mais de R$1000.00.')
print(f'O produto mais barato da compra foi {maisbarato}, custando R${precomaisbarato:.2f}.')