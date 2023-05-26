# CriE um programa quE Faça o computador jogar Jokenpô com você.
import random
from time import sleep
jokenpo = ['Pedra', 'Papel', 'Tesoura']
computador = random.randint(0, 2)

print('{:=^40}'.format('JOKENPÔ'))
print('''Você está pronto para o Desafio?:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Digite a sua Jogada: '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('POO!!')

print('-=' * 10)
print('Computador jogou {}'.format(jokenpo[computador]))
print('O Jogador jogou {}'.format(jokenpo[jogador]))
print('-=' * 10)

if computador == 0: # Computador Jogou Pedra
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCEU')
    elif jogador ==2:
        print('COMPUTADOR VENCEU')
    else:
        print('\033[mJogada Inválida!') # Computador Jogou Papel
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador ==2:
        print('JOGADOR VENCEU')
    else:
        print('\033[mJogada Inválida!')
elif computador == 2: # Computador Jogou Tesoura
    if jogador == 0:
        print('JOGADOR VENCEU')
    elif jogador == 1:
        print('COMPUTADOR VENCEU')
    elif jogador ==2:
        print('EMPATE')
    else:
        print('\033[mJogada Inválida!')