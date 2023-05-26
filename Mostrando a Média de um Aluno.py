# Crie um programa que leia duas notas de um aluno a calcule sua média, mostrando uma mansagam no Final, de acordo com a média atingida:
# — Média abaixo da 5.0:
#REPROVADO
# — Média entre 5.0 6.9:
# RECUPERRAÇÃO
# — Média 7.0 ou superior:
#APROVADO


nota1 = float(input('Digite a 1º nota do Aluno: '))
nota2 = float(input('Digite a 2º nota do Aluno: '))
media = (nota1 + nota2) / 2

if media < 5:
    print('O Aluno  está \033[31mREPROVADO\033[m com a Média {:.2f}'.format(media))
elif 7 > media >= 5:
    print('O Aluno ficou de \033[33mRECUPERAÇÃO\033[m com a Média {:.2f}'.format(media))
elif media > 7:
    print('O Aluno foi \033[32mAPROVADO\033[m com a Média {:.2f}'.format(media))