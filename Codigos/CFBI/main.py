# -*- coding: utf-8 -*-
from db_itens import *
from function import *
import sys

import matplotlib.pyplot as plt

def printDic(base, listDic):
    for x in listDic:
        print("Id: ", x, " - ", base[x])

# U.ITEM -- movie id | movie title | release date | video release date |
#   IMDb URL | unknown | Action | Adventure | Animation |
#   Children's | Comedy | Crime | Documentary | Drama | Fantasy |
#   Film-Noir | Horror | Musical | Mystery | Romance | Sci-Fi |
#   Thriller | War | Western |

# Os últimos 19 campos são os gêneros, um 1 indica que o filme é desse gênero,
# um 0 indica que não é; Os filmes podem estar em vários gêneros ao mesmo tempo.
# Os IDs dos filmes são os usados no conjunto de dados u.data.

# U.data -- user id | item id | rating | timestamp

# O conjunto completo de dados, 100.000 avaliações por 943 usuários em 1682 itens.
# Cada usuário classificou pelo menos 20 filmes. Usuários e itens são
# numeradas consecutivamente de 1. Os dados são aleatoriamente encomendado.
# Os carimbos de hora são segundos de unix desde 1/1/1970 UTC

# 'iFilme': {'idUser', rate}
#PREENCHE ARRAY COM O BANCO========================
# arrayRMovies = setMovies()

# listDic = list(arrayRMovies.keys())

# for x in listDic:
#     print("user: ", x, " - ", arrayRMovies[x])

# print( len(arrayRMovies) )


#BUSCA TODAS A SIMILARIDADES DOS ITEMS=============
# setSim = calculaItensSimilares(arrayRMovies)

# for x in listDic:
#     print("User: ", x, " - ", setSim[x])

# print(getRecomendacoesItens(arrayRMovies,setSim,"50"))
# print(getRecomendacoesItens(arrayRMovies,setSim,"Star Wars (1977)"))

# print("aa", euclidiana(arrayRMovies, '196', '64') )

'''

196 ------------ {'242': 3.0, '393': 4.0, '381': 4.0, '251': 3.0, '655': 5.0, '67': 5.0}

196  -  [(1.0, '64'), (1.0, '303'), (1.0, '244'), (1.0, '23'), (1.0, '193'), (1.0, '16'), (1.0, '154'), 
         (1.0, '10'), (0.5, '87'), (0.5, '63'), (0.5, '59'), (0.5, '328'), (0.5, '327'), (0.5, '307'), 
         (0.5, '296'), (0.5, '295'), (0.5, '290'), (0.5, '271'), (0.5, '264'), (0.5, '247'), (0.5, '201'), 
         (0.5, '178'), (0.5, '145'), (0.3333333333333333, '98'), (0.3333333333333333, '34'), 
         (0.3333333333333333, '306'), (0.3333333333333333, '286'), (0.3333333333333333, '226'), 
         (0.3333333333333333, '209'), (0.3333333333333333, '2')]

'''


# 'iFilme': {'idUser', rate}
arrayRMovies = rattingMovies()

#databubbles

setSim = calculaItensSimilares(arrayRMovies)

print(setSim)


# print(getRecomendacoesItens(arrayRMovies,setSim,"540"))