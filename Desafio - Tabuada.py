#Faça um programa qua leia um numero Inteiro qualquer e mostre na tela a sua tabuada.

tabuada = int(input('Digite um valor para apresentar a tabuada: '))

for count in range(10):
    print('%d x %d = %d' % (tabuada, count + 1, tabuada * (count + 1)))