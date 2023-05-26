#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condiÇão da pagamento:
# - À vista dinheiro/cheque: 10%
# - À vista no cartão: 5%
# - Em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de Juros

print('{:=^40}'.format(' Lojas TaQi '))
preco = float(input('Preço das Compras: R$ '))
print('''FORMAS DE PAGAMENTO
[ 1 ] À vista no Dinheiro / Cheque.
[ 2 ] À vista no Cartão.
[ 3 ] Em Até 2x no Cartão.
[ 4 ] 3x ou mais no Cartão.''')
opcao = int(input('Qual será a Modalidade de Venda? Selecione o Número Correpondente: '))

if opcao == 1:
    avista = preco - (preco * 10 /100)
    print('*', 'A sua Compra de R${:.2f} vai custa R${} com o Desconto de 10%.'.format(preco, avista))
elif opcao == 2:
    avcartao = preco - (preco * 5 /100)
    print('*', 'A sua Compra de R${:.2f} vai custa R${} com o Desconto de 5%.'.format(preco, avcartao))
elif opcao == 3:
    avcartao2x = preco
    parcela = avcartao2x / 2
    print('A sua Compra será pacelada em 2x de R${:.2f}'.format(parcela))
    print('*', 'A sua Compra de R${:.2f} no final sem Juros'.format(preco))
elif opcao == 4:
    avCartao = preco + (preco * 20 / 100)
    parcelas = int(input('Em Quantas Parcelas Deseja Fazer? '))
    totParcelas = avCartao / parcelas
    print('Sua Compra será Parcelada em {}x de R${:.2f} com Juros.'.format(parcelas, totParcelas))
    print(f'Sua compra de R${preco} vai acabar custado R${avCartao}')
else:
    preco = 0
    print('\033[31mModalidade de Venda Incorreta. Tente Novamente!')