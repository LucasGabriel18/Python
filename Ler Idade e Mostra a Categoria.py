# A ConFederaÇão Nacional da NataÇão precisa de um programa qua leia o ano da nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - Ate 9 anos : MIRIM
# - Ate 14 anos: INFANTIL
# - Até 19 anos: JUNIOR
# - 20 anos: SÉNIOR
# - Acima: MASTER

from datetime import date

nasc = int(input('Digite o ano do seu Nascimento: '))
atual = date.today().year
idade = atual - nasc

if idade <= 9:
    print('Você tem {} anos e está na categoria MIRIM'.format(idade))
elif idade <= 14:
    print('Você tem {} anos e está na categoria INFANTIL'.format(idade))
elif idade <= 19:
    print('Você tem {} anos e está na categoria JUNIOR'.format(idade))
elif idade <= 25:
    print('Você tem {} anos e está na categoria SÉNIOR'.format(idade))
else:
    print('Você tem {} anos e está na categoria MASTER'.format(idade))