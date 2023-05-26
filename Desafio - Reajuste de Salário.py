#Escreva um programa que pergunte o salário de um Funcionário e calcule o valor do seu aumento.
# Para salários superiores a RS1.25O,OO calcule um aumento da 10%
# Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Qual é o seu salário: '))

if salario > 1250:
    Nsalario = salario + (salario * 10 / 100)
    print(f'O Reajuste de 10% do Salário ficará em {Nsalario} R$ por Mês.')
else:
     Nsalario = salario + (salario * 15 / 100)
     print(f'O Reajuste de 15% do Salário ficará em {Nsalario} R$ por Mês.')