#Crie um programa que leia quanto dinheiro uma passoa tem na carteira e mostre quantos Dólares ela pode comprar.
# Considere US$ 1,OO = RS3,27

n = float(input("Quanto dinheiro você tem? \nR$"))
dolar = 3.27
conversao = n / dolar
print("Com R${} você pode comprar US$ {:.2f}.".format(n, conversao))
