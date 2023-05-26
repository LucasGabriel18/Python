# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Kmh mostre uma mansagem dizendo que ele foi multado.
# E a multa vai custar RS7,OO por cada km acima do limita.

speed = float(input('Digite a Velocidade do Carro: '))
if speed > 80:
    multa = (speed - 80) * 7
    print('Você foi multado por excesso de velocidade. Você estava {} KmH.\nVocê deve Paga uma multa de {} R$!'.format(speed,multa))
else:
    print('Pode Seguir o Seu caminhos Traquilamente! A Velocidade é Aceitável.')