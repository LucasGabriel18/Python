#Faça um programa que leia um ano qualquer e mostra se ele é BISSEXTO.
from datetime import date

year = int(input('Digite um Ano Qualquer: Se quiser validar o Ano Atual se é ou não Bissexto, Digite 0: '))

cores = {'Vermelho': '\033[31m',
         'Verde': '\033[32m',
         'limpa': '\033[m'}

if year == 0:
    year = date.today().year

if year % 4 ==0 and year % 100 != 0 or year % 400 == 0:
    print('O ano {}{}{} é Bissexto.'.format(cores['Verde'], year, cores['limpa']))
else:
    print('O ano {}{}{} não é Bissexto'.format(cores['Vermelho'], year, cores['limpa']))