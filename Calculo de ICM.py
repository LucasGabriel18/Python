# Desenvolva uma lógica qua leia o peso e a altura de uma pessoa, calcule seu IMC e mostra seu status, da acordo com a tabala abaixo:
# - Abaixo da 18 5: Abaixo do Peso
# - Entre 18.5 a 25: Peso ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obasidade mórbida

print('Calculador de ICM')
peso = float(input('Digite o Seu Peso em kg: '))
altura = float(input('Digite a Sua Altura: '))
icm = peso / (altura * altura)

indicador = {'Vermelho': '\033[31m',
            'Verde': '\033[32m',
             'Amarelo': '\033[33m',
             'Azul': '\033[34m',
             'Roxo': '\033[35m',
             'Limpa': '\033[m'}

if icm < 18.5:
    print('\nO seu Indíce é de {}{:.1f}{}'.format(indicador['Verde'], icm, indicador['Limpa']))
    print('Você está \033[32mAbaixo do Peso\033[m')
elif icm <= 25:
    print('O seu Indíce é de {}{:.1f}{}'.format(indicador['Verde'], icm, indicador['Limpa']))
    print('Você está no \033[33mPeso Ideal\033[m')
elif icm <= 30:
    print('O seu Indíce é de {}{:.1f}{}'.format(indicador['Verde'], icm, indicador['Limpa']))
    print('Você está com \033[35mSobrepeso\033[m')
elif icm <= 40:
    print('O seu Indíce é de {}{:.1f}{}'.format(indicador['Verde'], icm, indicador['Limpa']))
    print('Você está com \033[31mObesidade\033[m')
else:
    print('Você está com Obesidade Mórbida!')