#Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o noma deles e escrevendo o nome do escolhido.

import random
aluno1 = str(input('Digite o Nome do 1º Aluno que Vai no Pote: '))  #Pega a informação do nome do aluno e guarda na variável
aluno2 = str(input('Digite o Nome do 2º Aluno que Vai no Pote: '))  #Pega a informação do nome do aluno e guarda na variável
aluno3 = str(input('Digite o Nome do 3º Aluno que Vai no Pote: '))  #Pega a informação do nome do aluno e guarda na variável
aluno4 = str(input('Digite o Nome do 4º e Último Aluno que Vai no Pote: ')) #Pega a informação do nome do aluno e guarda na variável


lista = [aluno1, aluno2, aluno3, aluno4]    #Cria um array chamado lista para amazenar as variáves que foram denominadas com o nome dos alunos
sorteado = random.choice(lista) # Cria a variável sorteado para receber o retorno da função random.choice(lista) que consegue armazenar os arrays

print('O Aluno Sorteado Foi: {}'.format(sorteado)) # Mostra o Sorteado