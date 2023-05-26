# Faça um programa que leia um número de O a 999 e mostre na tela cada um dos dígitos separados.
# Exe: Digite um número:
# unidade: 4
# dezena: 3
# centena: 8
# milhar: 1

numero = input('Digite um número de 0 a 999: ')
print('Sua unidade é: {}'.format(numero[3]))
print('Sua dezena é: {}'.format(numero[2]))
print('Sua centena é: {}'.format(numero[1]))
print('seu milhar é: {}'.format(numero[0]))