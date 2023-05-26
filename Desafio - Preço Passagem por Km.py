#Dasenvolva um programa que pergunta a distancia de uma viagem em Km. Calcule o preço da passagem, cobrando RSO,5O por km para viagens de até 200km
# e R$0,45 para viagens mais longas.

lenghtViagem = int(input('Digite a Distância que Será Percorrida nesta Viagem: '))

if lenghtViagem <= 200:
    calcularPreco = lenghtViagem * 0.50
    print(f'O Valor da Passagem para está Viagem será de {calcularPreco} R$ para uma distância de {lenghtViagem} kmh')
if lenghtViagem > 200:
    calcularPreco = lenghtViagem * 0.45
    print(f'O Valor da Passagem para está Viagem será de {calcularPreco} R$ para uma distância de {lenghtViagem} kmh')
