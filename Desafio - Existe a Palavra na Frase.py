# Crie um programa que leia o nome de uma cidade a diga se ela começa ou não com o "SANTO"

cidade = str(input('Digite o Nome da Cidade: ')).strip().lower().capitalize().upper()
valida = 'SANTO' in cidade[:5]

print(valida)