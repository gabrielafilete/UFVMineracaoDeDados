# -*- coding: utf-8 -*-
# from db_users import *
from math import sqrt
from operator import itemgetter
import sys


def euclidiana(base, user1, user2):  # faz o calculo de aproximidade dos usuários
    dados = {}

    for item in base[user1]:
        if item in base[user2]:
            dados[item] = 1

    if len(dados) == 0:
        return 0

    soma = sum([pow(base[user1][item] - base[user2][item], 2)
                for item in base[user1] if item in base[user2]])
    return 1/(1+sqrt(soma))
    # return 1/(1+sqrt(soma))


def getSimilares(base, user):  # retorna a similaridade de um usuários com todos os outros filmes
    similaridade = [(euclidiana(base, user, outro), outro)
                    for outro in base if outro != user]

    similaridade.sort()
    similaridade.reverse()

    # print(user,"------------", similaridade)
    # sys.exit()

    return similaridade[0:30]  # retorna os 30 itens mais similares


def calculaItensSimilares(base):
    result = {}
    for user in base:
        # user 321
        result[user] = getSimilares(base, user)
    return result


def setMovies():
    filmes = {}
    # o enconding foi usado para solucionar o erro na abertura do arquivo
    for linha in open('u.item'):
        # começa a pegar da posição 0 e vai até a segunda qebra
        (id, titulo) = linha.split('|')[0:2]
        filmes[id] = titulo
    return filmes


def rattingMovies():
    base = {}
    # carrega os dados do arquivo u.data que contem o numero do user,o id do filme , a nota do filme e o tempo
    for linha in open('u.data'):
        (usuario, idfilme, nota, tempo) = linha.split('\t')  # \t é tab
        base.setdefault(idfilme, {})
        base[idfilme][usuario] = float(nota)

    return base


def carregaMovieLens():  # retorna o id do filme e o respectivo nome do filme
    filmes = {}
    for linha in open('u.item'):
        # começa a pegar da posição 0 e vai até a segunda quebra
        (id, titulo) = linha.split('|')[0:2]
        filmes[id] = titulo
    # print(filmes)
    base = {}
    for linha in open('u.data'):
        (usuario, idfilme, nota, tempo) = linha.split('\t')  # \t é tab
        base.setdefault(usuario, {})
        base[usuario][idfilme] = float(nota)
        # base[usuario][filmes[idfilme]] = float(nota)

    return base


def getRecomendacoesItens(base, similaridadeItens, item):

    print("Recomendacoes para o filme: " + setMovies()[item])
    notasUsuario = base[item]  # recebe a base de dados dos usuários
    notas = {}
    totalSimilaridade = {}

    mae = 0
    i = 0
    for (item, nota) in notasUsuario.items():  # percorre a base de daods e pega cada item e nota
        # percorre em um for e verifica a similaridade do item ja com a funcao de similaridade rodada e guarda a similaridade e o item
        if similaridadeItens[item]:
            for (similaridade, item2) in similaridadeItens[item]:
                if item2 in notasUsuario:
                    continue  # faz com que o item não faça o calculo dele mesmo

                notas.setdefault(item2, 0)  # inicia um item com um valor
                # na posição do item ele faz o calculo da similaridade com a nota da base de dados
                notas[item2] += similaridade * nota
                totalSimilaridade.setdefault(
                    item2, 0.0000000001)  # soma as notas
                totalSimilaridade[item2] += similaridade

                mae += abs(notas[item2] - nota)
                i = i+1

                rankings = [(setMovies()[item], score/totalSimilaridade[item]) for item, score in notas.items()]
        # rankings=[(setMovies()[item], score/totalSimilaridade[item] if totalSimilaridade[item] != 0.0 else 0.0) for item,score in notas.items()]

    print(mae/i)
    # print(i,len(rankings))

    rankings.sort(key=itemgetter(1), reverse=True)

    return rankings[0:10]


def printOrder(ListBase):
    for x in ListBase:
        print("Id: ", x)
