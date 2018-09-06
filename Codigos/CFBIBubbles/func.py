# -*- coding: utf-8 -*- 
#from db_users import *
from math import sqrt
from operator import itemgetter

def euclidiana(base,user1,user2): #faz o calculo de aproximidade dos usuários
    dados = {}

    for item in base[user1]:
        if item in base[user2]:
            dados[item] = 1

    if len(dados) == 0:
        return 0

    soma = sum ([pow(base[user1][item] - base[user2][item],2)  for item in base[user1] if item in base[user2]])
    return 1/(1+sqrt(soma))

def getSimilares(base,user): #retorna a similaridade de um usuários com todos os outros usuários
    similaridade = [(euclidiana(base,user, outro), outro) for outro in base if outro != user]
    similaridade.sort()
    similaridade.reverse()
    return similaridade[0:45] #retorna os 30 itens mais similares

def calculaItensSimilares(base):
    result = { }
    for item in base:
        #item 321
        notas = getSimilares(base,item)
        result[item] = notas
    return result

def setMovies():
    filmes = { }
    for linha in open('u.item'):#o enconding foi usado para solucionar o erro na abertura do arquivo
        (id,titulo) = linha.split('|') [0:2] #começa a pegar da posição 0 e vai até a segunda qebra
        filmes[id] = titulo
    return filmes

def rattingMovies():
    base = { }
    for linha in open('u.data'): #carrega os dados do arquivo u.data que contem o numero do user,o id do filme , a nota do filme e o tempo
        (usuario,idfilme,nota,tempo) = linha.split('\t')#\t é tab
        base.setdefault(idfilme,{ })
        base[idfilme][usuario] = float(nota)
        
    return base

def getRecomendacoesItens(base,similaridadeItens,item):