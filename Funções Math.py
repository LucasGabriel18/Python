from math import sqrt, floor

numero = int(input('Digite uma valor: '))
raiz = sqrt(numero)

print('A raiz quadrada de {} é {:.2f}'.format(numero, floor(raiz)))