#Desenvolva um programa qua leia as duas notas da um aluno, calcule e mostra a sua média.

nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
CalcMedia = (nota1 + nota2) / 2

print('A média do aluno é {:.2f}.'.format(CalcMedia))

if CalcMedia >= 7:
    print('O Aluno foi Aprovado com a média {}.'.format(CalcMedia))
else:
    print('O Aluno foi Reprovado Porque não Atingiu a Média Determinada.')