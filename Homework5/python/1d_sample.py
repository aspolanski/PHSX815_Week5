#!/usr/bin/env python3

#Default Modules:
import numpy as np
import pandas as pd
import scipy 
import matplotlib.pyplot as plt
import os, glob, sys
from tqdm import tqdm
from astropy import units as u

plt.style.use("/home/custom_style1.mplstyle")

#Other Modules:

##### Author: Alex Polanski #####


def targ(x):
    # This is my target distribution
    return (np.sin(x)**2)/np.pi

def get_scale():
    #roughly approximates the scaling factor needed for the proposal distribution
    x = np.random.uniform(0,2*np.pi,100)
    y = targ(x)

    return(np.max(y))



keeps = []

N = 1000000

C = get_scale()

for i in range(N):
    sample_prop = np.random.uniform(0.0,2*np.pi) #sample our proposal dist (a uniform one, in this case)
    sample_uniform = np.random.uniform(0.0,1.0) #sample a random number on the interval [0,1]
    target_eval = targ(sample_prop) #evaluate our target function at our proposal sample

    if sample_uniform <= (target_eval/ C):
        keeps.append(sample_prop)

    else:
        pass


# Plot stuff


x = np.linspace(0.0,2*np.pi,100)

fig, ax = plt.subplots(figsize = (11,8.5))

ax.hist(keeps, bins=100, density=True, alpha=0.6, label="Target\nSample")
ax.plot(x, targ(x), linewidth=3.0, linestyle='dashed',label="Target")
ax.hlines(C, xmin=0.0, xmax = 2*np.pi, linewidths=3.0, colors='red', label="Proposal")
ax.set_xlabel("Value")
ax.set_ylabel("Probability? Idk Density = True")
ax.legend(loc='center left')


plt.show()
