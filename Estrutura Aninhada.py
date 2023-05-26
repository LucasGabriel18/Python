nome = str(input('Qual é o seu nome? '))

if nome == 'Lucas':
    print('Que Nome Bonito Você Tem!')
elif nome == 'Mateus' or nome == 'Rafael' or nome == 'Pedro':
    print('O Seu Nome é Bem Popular no Brasil!')
elif nome in 'João Carlos Alberto Junior Neymar':
    print('Que belo nome você tem!')
else:
    print('Seu nome é Bem Normal.')

print(f'Tenha um Bom dia, {nome}!')