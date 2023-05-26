# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR

number = int(input('Digite um número Inteiro: '))
resto = number % 2

if resto == 0:
    print(f'O Número \033[4;36m{number}\033[m é Par!')
else:
    print(f'O número \033[4;33m{number}\033[m é Impar!')