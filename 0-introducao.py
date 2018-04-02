#!/bin/env python3
#-*- encoding:utf-8-*-

print("O que é a biblioteca pandas ?")
raw_input()
print("pandas é uma biblioteca open-source em Python para análse de dados. Python tem \
	sido uma exelente plataforma para manipulação e leitura de dados, mas nunca foi boa\
	para análise - sempre caíamos no uso da linguagem R ou MatLab ou carregando a base de dados\
	usando SQL ou até no Excel. Pandas torna Python uma exelente alternativa para análise exploração de dados.")

raw_input()
print("Importando bibliotecas pandas, numpy, matplotlib")

raw_input()
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
pd.set_option('max_columns', 50)

print("Series")
print("Series é um objeto em uma dimensão similar ao array, lista ou coluna em uma tabela. Ele permite\
	atribuir indices rotulados 	para cada item dentro da Series. Por padrão, cada item irá receber um rótulo\
	(indice) de 0 até N, onde N é o tratamento da Serie - 1")

# create a Series with an arbitrary list
s = pd.Series([7, 'Python', 3.14, -123123, 'Adoro'])

raw_input()
print("Outra alternatica é poder especificar o índice que será usado quando criar uma Series")
s = pd.Series([7, 'Python', 3.14, -123123, 'Adoro'], index=['A', 'Z', 'C', 'Y', 'E'])

raw_input()
print("O construtor de Series pode converter um dicionario também, usando as chaves dicionário como índice")
d = {'Recife': 1000, 'Brasilia': 1300, 'Maceio': 900, 'Salvador': 1100, 'Aracaju': 450, 'Natal': None}
cities = pd.Series(d)
cities

raw_input()
print("Você pode usar índice para selecionar items específicos de uma Series...")
cities['Brasilia']

raw_input()
print("Pode ser passado uma lista de ídices")
cities[['Brasilia', 'Salvador', 'Recife']]

#ou ate boolean indexing para celecao
cities[cities < 1000]

raw_input()
print("O último caso pode ser um pouco estranho, mas vamos torná-lo mais claro - cities < 1000 retorna uma Series de valores True\ False, onde \
	passamos para nossa Series cities e ele retorna apenas os items correnspondentes a True")

menor_que_1000 = cities < 1000
print(menor_que_1000)
print('\n')
print(cities[menor_que_1000])

raw_input()
print("Você pode mudas as dados Series em tempo de execução!")
#changing based on the index
print("Valor antigo: ", cities['Aracaju'])
cities['Aracaju'] = 1400
print("valor Novo: ", cities['Aracaju'])

#charging value using boolean logic 
print(cities[cities < 1000])
print('\n')
cities[cities < 1000] = 750
print(cities[cities < 1000]) 

raw_input()
print("Se você não tem certeza se um item está dentro de uma Series, você pode checar usando Python básico.")
print("Recife" in cities)
print("Sao Paulo" in cities)

raw_input()
print("Operações matemáticas podem ser usandp escalares e funções")
#divide city values by 3
cities / 3
#square city values
np.square(cities)

raw_input()
print("Você pode adicionar 2 Series, o que vai retornar uma união de duas séries com adição dos valores em que índices são iguais.\
	valores nas séries que não tem índices em comum irão retornar um valor NULL/NaN( not a number)")
print(cities[['Recife', 'Brasilia', 'Aracaju']])
print('\n')
print(cities[['Maceio', 'Recife']])
print('\n')
print(cities[['Recife', 'Brasilia', 'Aracaju']] + cities[['Maceio', 'Recife']])
print("Note que Aracaju, Brasilia e Maceio como não foram encontradas em ambas as Series, eles retornarma valores NULL/NaN")
print(" O check de NULL pode ser realizado com as funções isnull e notnull")

raw_input()
#return a boolean series indicating which values aren't NULL
cities.notnull()

print(cities.isnull())
print("\n")
print(cities[cities.isnull()])

raw_input()
print("\nData Frame\n")
raw_input()
print("Um DataFrame é uma estrutura de dados tabular composta por colunas e linhas, lembrando muito as planilhas, tabela de banco de dados,\
	ou quem é familiar com a linguagem R: o data.frame. Você pode imaginar o DataFrame como um grupo de Series que compartinham o índice (os nomes das colunas)\n")

raw_input()
print("\nLendo dados\n")
raw_input()
print("Para criarmos um DataFrame a partir das estruturas de dados naticas em Python, nós podemos passar um dicionário de listas para o construtor do DataFrame")
print("Usando o parâmetro columns nos ajuda a definir no construtor como queremos que as colunas sejam ordenados. Por padrão, o construtor do DataFrame irá ordenar as colunas em ordem alfabética\
	(embora que este não seja o caso quando estamos lendo de um arquivo)\n")

data = {'Ano': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012], 'Time': ['Flamengo', 'Flamengo', 'Flamengo', 'Vasco', 'Vasco', 'Cruzeiro', 'Cruzeiro', 'Cruzeiro'],
'Vitorias': [11,8,10, 15, 11, 6, 10, 4], 'Derrotas': [5, 8, 6,1,5,10,6,12]}
football = pd.DataFrame(data, columns=['Ano', 'Time', 'Vitorias', 'Derrotas'])
print(football)

raw_input()

print("CSV")

from_csv = pd.read_csv("nome_do_arquivo.csv", sep= ';')
from_csv.head()


print("Excel")

football = pd.read_excel('football.xlsx', 'Sheet1')
print(football)


print("DataBase")
from pandas.io import SQL
import sqlite3

conn = sqlite3.connect("simple.db")
query = "SELECT * FROM albums WHERE artist='Red';"

results = sql.read_frame(query, con=conn)
print(results.head())


print("URL")

from urllib2 import urlopen
from StringIO import StringIO

url = urlopen('https://raw.github.com/...')

from_url = pd.read_table(StringIO(url), sep='\t')
from_url.head(3)