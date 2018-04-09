import pickle
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import spline
import math

with open('data.pickle', 'rb') as f:
    data = pickle.load(f)

with open('pop_coding.pickle', 'rb') as f:
    pop_coding = pickle.load(f)

stim = data['stim']
del data['stim']

keys = list(sorted(data.keys()))

#compute max_rate
max_rates = []
for neuron in keys:
    trans_neur = np.transpose(data[neuron])
    mfr = [np.mean(trans_neur[t]) for t in range(24)]
    max_rates.append([neuron, max(mfr)])
max_rates = list(max_rates)

#separate bas_vec and rates in pop_coding data
bas_vec = {k: pop_coding[k] for k in ('c1', 'c2', 'c3', 'c4')}
bas_vec_list = []
for k in sorted(bas_vec.keys()):
    del pop_coding[k]
    bas_vec_list.append(bas_vec[k]) 
bas_vec = bas_vec_list

#compute population vector
it = 0
vec_fi = [0, 0]
for i in sorted(pop_coding.keys()):
    vec_fi += (np.mean(pop_coding[i]) / max_rates[it][1]) * bas_vec[it]
    it += 1;
print(bas_vec)
print(pop_coding)
print(90 - math.degrees(math.atan2(vec_fi[1], vec_fi[0])))
