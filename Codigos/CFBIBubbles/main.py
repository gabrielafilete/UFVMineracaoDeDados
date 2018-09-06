# from utils import *
from databubbles_teste import *
from func import *
# from lib.databubbles import *
import numpy as np


base = carregaMovieLens()

# print(len(base))
sim = calculaItensSimilares(base)
print(sim)
# print(printToJson(base))