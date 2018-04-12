import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

Q = [[0.2, 0.1], [0.1, 0.15]]

lan, e = LA.eig(Q)
iii = [-0.15155, -1.3051]
print(lan,'\n', e[:,0] * 2)
