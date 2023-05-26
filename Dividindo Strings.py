# Separando
inter = str('O Inter Não Colabora') # Por padrão a numeração de string é a seguinte. 012345678910111213141516171819202122232425262728
print(inter)
splitando = inter.split() # Ele basicamente vai dividir novamente só que diferente, toda nova palavra ele reinciai a contagem.
# 0 0123456 012345678
print(splitando)

#Juntando

junta = '-'.join(inter)
print(junta)

# Se quiser mostrar apenas uma parte da frase podemos fazer assim.

print(splitando[1])

