# Escreva um programa que Faça o computador "pensar" em um número inteiro entre O a 5 a peça para o usuário tentar descobrir qual foi o número
# escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
numberMachine = random.randint(1,5)
numberUser = int(input('Digite um número inteiro qualquer entre 1 e 5: '))
if numberMachine == numberUser:
    print('\033[32mVocê Venceu da Máquina! O Número da Sorteado pela Máquina foi {} e seu número digitado foi {}\033[m'.format(numberMachine,numberUser))
else:
    print('\033[31mVocê Perdeu para a Máquina! O Número da Sorteado pela Máquina foi: {} e seu número digitado foi: {}\033[m'.format(numberMachine,numberUser))