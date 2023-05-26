#Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno,cosseno e tangente dessa angulo.
from math import sin, cos, tan, radians, trunc # Trazendo as funções de seno, cosseno,  tangente, radians (Conversão de angulo par radianos) e trunc para arredondar
angulo = float(input('Digite o Valor do Ângulo: ')) # Solicitando a informação de ângulo para armazenar na variável "angulo".
seno = sin(radians(angulo)) # Função que vai armazenar o retorno do calculo na variável seno.
cosseno = cos(radians(angulo)) # Função que vai armazenar o retorno do calculo na variável cosseno.
tangente = tan(radians(angulo)) # Função que vai armazenar o retorno do calculo na variável tangente.

print('O Ângulo digitado {}º é respectivo ao valor de Seno que é {:.2f} e o Cosseno será {:.2f} e a Tangente é {:.2f}.'.format(trunc(angulo), seno, cosseno, tangente)) # Mostrar o resultado