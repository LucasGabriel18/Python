# Escreva um programa que leia dois números inteiros e compare—os, mostrando na tela uma mensagem:
# -o primeiro valor é maior.
# -o segundo valor é maior
# — Não existe valor maior, os dois são iguais.

numero1 = int(input('Digite um Número Inteiro: '))
numero2 = int(input('Digite outro Número Inteiro: '))

if numero1 > numero2:
    print('O PRIMEIRO número é MAIOR!')
elif numero2 > numero1:
    print('O SEGUNDO número é MAIOR!')
elif numero1 == numero2:
    print('O DOIS número são IGUAIS!')