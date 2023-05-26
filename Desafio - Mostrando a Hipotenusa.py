# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente do triângulo ratangulo, calcule a mostre o comprimento da hipotenusa.
from math import hypot # Chamando a biblioteca e solicitando a função especifica hypot
catOposto = float(input('Digite o Valor do Cateto Oposto: ')) # Solicitando o valor de cateto oposto e aramzenando na variável catOposto
catAdj = float(input('Digite o Valor do Cateto Adjacente: ')) # Solicitando o valor de cateto adjacente e aramzenando na variável catAdj
hipotenusa = hypot(catOposto,catAdj) # Adicionando o valor de retorno da função a variável hipotenusa

print('O valor da Hipotenusa será: {:.2f}'.format(hipotenusa)) # Escrevendo para o usuário o valor da hipotenusa e deixando apenas duas casas depois da virgula {:.2f}
