
frase = str('Curso em Video Python')
trocando = frase.replace('Python','Pinto') # O método replace faz a troca de um por outro, o que vem primeiro é o que vai ser substituido pelo o que vem depois da virgula
letrasMaisuculas = frase.upper() # Aumenta todas as letras da frase em maiusculas
letrasMinusculas = frase.lower() # Deixas todas as letras da frase em minusculas
inicialM = frase.capitalize() # Deixando apenas a primeira letra maiuscula
contaFrase = frase.title() # Deixa todas as inciais de cada palavra em maisuculo

print('*', frase, ': Mostrando a frase')
print('*', trocando, ' : Trocando a palavra por outra')
print('*', letrasMaisuculas, ': Deixa maiusculo')
print('*', letrasMinusculas, ': Deixa minusculo')
print('*', inicialM, ': Deixando a incial maiuscula')
print('*', contaFrase, ': Deixando a incial de cada palavra maiuscula')
print('---------------------------------------------------------------------------------------')

# Removendo os espaços inciais e finais de uma frase, exceto espaços do meio de uma frase.#

text = str('   Aprendendo Python  ')
print(':Antes:\n', text, '\n:Depois sem espaço:')
tiraE = text.strip()
print(tiraE)

tirandoER = text.rstrip() # Tirando apenas o espaço com caracteres vazios a direita. O 'r' significa right
tirandoEL = text.lstrip() # Tirando apenas o espaço com caracteres vazios a direita. O 'l' significa right

print('*', tirandoER, ': Tirando espaço só da direita')
print('*', tirandoEL, ': Tirando espaço só da esquerda')
