# Escreva um programa qua leia um valor em metros a o exiba convertido em centimatros a milimatros.
# 1 metro é igual a 100cm
# 1 metro é igual a 1000mil

metro = float(input('Digite o valor em metros desejado: '))
centimetro = metro * 100
milimetro = metro * 1000

print('O valor convertido de metros para centimentro fica {}.\n Já o valor convertido de metros para milimetros fica {}.'.format(centimetro,milimetro))