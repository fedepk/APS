# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 10:22:10 2026

@author: Fede
"""

import sys
import os
directorio_actual = os.path.dirname(os.path.abspath(__file__))
directorio_padre = os.path.abspath(os.path.join(directorio_actual, '..'))
sys.path.insert(0, directorio_padre)
import gen_fun as gen
import numpy as np
import matplotlib.pyplot as plt


#%%   ------------------ Definiciones

N = 1000
fs = 1000
Vfs = 1.5
f = 1
bits = 4
k = 1

#%%   ------------------- Codigo

q=2*Vfs/(2**bits)
pq=q**2/12
pn = k * pq

tt,xx = gen.senoidal(pot = 1,fs = fs,nn = N,ff=f)
ttn,nx = gen.ruido_normal(pot = pn,nn = N,fs = fs)

xn = xx + nx

xq= gen.cuant(xn, bits, Vfs)

nq = xq - xn

NX = 1/N * np.fft.fft(nx)
NX_db = 10 * (np.log10((np.abs(NX)**2)*2))

pot_nx = sum((np.abs(NX)**2))/(N/2)
pot_nx = 10 * (np.log10(pot_nx))


XN = 1/N * np.fft.fft(xn)
XN_db = 10 * (np.log10((np.abs(XN)**2)*2))

NQ = 1/N * np.fft.fft(nq)
NQ_db = 10 * (np.log10((np.abs(NQ)**2)*2))

pot_nq = sum((np.abs(NQ)**2))/(N/2)
pot_nq = 10 * (np.log10(pot_nq))


XX = 1/N * np.fft.fft(xx)
XX_db = 10 * (np.log10((np.abs(XX)**2)*2))

XQ = 1/N * np.fft.fft(xq)
XQ_db = 10 * (np.log10((np.abs(XQ)**2)*2))

frec = tt*(fs/N)
frec = frec[:(N//2)]


pn = 10 * np.log10(pn/(N/2))
pq = 10 * np.log10(pq/(N/2))

tt = tt*(f/N)

#%% 2. CONFIGURACIÓN DEL PLOT AMPLITUD
# =====================================================================
plt.figure(figsize=(14, 6))

# Plot de la señal cuantizada (xq): Línea continua azul, más gruesa
plt.plot(tt, xq, 
         label=r'$x_q = Q_{B,Vfs}\{s_R\}$ (ADC out)', 
         color='tab:blue', 
         linewidth=2)

# Plot de la señal con ruido (xx): Línea punteada verde con círculos huecos
plt.plot(tt, xn, 
         label=r'$x_n = x + n$ (ADC in)', 
         color='forestgreen', 
         linestyle=':', 
         marker='o', 
         markerfacecolor='none', 
         markersize=3, 
         linewidth=1.5)

plt.plot(tt, xx, 
         label=r'$x (senoidal)', 
         color='orange', 
         linestyle='-',  
         markerfacecolor='none', 
         markersize=3, 
         linewidth=1.5)

# Título y etiquetas (usando raw strings 'r' para el formato matemático)
plt.title(rf'Señal muestreada por un ADC de {bits} bits - $\pm Vfs$ = {Vfs} V - q = {q} V')
plt.xlabel('Tiempo [segundos]')
plt.ylabel('Amplitud [V]')
# Configuración de la leyenda (ubicada arriba a la derecha como en tu imagen)
plt.legend(loc='upper right')

# Ajuste de los márgenes y muestra en pantalla
plt.tight_layout()


#%% 2. CONFIGURACIÓN DEL PLOT ESPECTRO
# =====================================================================

plt.figure(figsize=(14, 6))

# 1. Espectro de la señal cuantizada (ADC out): Línea continua azul
plt.plot(frec, XQ_db[:(N//2)], 
         label=r'$X_q = Q_{B,Vfs}\{x_n\}$ (ADC out)', 
         color='tab:blue', 
         linewidth=1.5)

# 2. Espectro de la señal con ruido (ADC in): Línea punteada verde
plt.plot(frec, XN_db[:(N//2)], 
         label=r'$X_n = s + n$  (ADC in)', 
         color='forestgreen', 
         linestyle=':', 
         linewidth=1.5)


# 3. Piso de ruido analógico: Línea horizontal rayada roja
# Se usa hlines para dibujar una recta desde la primera hasta la última frecuencia
plt.hlines(pot_nx, frec.min(), frec.max(), 
           label=fr'$\overline{{n_x}} =$ {pot_nx:.1f} dB (piso analog.)', 
           color='red', 
           linestyle='--')

plt.plot(frec, NX_db[:(N//2)], 
         color='red', 
         linestyle=':', 
         linewidth=1.5)


# 4. Piso de ruido digital: Línea horizontal rayada cian
plt.hlines(pot_nq, frec.min(), frec.max(), 
           label=fr'$\overline{{n_Q}} =$ {pot_nq:.1f} dB (piso digital)', 
           color='c', 
           linestyle='--')

plt.plot(frec, NQ_db[:(N//2)], 
         color='c', 
         linestyle=':', 
         linewidth=1.5)

# Título dinámico (usando f-string) y etiquetas de ejes
titulo = fr'Señal muestreada por un ADC de {bits} bits - $\pm Vfs =$ {Vfs} V - q = {q} V'
plt.title(titulo)
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Densidad de Potencia [dB]')

# Leyenda ubicada arriba a la derecha
plt.legend(loc='upper right')

# Ajuste de márgenes y renderizado
plt.tight_layout()
plt.show()
