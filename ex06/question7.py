import numpy as np
import pickle
import matplotlib.pyplot as plt
from numpy import linalg as LA

with open('c10p1.pickle', 'rb') as f:
    data = pickle.load(f)
data = np.array(data['c10p1'])
#normalize
mu = np.mean(data, axis=0)
data -= mu


corr_mat = np.dot(data.T, data) / 100
lan, e = LA.eig(corr_mat)
print (lan[0], '\n', e[:, 0], '\n', corr_mat, '\n\n')

N = 1
alpha = 1.0
delta_t = 0.01
w = np.random.rand(2)
print(type(w))

for z in range (5):
    for i in np.arange(0, 100000, 1):
        v = np.dot(data[i%100, :], w)
        w = w + delta_t * N * (v*data[i%100,:])# - alpha*v*v*w)
    print('mu = {} --- v = {} --- w = {}\n'.format(np.mean(data, axis=0), v, w))
    data[:,0] += z
    data[:,1] += z * 1/4
    '''if (i%1000 == 0):
        w_ev.append(w) 
w_ev = np.asarray(w_ev)
'''
