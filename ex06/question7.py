import numpy as np
import pickle
import matplotlib.pyplot as plt
from numpy import linalg as LA

with open('c10p1.pickle', 'rb') as f:
    data = pickle.load(f)
data = np.array(data['c10p1'])
#normalize
data -= np.mean(data, axis=0)

cov_mat = np.dot(np.transpose(data), data) / 100
lan, e = LA.eig(cov_mat)
print (lan, '\n', e, '\n', cov_mat, '\n\n')

N = 1
alpha = 1
delta_t = 0.01
w = [0.1222, 0.94]
w_ev = []

for i in np.arange(0, 100000, 1):
    v = data[i%100] * w
    w = w + delta_t * N * (v*data[i%100] - alpha*(v**2)*w)
    '''if (i%1000 == 0):
        w_ev.append(w) 
w_ev = np.asarray(w_ev)
'''
print(v, w)
