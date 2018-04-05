import pickle
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import spline


with open('data.pickle', 'rb') as f:
    data = pickle.load(f)

with open('pop_coding.pickle', 'rb') as f:
    pop_coding = pickle.load(f)

stim = data['stim']
del data['stim']

keys = list(data.keys())

max_rates = []
#compute max_rate
for neuron in keys:
    trans_neur = np.transpose(data[neuron])
    mfr = [np.mean(trans_neur[t]) for t in range(24)]
    max_rates.append([neuron, max(mfr)])

max_rates = list(reversed(max_rates))
#separate bas_vec and rates
bas_vec = {k: pop_coding[k] for k in ('c1', 'c2', 'c3', 'c4')}
bas_vec = [bas_vec[i] for i in sorted(bas_vec.keys())]
for k in list(bas_vec.keys()):
    del pop_coding[k]
it = 0
vec_fi = [0, 0]
print(bas_vec)
for i in sorted(pop_coding.keys()):
    vec_fi += (np.mean(pop_coding[i] / max_rates[it][1])) * bas_vec[it]
    print(vec_fi)
    #print(max_rates[it])
    it += 1;
