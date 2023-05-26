# Cria um algoritmo qua leia um numero a mostre o seu dobro, triplo a raiz quadrada.

numero = float(input('Digite um número: '))
dobro = numero * 2
triplo = numero * 3
raiz = numero ** 0.5

print(' O dobro do valor digitado é {}.\n Já o seu triplo será {}.\n Para concluir a raiz de seu número é {:.35f}:'.format(dobro,triplo,raiz))