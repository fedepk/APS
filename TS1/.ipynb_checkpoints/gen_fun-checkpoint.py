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
import scipy.signal as sp


#%%  Funcion generador de señales

def ruido_normal(pot = 1, dc=0 , nn=1000 , fs=1000):
    
    tt=np.arange(0,nn,1)
    desvio = np.sqrt(pot)
    xx = np.random.normal(0,desvio,nn)
    
    return tt , xx

def ruido_uniforme(pot = 1, dc=0 , nn=1000 , fs=1000):
    
    tt=np.arange(0,nn,1)
    a = np.sqrt(3*pot)
    xx = np.random.uniform(-a,a,nn)
    
    return tt , xx
    
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
    
    
def cuant(xx,n_bits,Vfs):
            
        """
        Cuantiza una señal  
        
          xx: Vector de valores
          
          n_bits: Numero de bits
          
          Vfs: Tension Full Scale
        
        Retorna vector x (amplitud)
        """
        N = (2**n_bits)
        q =2 * Vfs/(N-1)
        x = np.round(xx/q)*q
        # x =  np.clip(x,((-N/2)+1),N/2)
        return x , q

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

tt,xx = cuadrada_duty( vmax=1 , dc=0 , ff=10 ,duty=50, nn=1000 , fs=1000)

