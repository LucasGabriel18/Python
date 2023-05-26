# Crie um programa qua leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
import math # Importanto a Biblioteca
numqlqr = float(input('Digite um número qualquer: ')) # Solicitando o usuário para digitar um número e armazenar a informação na variável numqlqr
porcaoInteira = math.trunc(numqlqr) # Fazendo com que a variável porcaoInteiraa receba o valor que a função math.trunc(numqlqr) retornar.

print('O número {} tem a sua porção inteira em {}'. format(numqlqr,porcaoInteira)) # Apresentando o resultado da porção inteira