# Faça um programa qua leia um numero Inteiro a mostre na tela o seu sucessor a seu antecessor.

numero = int(input('Digite um valor qualquer: '))
ant = numero - 1
suc = numero + 1
print('O valor antecessor será: {}. Já o valor sucessor é: {}.'.format(ant, suc))