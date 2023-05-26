# Faça um programa que leia o ano do nascimento de um jovem e informe, de acordo com sua idade:
# — Se ele ainda vai se alistar ao serviÇo militar.
# — Se é a hora de se alistar.
# — Sa já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tampo qua Falta ou que passou do prazo.

from datetime import date
atual = date.today().year
Nascimento = int(input('Digite o Ano do seu Nascimento: '))
idade = atual - Nascimento

print('Quem nasceu em {} tem {} anos de idade em {}'.format(Nascimento, idade, atual))

if idade == 18:
    print('Você deve se Alistar \033[31mIMEDIATAMENTE!')
elif idade < 18:
    Faltaidade = 18 - idade
    print('Ainda faltam\033[32m {} ano(s)\033[m para o seu Alistamento.'.format(Faltaidade))
    ano = atual + Faltaidade
    print('O seu alistamento será no ano de {}'.format(ano))
elif idade > 18:
    Faltaidade = idade - 18
    print('Você já deveria ter se alistado há {} anos'.format(Faltaidade))
    ano = atual - Faltaidade
    print('O seu Alistamento foi no ano de \033[33m{}'.format(ano))
