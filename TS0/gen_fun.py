# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 09:03:20 2026

@author: Fede
"""
import matplotlib.pyplot as plt
import numpy as np


#%%  Definiciones


#%%  Funcion generador de señales

def generador( vmax , dc , ff , ph , nn , fs):
    
    tt=np.arange(0,nn,1)

    xx = vmax * np.sin(2*np.pi*ff*tt/fs + ph) + dc
    
    return tt , xx

#%%  Inicio script

tt , xx = generador(1,0,2,0,1000,1000)

plt.plot(tt,xx)
plt.axhline(0, linestyle='--' , color = 'black', linewidth=1)


