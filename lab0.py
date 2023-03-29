# Strings

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

# o método len(string) retorna o tamanho da string
print(len(hello))

# Retorna um boolean (true or false), verifica se um caracter ou um conjunto de caracteres está ou não está presetente na string
texto = "Melhores alunos estão no IPS!"
print('alunos' in texto)

#Obtenção de uma substring de uma string

print(texto[1:6]) # mostra os caracteres do índice 1 ao índice 5
print(texto[:6]) #mostra os caracteres do índice 0 ao índice 5
print(texto[9:]) #mostra os caracteres do índice 9 até ao final

#o método replace(string1,string2) substitui uma string ou parte de uma string por outra
print(texto.replace('IPS','Politécnico de Setúbal'))

#Operações úteis com sstrings incluem:

#o método len (string), que retorna o tamanho da string

print(len(hello))

# as palavras-chave in e not in, para verificar se um carater ou conjunto de carateres está
# ou não está presente numa string:

print('alunos' in texto)

# obter uma substring da string:

print(texto[1:6]) # mostra os carateres do índice 1 ao índice 5

print(texto[:6]) # mostra os carateres do índice 0 ao índice 5

print(texto[9:]) # mostra os carateres do índice 9 ao final

# usar o método replace(string1,string2) para substituir uma string ou parte de uma string por outra:

print(texto.replace('IPS','Politécnico de Setúbal'))

# usar o método split(delimitador) para dividir a string em substrings se encontrar
# instâncias do delimitador:

print(texto.split(' '))

# usar o operador '+' para concatenar strings:

hello = 'alo'
world = "mundo"
frase = hello + ' ' + world
print(frase)

# usar o método format(valor) para concatenar strings com números. A string tem de ter
#sido definida com a indicação de onde vai o número ou números (placeholder) usando chavetas:

idade = 35
dizer = 'Meu nome é João e tenho {} anos'
print(dizer.format(idade))

# Se houver mais de um placeholder, pode-se colocar um número dentro das chavetas a
# indicar o posicionamento correto dos argumentos:

dizer = 'Meu nome é João e tenho {1} anos e {0} filhos'
print(dizer.format(2,idade))

# usar o método zfill(valor) para preencher a string com zeros até a string completar o
# tamanho desejado:

print(frase)
zfrase = frase.zfill(15)
print(zfrase)

# Listas

# 1. Alterar elementos da lista

hello = 'alo' # aspas simples ou duplas, dá no mesmo
minha_lista = [hello, 'mundo', 3.14, 45]
print(minha_lista)
['alo', 'mundo', 3.14, 45] # mostra com aspas simples
print(minha_lista[2])
minha_lista[2] = 33
print(minha_lista)
print(minha_lista[1:3])

# 2. Adicionar elementos na lista

nova_lista = minha_lista + ['adicione', 'elemento']
print(nova_lista)
['alo', 'mundo', 33, 45, 'adicione', 'elemento']

# 3. Remover elementos da lista
del nova_lista[0]
print(nova_lista)
['mundo', 33, 45, 'adicione', 'elemento']

#O que é uma matriz?
#No Python, tal como em outras linguagens, uma matriz é um vetor ou array multi-dimensional.
#Podemos tratar uma lista de listas como uma matriz. Por exemplo, uma matriz de 2 linhas e 3 colunas:

A = [[1, 4, 5], [-5, 8, 9]]
print(A);

# Os exemplos a seguir ilustram algumas formas de trabalhar com listas encadeadas:

M = [[1, 4, 5, 12],
     [-5, 8, 9, 0],
     [-6, 7, 11, 19]]

print("M =", M)
print("M[1] =", M[1]) # segunda linha
print("M[1][2] =", M[1][2]) # terceiro elemento da segunda linha
print("M[0][-1] =", M[0][-1]) # último elemento da primeira linha
print("M[0][3] =", M[0][3])



