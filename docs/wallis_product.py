"""
looking at wallis product for pi/2
"""

# import libraries
import numpy as np
import matplotlib.pyplot as plt

# close all plots
plt.close('all')

# generate numbers and sequences via an upper bound
ub = 100
num = np.append(np.repeat(np.arange(2,ub,2),2),ub)
den = np.insert(np.repeat(np.arange(3,ub+1,2),2),0,1)

# empty lists for two methods
wallis1, wallis2, wallis3 = [], [], []

### method 1 - calculate numerator, then denominator, then divide ###

# iterate through arrays and calculate
for i in range(len(num)):
    wallis1.append(np.prod(num[:i+1])/np.prod(den[:i+1]))

### method 2 - calculate num/denom of each term, then multiply ###

# iterate through arrays and calculate
for i in range(len(num)):
    wallis2.append(np.prod(num[:i+1]/den[:i+1]))

### method 3 - using production summation definition ###

# start with the first term of the series
wallis3_val = 4.0/3.0

# now start iterations from n=2
for n in range(2, ub):
    wallis3_val *= (4*n**2)/(4*n**2-1)
    wallis3.append(wallis3_val)


### create figures

fig,ax = plt.subplots()
plt.rcParams.update({'font.size': 18})
ax.plot(wallis1,label='Method 1')
ax.plot(wallis2,label='Method 2',color='g')
ax.plot(wallis3,label='Method 3',color='r')
ax.set_xlabel('# of Iterations $(n)$')
ax.set_ylabel('Value')
ax.axhline(np.pi/2.0,color='k',linestyle='--',label=r'$\pi/2$')
ax.axhline(0,color='k',linewidth=0.8)
ax.axvline(0,color='k',linewidth=0.8)
plt.legend()
ax.set_title('Wallis Product')
plt.tight_layout()