import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
import math

#initialize vars
mu = 5
sigma = 0.5
mu2 = 7
sigma2 = 1

#compute funcs
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
y = np.linspace(mu2 - 3*sigma2, mu2 + 3*sigma2, 100)
s1 = mlab.normpdf(x, mu, sigma);
s2 = mlab.normpdf(y, mu2, sigma2);

#plot gaussians
plt.plot(x, s1, 'r-', label='s1')
plt.plot(y, s2, label='s2')
plt.xlabel('Firing rate response');
plt.ylabel('Probability');

#compute loss function
loss1 = 2 * s1;
plt.plot(x, loss1, 'g-', label='loss1')

#find intersec
def solve(m1,m2,std1,std2):
    a = 1/(2*std1**2) - 1/(2*std2**2)
    b = m2/(std2**2) - m1/(std1**2)
    c = m1**2 /(2*std1**2) - m2**2 / (2*std2**2) - np.log(std2/std1)
    return np.roots([a,b,c])
result = solve(mu, mu2, sigma, sigma2)
print(result)
#launch plotting
plt.legend();
plt.show()
