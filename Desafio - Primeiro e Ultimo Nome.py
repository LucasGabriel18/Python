#Faça um programa que leia o nome completo de uma pessoa,mostrando em seguida o primeiro e o último nome saparadamente.
#Exemplo: Ana Maria de Souza
# Primeiro: Ana
# Último: Souza

nomeC = str(input('Digite o seu nome completo: '))
plite = nomeC.split()
print(plite)
print('O nome que está na primeira posição é: {}'.format(plite[0]))
PegaU = nomeC.rsplit()
print('O nome que está na última posição é: {}'.format(plite[len(plite)-1]))