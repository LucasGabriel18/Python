
frase = str('Curso em Vídeo Python')

letra = frase[3]
balum = frase[3:13]
frases = frase[1:15:2]
prkeka = frase[:5]
blabla = frase[15:]
lapada = frase[1::2]
pulaLa = frase[::2]
tamanho = len(frase)
contador = frase.count('o')
finde = frase.find('deo')
ine = 'Curso' in frase

print(letra) # Vai mostrar o quarto caracter da frase
print(balum) # Vai mostrar os caracteres entre a quarta e décima terceira casa.
print(ine) # Mostra se a Palavra "Curso" existe, se sim, retorna True, se não, mostra False
print(finde) # Mostra a posição aonde está o trecho informado.
print(tamanho) # Mostra o tamanho da frase
print(contador) # Neste caso ele mostrou quantas vezes aparece a letra "o"
print(frases)  # Mostra do do caracter 1 até o 15 pulando de duas em duas casas
print(prkeka) # Do inicio até o quinto caracater
print(blabla) # Mostra da décima quinta casa em diante
print(lapada) # Aqui ele mostra do primeira caracter até o final pulando de dois em dois
print(pulaLa) # Mostra toda a string só que pulando de dois em dois