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


def generador_triangular(vmax, dc, ff, ph, nn, fs):
    
    tt = np.arange(0, nn, 1)
    
    xx = vmax * (2 * np.abs(2 * (ff * tt / fs + ph / (2*np.pi)- np.floor(ff * tt / fs + ph / (2*np.pi) + 0.5))) - 1) + dc
    
    return tt, xx
#%%  Inicio script

tt , xx = generador(np.sqrt(2),0,1,0,1000,1000)



#plt.plot(tt,xx)
#plt.axhline(0, linestyle='--' , color = 'black', linewidth=1)


snr = 10
potnq =  10**(-snr/10)

desvio = np.sqrt(potnq)

nq = np.random.normal(0,desvio,1000)

plt.plot(tt,xx + nq)
plt.axhline(0, linestyle='--' , color = 'black', linewidth=1)

 
print( np.var(xx)/np.var(nq))

