#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 10:12:46 2018

@author: donaldferguson
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cmx
import matplotlib as mpl

DATA = np.random.rand(5,5)

cmap = plt.cm.jet

cNorm  = colors.Normalize(vmin=np.min(DATA[:,4]), vmax=np.max(DATA[:,4]))

scalarMap = cmx.ScalarMappable(norm=cNorm,cmap=cmap)

fig = plt.figure()
ax  = fig.add_axes([0.1, 0.1, 0.7, 0.85]) # [left, bottom, width, height]
axc = fig.add_axes([0.85, 0.10, 0.05, 0.85])

for idx in range(0,len(DATA[:,1])):
    colorVal = scalarMap.to_rgba(DATA[idx,4])
    print("Colorval = ", colorVal)
    ax.arrow(DATA[idx,0],  # x1
             DATA[idx,1],  # y1
             DATA[idx,2]-DATA[idx,0], # x2 - x1
             DATA[idx,3]-DATA[idx,1], # y2 - y1
             color=colorVal)

cb1 = mpl.colorbar.ColorbarBase(axc, cmap=cmap,
                                norm=cNorm,orientation='vertical')

plt.show() 