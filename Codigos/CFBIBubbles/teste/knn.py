from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

arquivo = 'iris.txt'

with open(arquivo) as f:
    amostras = f.readlines()
# print amostras

# separacao por classes:
setosa = amostras[:50]
versicolor = amostras[50:100]
virginica = amostras[100:]

# regorniza dados para ter proporcao igual de amostras
amostras_organizadas = []
for i in range(0, 50):
    amostras_organizadas.append(setosa[i])
    amostras_organizadas.append(versicolor[i])
    amostras_organizadas.append(virginica[i])
# print amostras_organizadas

# separacao caracteristicas e classes
caracteristicas = []
classes = []
for amostra in amostras_organizadas:
    aux = amostra.split(",")
    comprimento_sepala = float(aux[0])
    largura_sepala = float(aux[1])
    comprimento_petala = float(aux[2])
    largura_petala = float(aux[3])
    classe = aux[4].strip()
    caracteristicas.append(
        [comprimento_sepala, largura_sepala, comprimento_petala, largura_petala])
    classes.append(classe)
# print caracteristicas
# print classes

# separacao treinamento e teste
proporcao_treinamento = 0.7
caracteristicas_treinamento = caracteristicas[:int(
    proporcao_treinamento * len(amostras))]
caracteristicas_teste = caracteristicas[int(
    proporcao_treinamento * len(amostras)):]
classes_treinamento = classes[:int(proporcao_treinamento * len(amostras))]
classes_teste = classes[int(proporcao_treinamento * len(amostras)):]

# treinamento
k = 20
neigh = KNeighborsClassifier(n_neighbors=k,leaf_size=3, metric='euclidean')
neigh.fit(caracteristicas_treinamento, classes_treinamento)
classes_previstas = neigh.predict(caracteristicas_teste)

plt.plot(classes_teste, classes_previstas, 'ro')

# print(classes_previstas)

# verifica acertos
porcentagem_acerto = 0
for classe_correta, classe_prevista in zip(classes_teste, classes_previstas):
    if( classe_correta != classe_prevista):
        print(classe_correta + ' - ' + classe_prevista)
    if classe_correta == classe_prevista:
        porcentagem_acerto += 1
porcentagem_acerto /= float(len(classes_teste))
print(porcentagem_acerto * 100)


#plt.show()