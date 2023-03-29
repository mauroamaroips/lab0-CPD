hello = "alo"
hello = 'alo'

print('alo')
print(hello)

b = """Esta string é
multilinha usando
três aspas como delimitador"""

print(b)

c = "Esta string é\nmultilinha usando \no caracter de mudança de linha"
print(c)

print(hello[1])

for x in hello:
    print(x)

# O método len(string) retorna o tamanho da string
print(len(hello))

# Retorna um boolean (true or false), verifica se um caracter ou um conjunto de caracteres está ou não está presetente na string
texto = "Melhores alunos estão no IPS!"
print('alunos' in texto)

#Obtenção de uma substring de uma string

print(texto[1:6]) # mostra os caracteres do índice 1 ao índice 5
print(texto[:6]) #mostra os caracteres do índice 0 ao índice 5
print(texto[9:]) #mostra os caracteres do índice 9 até ao final

#método replace(string1,string2) substitui uma string ou parte de uma string por outra  
print(texto.replace('IPS','Politécnico de Setúbal'))
