#Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas
# O nome com todas minusculas.
# Quantas letras ao todo (sem considerar espaços).
# Quantas letras tem o primeiro nome.

nomeC = str(input('Digite o seu Nome Completo: '))
maisculas = nomeC.upper()
minusculas = nomeC.lower()
LetrasTot = len(nomeC)
PNome = nomeC.split()


print('->', 'O Nome com Todas as Letras Maiúsculas fica: {}'.format(maisculas))
print('->', 'O Nome com Todas as Letras Minúsculas fica: {}'.format(minusculas))
print('->', 'A quantidade de Letras ao Total Sem Considerar Espaço é: {}'.format(LetrasTot))
print('->', 'O Primeiro Nome Inserido é: {}'.format(PNome[0]))

