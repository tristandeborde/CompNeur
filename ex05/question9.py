import time
import numpy as np
from numpy import concatenate as cc
import matplotlib.pyplot as plt
from numpy import linalg as LA

W = np.eye(5)
W[W > 0] -= 0.5
W += 0.1
u = np.zeros((5, 1))
u = [0.6, 0.5, 0.6, 0.2, 0.1]
M = np.zeros((5, 5))
M[0] = [-0.75, 0, 0.75, 0.75, 0]
M[1] = [0, -0.75, 0, 0.75, 0.75]
M[2] = [0.75, 0, -0.75, 0, 0.75]
M[3] = [0.75, 0.75,0, -0.75, 0]
M[4] = [0, 0.75, 0.75, 0, -0.75]
#print("W = {},\nu = {},\nM = {}\n".format(W, u, M))

h = np.dot(W, u)
lan, e = LA.eig(M)

V_ss= ((np.dot(h, e) / (1 - lan))* e)

print(np.sum(V_ss, axis=1))
