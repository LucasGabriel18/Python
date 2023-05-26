#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

num1 = int(input('Digite um Número: '))
num2 = int(input('Digite mais Número: '))
num3 = int(input('Digite outro Número: '))
cores = {'Roxo': '\033[35m',
         'Azul': '\033[34m',
         'Vermelho': '\033[31m',
         'limpa': '\033[m'}

print('Os número digitados foram {}{}{}, {}{}{} e {}{}{}'.format(cores['Roxo'], num1, cores['limpa'], cores['Azul'], num2, cores['limpa'], cores['Vermelho'], num3, cores['limpa']))

maior = num1
if (num2 > maior):
    maior = num2
    if (num3 > maior):
        maior = num3
        print('O número Maior é {}'.format(maior))

        menor = num1
        if(num2 < menor):
            menor = num2
            if(num3 < menor):
                menor = num3
                print('O número menor é {}'.format(menor))