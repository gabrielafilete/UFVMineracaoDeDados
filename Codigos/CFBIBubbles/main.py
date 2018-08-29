# -*- coding: utf-8 -*-
from db_itens import *
from function import *

# U.ITEM -- movie id | movie title | release date | video release date |
#   IMDb URL | unknown | Action | Adventure | Animation |
#   Children's | Comedy | Crime | Documentary | Drama | Fantasy |
#   Film-Noir | Horror | Musical | Mystery | Romance | Sci-Fi |
#   Thriller | War | Western |

# Os últimos 19 campos são os gêneros, um 1 indica que o filme é desse gênero, 
# um 0 indica que não é; Os filmes podem estar em vários gêneros ao mesmo tempo. 
# Os IDs dos filmes são os usados no conjunto de dados u.data.  

# U.data -- user id | item id | rating | timestamp

# O conjunto completo de dados, 100000 avaliações por 943 usuários em 1682 itens.
# Cada usuário classificou pelo menos 20 filmes. Usuários e itens são
# numeradas consecutivamente de 1. Os dados são aleatoriamente encomendado.
# Os carimbos de hora são segundos de unix desde 1/1/1970 UTC

# 'iFilme': {'idUser', rate}
arrayRMovies = rattingMovies()

# setSim = calculaItensSimilares(arrayRMovies)

# print(getRecomendacoesItens(arrayRMovies,setSim,"144"))

dataBubbles(arrayRMovies)
