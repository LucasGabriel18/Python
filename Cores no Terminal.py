
print('\033[1;31;43m Olá Mundo\033[m')
print('\033[4;30;45m Olá Mundo\033[m')
print('\033[30m Olá Mundo\033[m')
print('\033[7;33;44m Olá Mundo\033[m')

a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \33[35m{}\033[m !!!'.format(a, b)) # Neste exemplo eu deixei apenas os numeros declarados com cor.

nome = 'Lucas'
print('Olá! Muito Prazer em te Conhecer, {}{}{} !!!'.format('\033[4;31m', nome, '\033[m'))# Neste exemplo eu deixei apenas o nome declarados com cor.

cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'vermelho': '\033[31m',
         'pretoebranco': '\033[7;30m'}

print('Olá! Muito Prazer em te Conhecer, {}{}{} !!!'.format(cores['azul'], nome, cores['limpa']))# Já neste exelo decalrei variáveis já definindo um padrão de cores.
# Na hora de chamar apenas usa o nome da varável e a cor desejada.
