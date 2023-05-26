# FaÇa um programa que leia uma Frase pelo teclado e mostre:
# Quantas vezes aparece a latra "A"
# Em qua posiÇão ele aparece a última vez.
# Em qua posiÇão ele aparece a primeira vez.

frase = str(input('Digite uma Frase: '))
contador = frase.count('a')
splite = frase.split()
print('A letra "A" aparece {} vezes'.format(contador))
print(splite)
print('A primeira posição que a letra "A" aparece é {}'.format(frase.find('a')+1))
print('A última posição que a letra "A" aparece é {}'.format(frase.rfind('a')+1))