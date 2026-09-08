# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 09:03:20 2026

    Funciones:    
        
    senoidal( vmax = None, pot = None, dc=0 , ff=1 , ph=0 , nn=1000 , fs=1000,snr = None,opcion_ruido = None):
        
    cuadrada_duty( vmax = None, pot = None, dc=0 , ff=1 ,duty=50, nn=1000 , fs=1000):
        
    ruido_normal(pot = 1, dc=0 , nn=1000 , fs=1000):
        
    ruido_uniforme(pot = 1, dc=0 , nn=1000 , fs=1000):
        
    cuant(xx,n_bits,Vfs):
        
    triangular( vmax = None, pot = None, dc=0 , ff=1 ,duty=50, nn=1000 , fs=1000,ph = 0):
    
@author: Fede
"""

#%% ---------------------- Generador de señales

import numpy as np
import scipy.signal as sp
import matplotlib.pyplot as plt


#%% ---------------------- Ruido normal

def ruido_normal(pot = 1, dc=0 , nn=1000 , fs=1000):
    
    tt=np.arange(0,nn,1)
    desvio = np.sqrt(pot)
    xx = np.random.normal(0,desvio,nn)
    
    return tt , xx

#%% ---------------------- Ruido uniforme

def ruido_uniforme(pot = 1, dc=0 , nn=1000 , fs=1000):
    
    tt=np.arange(0,nn,1)
    a = np.sqrt(3*pot)
    xx = np.random.uniform(-a,a,nn)
    
    return tt , xx

#%% ---------------------- Senoidal
    
def senoidal( vmax = None, pot = None, dc=0 , ff=1 , ph=0 , nn=1000 , fs=1000,snr = None,opcion_ruido = None):
    
    """
    Señal senoidal. 
    
    pot: float
         Potencia de la señal (introducir potencia o amplitud)
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
    if vmax is None and pot is None:
        raise ValueError("Debe introducir vmax o potencia")
        
    if vmax is None:
        vmax = np.sqrt(2 * pot)
        pot_sen = pot
    else:
        pot_sen = vmax**2   
    
    tt=np.arange(0,nn,1)
    xx = vmax * np.sin(2*np.pi*ff*tt/fs + ph) + dc
    
    if snr is not None:
        pot_ruido =  (10**(-snr/10))* pot_sen
        if opcion_ruido == "uniforme" :
            _,ruido = ruido_uniforme(pot = pot_ruido)
            xx = xx + ruido
        else:
            _,ruido = ruido_normal(pot = pot_ruido)
            xx = xx + ruido
        
    return tt , xx


#%% ---------------------- cuadrada duty
    
def cuadrada_duty( vmax = None, pot = None, dc=0 , ff=1 ,duty=50, nn=1000 , fs=1000):
        
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
        if vmax is None and pot is None:
            raise ValueError("Debe introducir vmax o potencia")
            
        if vmax is None:
            vmax = np.sqrt(pot)
            
        else:
            pot = vmax**2   
            
        tt=np.arange(0,nn,1)
        duty = duty/100

        xx = (vmax * (sp.square(2*np.pi*ff*tt/fs,duty))) + dc

        return tt,xx 
    
#%% ---------------------- Cuantizador
    
def cuant(xx,n_bits,Vfs):
            
        """
        Cuantiza una señal  
        
          xx: Vector de valores
          
          n_bits: Numero de bits
          
          Vfs: Tension Full Scale
        
        Retorna vector x (amplitud)
        """
        N = (2**n_bits)
        q =2 * Vfs/N
        x = np.round(xx/q)*q
        return x 

# def cuant2(xx,n_bits,Vfs):
            
#         """
#         Cuantiza una señal  
        
#           xx: Vector de valores
          
#           n_bits: Numero de bits
          
#           Vfs: Tension Full Scale
        
#         Retorna vector x (amplitud)
#         """
#         N = (2**n_bits)
#         xx = (xx + (Vfs/2))/Vfs
#         xx = np.clip(xx,0,1)
#         x = np.round(xx*(N-1))
#         return x

#%% ---------------------- Triangular

def triangular( vmax = None, pot = None, dc=0 , ff=1 ,duty=50, nn=1000 , fs=1000,ph = 0):
        
        """
        Señal triangular. 
        
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
        if vmax is None and pot is None:
            raise ValueError("Debe introducir vmax o potencia")
            
        if vmax is None:
            vmax = np.sqrt(pot)
            
        else:
            pot = vmax**2   
            
        tt=np.arange(0,nn,1)


        xx = (vmax * (sp.sawtooth((2*np.pi*ff*tt/fs+ph+np.pi/2),0.5))) + dc

        return tt,xx 

#%% ---------------------- Grafico Espectro

def espectro(t,x,N,fs,xlim_min = None , xlim_max = None):
    
    frec = t*(fs/N)
    X = 1/N * np.fft.fft(x)
    X_arg = np.angle(X)
    X_db = 10 * (np.log10((np.abs(X)**2)*2))    # A db (escala 0db 1W)

    fig, ax = plt.subplots(2, 1, figsize=(10, 6),layout="constrained")
    
    x_max = N//2
    x_min = 0
    
    if xlim_max is not None : x_max = xlim_max
    if xlim_min is not None : x_min = xlim_min    

# --- Subplot 0: Espectro de Magnitud ---
    ax[0].plot(frec[x_min:x_max], X_db[x_min:x_max], linewidth=1.2, color='#1f77b4')
    ax[0].set_title("Densidad espectral de potencia", fontsize=11, fontweight='bold')
    ax[0].set_ylabel("Amplitud [dB]", fontsize=10)
    ax[0].grid(True, which='both', linestyle='--', alpha=0.5)
    ax[0].minorticks_on()

# --- Subplot 1: Fase ---
    ax[1].plot(frec[x_min:x_max], X_arg[x_min:x_max], linewidth=1.2, color='#ff7f0e')
    ax[1].set_title("Fase", fontsize=11, fontweight='bold')
    ax[1].set_xlabel("Frecuencia [Hz]", fontsize=10)
    ax[1].set_ylabel("Fase [rad]", fontsize=10)
    ax[1].set_yticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi])
    ax[1].set_yticklabels([r'$-\pi$', r'$-\pi/2$', r'$0$', r'$\pi/2$', r'$\pi$'])
    ax[1].grid(True, which='both', linestyle='--', alpha=0.5)
    ax[1].minorticks_on()

    
#%% zero padding
    
def zero_padding(xx, factor = 10):
    nuevo_N = factor * len(xx)
    pad = np.zeros(nuevo_N-len(xx), dtype=float)
    xx = np.concatenate((xx,pad))
    tt = np.arange(0,nuevo_N,1)
    return(xx,tt)


