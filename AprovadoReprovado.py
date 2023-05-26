num1 = float(input('Digite a primeira nota do aluno: '))
num2 = float(input('Digite a segunda nota do aluno: '))
media = (num1 + num2) / 2

if media >= 7:
    print('Aprovado')
    print('A média do aluno ficou', media)
else:
    print('Reprovado')
    print('A média do aluno ficou', media)
