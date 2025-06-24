from random import randint
from emoji import emojize
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
for c in range(0, 3):
    print('-='*4, '\033[1;31mJO\033[m\033[1m-\033[m\033[1;35mKEN\033[m\033[1m-\033[m\033[1;33mPÔ\033[m\033[1m!\033[m',
          '-='*5)
    print('Suas opções:')
    print('[ 0 ] PEDRA', emojize(":raised_fist:"))
    print('[ 1 ] PAPEL', emojize(":hand_with_fingers_splayed:"))
    print('[ 2 ] TESOURA', emojize(":victory_hand:"))
    sleep(1)
    jogador = int(input('Qual é a sua jogada? '))
    #print(random.choice(itens)) or
    computador = randint(0, 2)
    print('-='*15)
    sleep(1)
    if computador == 0:
        if jogador == 0:
            print('          ', emojize(":raised_fist:"), 'X', emojize(":raised_fist:"))
            print('\033[1;33mEMPATE !\033[m')
        elif jogador == 1:
            print('          ', emojize(":hand_with_fingers_splayed:"), 'X', emojize(":raised_fist:"))
            print('\033[1;33mVocê GANHOU !!!\033[m')
        elif jogador == 2:
            print('          ', emojize(":victory_hand:"), 'X', emojize(":raised_fist:"))
            print('\033[1;33mVocê PERDEU\033[m')
    elif computador == 1:
        if jogador == 0:
            print('          ', emojize(":raised_fist:"), 'X', emojize(":hand_with_fingers_splayed:"))
            print('\033[1;33mVocê PERDEU\033[m')
        elif jogador == 1:
            print('          ', emojize(":hand_with_fingers_splayed:"), 'X', emojize(":hand_with_fingers_splayed:"))
            print('\033[1;33mEMPATE !\033[m')
        elif jogador == 2:
            print('          ', emojize(":victory_hand:"), 'X', emojize(":hand_with_fingers_splayed:"))
            print('\033[1;33mVocê GANHOU !!!\033[m')
    elif computador == 2:
        if jogador == 0:
            print('          ', emojize(":raised_fist:"), 'X', emojize(":victory_hand:"))
            print('\033[1;33mVocê GANHOU !!!\033[m')
        elif jogador == 1:
            print('          ', emojize(":hand_with_fingers_splayed:"), 'X', emojize(":victory_hand:"))
            print('\033[1;33mVocê PERDEU\033[m')
        elif jogador == 2:
            print('          ', emojize(":victory_hand:"), 'X', emojize(":victory_hand:"))
            print('\033[1;33mEMPATE !\033[m')
    print('\033[31mJogador\033[m escolheu {}'.format(itens[jogador]))
    print('\033[35mComputador\033[m escolheu {}'.format(itens[computador]))
    print('-='*15)
    sleep(2)
print('FIM')