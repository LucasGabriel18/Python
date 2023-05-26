#Escrava um programa que leia um número inteiro qualquer a peça para o usuário escolhar qual será a basa da convarsao:
# -1 binário
# -2 para octal
# -3 para hexadecimal

number = int(input('Digite um Número Inteiro para Conversão: '))
base = int(input('Digite a forma de conversão desejada. Digite [1] para Conversão Binária, Digite [2] para Conversão Octal e Digite [3] para Conversão Hexadecimal. '))

if base == 1:
    binario = bin(number)
    print('A conversão do número {} para Binário é {}'.format(number, binario[2:]))
elif base == 2:
    octal = oct(number)
    print('A conversão do número {} para Octal é {}'.format(number, octal[2:]))
elif base == 3:
    hexa = hex(number)
    print('A conversão do número {} para Hexadecimal é {}'.format(number, hexa[2:]))
else:
    print('Número Digitado é Inválido!')