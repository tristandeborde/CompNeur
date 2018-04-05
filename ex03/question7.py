import pickle
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import spline


##QUESTION 1
with open('data.pickle', 'rb') as f:
    data = pickle.load(f)

stim = data['stim']
del data['stim']

keys = list(data.keys())

for neuron in keys:
    mfr = [np.mean(np.transpose(data[neuron])[t]) for t in range(24)]
    max_rate = max(mfr)
    mfr = [rate / max_rate for rate in mfr]
    stim_new = np.linspace(stim.min(),stim.max(),300)
    mfr_smooth = spline(stim,mfr,stim_new)
    plt.plot(stim, mfr, label=neuron)


plt.xlabel('Direction of air velocity stimuli in degrees')
plt.ylabel('Firing rate of neuron in Hz')
plt.show()

##QUESTION 2
with open('pop_coding.pickle', 'rb') as f:
    data = pickle.load(f)
