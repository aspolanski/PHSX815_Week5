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
from mpl_toolkits.mplot3d import Axes3D

#This desn't work well, not sure why but I tried

##### Author: Alex Polanski #####


def lorentz(x,y, gamma):
    
    # this is my target distribution

    return 1.0 / (np.pi*gamma*(1+ (x**2 + y**2)/(gamma**2) ))

C = 1.0

keeps_x = []
keeps_y = []
N = 100000

for i in range(N):

    sample_x, sample_y = np.random.uniform(-6,6), np.random.uniform(-6,6)

    sample_uniform = np.random.uniform(0,1)
    
    target_eval = lorentz(sample_x, sample_y, 1.0)

    if sample_uniform <= (target_eval/ C):
        keeps_x.append(sample_x)
        keeps_y.append(sample_y)

    else:
        pass


x = np.linspace(-6,6,1000)
y = np.linspace(-6,6,1000)

X, Y = np.meshgrid(x,y)

hist, xedges, yedges = np.histogram2d(keeps_x, keeps_y, bins=100, range=[[-6, 6], [-6, 6]],density=False)
xpos, ypos = np.meshgrid(xedges[:-1] + 0.25, yedges[:-1] + 0.25)
xpos = xpos.flatten('F')
ypos = ypos.flatten('F')
zpos = np.zeros_like(xpos)
dx = 0.5 * np.ones_like(zpos)
dy = dx.copy()
dz = hist.flatten()


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color='b', zsort='average')

#ax.plot_surface(X,Y,lorentz(X,Y,1.5),alpha=0.3,color='orange')

plt.show()
