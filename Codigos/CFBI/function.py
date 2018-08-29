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

def getRecomendacoesItens(baseUsuario,similaridadeItens,usuario):
    print("Recomendacoes para o filme: " + setMovies()[usuario])
    notasUsuario = baseUsuario[usuario] #recebe a base de dados dos usuários
    notas={}
    totalSimilaridade={}

    mae  = 0
    i = 0
    for (item,nota) in notasUsuario.items():#percorre a base de daods e pega cada item e nota
        for (similaridade,item2) in similaridadeItens[item]: #percorre em um for e verifica a similaridade do item ja com a funcao de similaridade rodada e guarda a similaridade e o item
            if item2 in notasUsuario:
                continue #faz com que o item não faça o calculo dele mesmo

            notas.setdefault(item2,0)#inicia um item com um valor
            notas[item2] += similaridade * nota #na posição do item ele faz o calculo da similaridade com a nota da base de dados
            totalSimilaridade.setdefault(item2,0.0000000001) #soma as notas
            totalSimilaridade[item2] += similaridade

            mae += abs( notas[item2] - nota ) 
            i = i+1
            
        rankings=[(setMovies()[item], score/totalSimilaridade[item]) for item,score in notas.items()]
        # rankings=[(setMovies()[item], score/totalSimilaridade[item] if totalSimilaridade[item] != 0.0 else 0.0) for item,score in notas.items()]

    print(mae/i)
    # print(i,len(rankings))

    rankings.sort(key=itemgetter(1),reverse=True)

    return rankings[0:10]