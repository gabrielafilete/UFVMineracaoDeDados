import numpy as np
from sklearn.neighbors import KNeighborsClassifier

import os
import csv
import time
from datetime import date, timedelta

import math


# def distanceEuclidian(obj1, obj2, length):
#    distance = 0
#    if(len(obj1) < length || len(obj2) > length):
#        length
#
#    for x in range(length):
#        distance += pow((obj1[x] - obj2[x]), 2)
#    return math.sqrt(distance)


def loadDataset(path, split, trainingSet=[], testSet=[]):
    with open("/home/romulo/Área de Trabalho/u.csv", "rb") as csvfile:
        dataset = list(csv.reader(csvfile))
        for row in range(len(dataset) - 1):
            print(", ".join(row))


def carregaMovieLens():  # retorna o id do filme e o respectivo nome do filme
    filmes = {}
    for linha in open("u.item"):  # o enconding foi usado para solucionar o erro na abertura do arquivo
        (id, titulo) = linha.split("|")[0:2]  # começa a pegar da posição 0 e vai até a segunda qebra
        filmes[id] = titulo
    base = {}
    
    for linha in open("u.data"):  # carrega os dados do arquivo u.data que contem o numero do user,o id do filme , a nota do filme e o tempo
        (usuario, idfilme, nota, tempo) = linha.split("\t")  # \t é tab
        base.setdefault(usuario, {})
        base[usuario][filmes[idfilme]] = float(nota)
    return base
