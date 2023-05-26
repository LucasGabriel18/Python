# O mesmo professor do dasafio anterior quer soretar a ordem de aprasantação da trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

aluno1 = str(
    input('Digite o Nome do 1º Aluno que Vai no Pote: '))  # Pega a informação do nome do aluno e guarda na variável
aluno2 = str(
    input('Digite o Nome do 2º Aluno que Vai no Pote: '))  # Pega a informação do nome do aluno e guarda na variável
aluno3 = str(
    input('Digite o Nome do 3º Aluno que Vai no Pote: '))  # Pega a informação do nome do aluno e guarda na variável
aluno4 = str(input(
    'Digite o Nome do 4º e Último Aluno que Vai no Pote: '))  # Pega a informação do nome do aluno e guarda na variável

listaAlunos = [aluno1, aluno2, aluno3,
               aluno4]  # Cria um array chamado lista para armazenar as variáves que foram denominadas com o nome dos alunos
random.shuffle(listaAlunos)  # A função random.shuffle é responsável por embaralhar
print('A lista de apresentação, ficará da seguinte maneira\n: ')
print(listaAlunos)  # Mostra a lista embaralhada.
