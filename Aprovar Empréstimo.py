# Escreva um programa para aprovar o empréstimo bancário para uma compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador
# em quantos anos ele vai pagar.
# Calcule o valor da prastaÇão mensal, sabendo qua ele não pode exceder 30% do salário ou então o empréstimo sará negado.

Vlrcasa = float(input('Qual é o Valor da Casa? R$: '))
SalarioComprador = float(input('Qual é Salário do Comprador? R$: '))
AnosFinan = int(input('Em quantos Anos de Financiamento? '))

prestacao = Vlrcasa / (AnosFinan * 12)
minimo = SalarioComprador * 30 / 100

print('Para Pagar uma Casa de R${:.2f} em {} anos. A prestação será de R${:.2f}!'.format(Vlrcasa, AnosFinan, prestacao))
if prestacao <= minimo:
    print('Empréstimo \033[32mAPROVADO!\033[m')
else:
    print('Emprestimo \033[31mNEGADO!\033[m')
