# -*- coding: utf-8 -*-
from db_users import *
from function import *


# print(euclidiana(avaliacoesUsuario,'2','7'))
# print(euclidiana(avaliacoesFilme,'Star Wars','Star Trek'))
# print(getSimilares(avaliacoesUsuario,'2'))
# print(getSimilares(avaliacoesFilme,'Star Wars'))
# print(getRecomendacoes(avaliacoesFilme,'Star Wars'))
# print(getRecomendacoes(avaliacoesUsuario,'7'))
base = carregaMovieLens()
#print(getSimilares(base,'1'))#usuários mais parecidos com o 212
print(getRecomendacoes(base,'1'))
