#!/usr/bin/env python3

#Default Modules:
import numpy as np
import pandas as pd
import scipy 
import matplotlib.pyplot as plt
import os, glob, sys
from tqdm import tqdm
from astropy import units as u



#Other Modules:

##### Author: Alex Polanski #####

xmin = 0
xmax = 1
num_sections = 100


def sin_square(x):
    
    # This is the function I am trying to integrate


    return np.sin(x)**2


def trap(func,xmin,xmax,num):

    # Trapezoidal integration


    x = np.linspace(xmin,xmax,num)

    y = func(x)

    dx = np.diff(x)

    sides = (y + np.roll(y,1))[1:]/2

    return( sum(sides*dx) )


val = trap(sin_square,xmin,xmax,num_sections)

print(f"Trapezoidal Integration:\nXmin = {xmin}\nXmax = {xmax}\nNumber of Portions = {num_sections}\n\nIntegral Value = {val:0.4}")

