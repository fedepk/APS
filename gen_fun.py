# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 09:03:20 2026

    Funciones:    
        
    senoidal( vmax=1 , dc=0 , ff=1 , ph=0 , nn=1000 , fs=1000):
        
    cuadrada( vmax=1 , dc=0 , ff=1 , ph=0 , nn=1000 , fs=1000):
        
    cuadrada_duty( vmax=1 , dc=0 , ff=1 ,duty=50, nn=1000 , fs=1000):
        
    snr( vmax=1 , dc=0 , ff=1 , ph=0 , nn=1000 , fs=1000,snr = 10):
    
@author: Fede
"""
import numpy as np


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
        
        
    Retorna vectores tt y xx (tiempo y amplitud)
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
                 
        
    Retorna vectores tt y xx (tiempo y amplitud)
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
                     
        
        Retorna vectores tt y xx (tiempo y amplitud)
        """
        
        tt=np.arange(0,nn,1)
        T = fs/ff
        r = (tt % T)/T
        xx = vmax * np.where(r < duty/100, 1,0) + dc

        return tt,xx 
    
def snr( vmax=1 , dc=0 , ff=1 , ph=0 , nn=1000 , fs=1000,snr = 10):
        
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
        snr: Relacion señal ruido en db
        
        
        Retorna vectores tt y xx (tiempo y amplitud)
        """
        
        tt=np.arange(0,nn,1)
        xx = vmax * np.sin(2*np.pi*ff*tt/fs + ph) + dc
        pot_sen = np.mean(xx**2)
        pot_ruido =  10**(-snr/10) 
        pot_ruido = pot_ruido *pot_sen
        desvio = np.sqrt(pot_ruido)
        ruido = np.random.normal(0,desvio,nn)
        xx = xx + ruido
        
        return tt , xx




