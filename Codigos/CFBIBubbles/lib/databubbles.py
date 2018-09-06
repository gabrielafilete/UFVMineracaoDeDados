import numpy as np
import matplotlib.pyplot as plt

def init():
    print('INICIO')


def distance(objeto1, objeto2):
    #se objetos forem listas ou tuplas
    objeto1 = np.array(objeto1) 
    objeto2 = np.array(objeto2)
    return np.linalg.norm(objeto1 - objeto2)

def get_neighbors(training_set, labels, test_instance, k, distance=distance):
    distances = []
    for index in range(len(training_set)):
        dist = distance(test_instance, training_set[index])
        distances.append((training_set[index], dist, labels[index]))
    distances.sort(key=lambda x: x[1])
    neighbors = distances[:k]
    return neighbors