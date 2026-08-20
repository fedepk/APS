# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 09:03:20 2026

@author: Fede
"""
import matplotlib.pyplot as plt
import numpy as np


#%%  Definiciones


#%%  Funcion generador de señales

def senoidal( vmax=1 , dc=0 , ff=1 , ph=0 , nn=1000 , fs=1000):
    
    """
    Señal senoidal. 
    
    vmax: float
         Amplitud de la señal.
    dc: float
         Nivel de continua.
    ff: float
         Frecuencia en Hz.
    ph: float
         Fase en radianes.
    nn: int
         Cantidad de muestras.
    fs: float
         Frecuencia de muestreo en Hz.
    """
    
    tt=np.arange(0,nn,1)
    xx = vmax * np.sin(2*np.pi*ff*tt/fs + ph) + dc
    
    return tt , xx

def cuadrada( vmax=1 , dc=0 , ff=1 , ph=0 , nn=1000 , fs=1000):
    
    """
    Señal cuadrada. 
    
    vmax: float
         Amplitud de la señal.
    dc: float
         Nivel de continua.
    ff: float
         Frecuencia en Hz.
    ph: float
         Fase en radianes.
    nn: int
         Cantidad de muestras.
    fs: float
         Frecuencia de muestreo en Hz.
    """
    
    tt=np.arange(0,nn,1)
    xx = vmax * np.sign(np.sin(2*np.pi*ff*tt/fs + ph) )+ dc

    return tt,xx 
    
def cuadrada_duty( vmax=1 , dc=0 , ff=1 ,duty=50, nn=1000 , fs=1000):
        
        """
        Señal cuadrada con posibilidad de modificar duty cycle. 
        
        vmax: float
             Amplitud de la señal.
        dc: float
             Nivel de continua.
        ff: float
             Frecuencia en Hz.
        duty: float
             Duty cycle en %.
        nn: int
             Cantidad de muestras.
        fs: float
             Frecuencia de muestreo en Hz.
        """
        
        tt=np.arange(0,nn,1)
        T = fs/ff
        r = (tt % T)/T
        xx = vmax * np.where(r < duty/100, 1,0) + dc

        return tt,xx 




