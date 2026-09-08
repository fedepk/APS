# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 08:40:00 2026

@author: Fede
"""
import numpy as np
import matplotlib.pyplot as plt
import gen_fun as gen
from scipy import stats as st



#%% --------------------------------- Definiciones

fs = 1000
N = 1000
f = 2
Vfs = 2
pot = 1
bits = 4
k = 0.1
k0 = N/4
factor = 10

#%% ---------------------------- Ruido cuantizacion

q=2*Vfs/(2**bits)

pq=q**2/12

pn = k * pq

snr = 10 * np.log10(1/pn)

f = (k0)*fs/N

tt,xx= gen.senoidal(pot=1,ff=f,fs=fs,nn =N )

f1=(k0+0.25)*fs/N

tt1,xx1= gen.senoidal(pot=1,ff=f1,fs=fs,nn =N )

f2=(k0+0.5)*fs/N

tt2,xx2= gen.senoidal(pot=1,ff=f2,fs=fs,nn =N )


#%%-------------------------- FFT


xx,tt =gen.zero_padding(xx)
xx1,tt =gen.zero_padding(xx1)
xx2 ,tt=gen.zero_padding(xx2)

N2 = N*factor

frec = np.arange(int(N2 / 2)) * (fs / N2)


X = 1/N * np.fft.fft(xx)
X1 = 1/N * np.fft.fft(xx1)
X2 = 1/N * np.fft.fft(xx2)

pot_frec = sum((np.abs(X)**2))/factor
print(pot_frec)

pot_frec = sum((np.abs(X1)**2))/factor
print(pot_frec)

pot_frec = sum((np.abs(X2)**2))/factor
print(pot_frec)

X_db = 10 * (np.log10((np.abs(X)**2)*2))
X_db1 = 10 * (np.log10((np.abs(X1)**2)*2))
X_db2 = 10 * (np.log10((np.abs(X2)**2)*2))



#%%      --------------- cuantizado

# xq,q = gen.cuant(xx,bits,Vfs)

# nq = xq - xx

# NQ = 1/N * np.fft.fft(nq)

# NQ_db = 10 * (np.log10((np.abs(NQ)**2)*2))

#%% 
# print ("q**2/12 = ",(q**2)/12)
# print("varianza = ",np.var(nq))

# cc = np.correlate(nq,nq,mode = 'full')
# cc = cc/N
# n= np.arange(0,2*N-1,1)

# a = -(q/2)
# b = (q/2)

# res = st.kstest(nq, 'uniform', args=(a, b - a))
# alpha = 0.05  # Nivel de significancia (95% de confianza)

# estadistico_D = res.statistic
# p_valor = res.pvalue

# print("-" * 50)
# print(f"P-valor obtenido:    {p_valor:.5e}")
# print("-" * 50)

# if p_valor > 0.05:
#     print("Conclusión: La señal es compatible con una distribución uniforme U(a, b).")
# else:
#     print("Conclusión: La señal NO sigue una distribución uniforme.")
#     print("-" * 50)



#%% ----------------------------------------------ploteos

fig, ax = plt.subplots(1, 1, figsize=(10, 6),layout="constrained")

# --- Subplot 0: Espectro de Magnitud ---
ax.plot(frec,X_db[:int(N2 / 2)], linewidth=1.2)
ax.plot(frec,X_db1[:int(N2 / 2)], linewidth=1.2)
ax.plot(frec,X_db2[:int(N2 / 2)], linewidth=1.2)

ax.set_title("Espectro de potencia normalizado", fontsize=11, fontweight='bold')
ax.set_ylabel("Potencia [dB]", fontsize=10)
ax.set_xlabel("Frecuencia [Hz]")
ax.set_xlim([240, 260])
ax.set_ylim(-60)
ax.grid(True, which='both', linestyle=':', alpha=0.5)
ax.minorticks_on()

# --- Subplot 1: Fase ---
# ax[1].plot(frec[:N // 2], X_arg[:N // 2], linewidth=1.2, color='#ff7f0e')
# ax[1].set_title("Fase", fontsize=11, fontweight='bold')
# ax[1].set_xlabel("Frecuencia [Hz]", fontsize=10)
# ax[1].set_ylabel("Fase [rad]", fontsize=10)
# ax[1].set_xlim(0, frec[N // 2 - 1])
# ax[1].set_ylim(-np.pi * 1.05, np.pi * 1.05)
# ax[1].set_yticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi])
# ax[1].set_yticklabels([r'$-\pi$', r'$-\pi/2$', r'$0$', r'$\pi/2$', r'$\pi$'])
# ax[1].grid(True, which='both', linestyle='--', alpha=0.5)
# ax[1].minorticks_on()

# plt.figure(4)
# plt.plot(tt,xq,':',marker="o",markersize=2,alpha=0.8, linewidth=0.7, markerfacecolor='none')
# plt.grid()
# plt.title("Señal cuantizada")
# plt.xlabel("Tiempo [s]")
# plt.ylabel("Amplitud")

# plt.figure(5)
# plt.plot(n,cc,'.')
# plt.grid()
# plt.title("Autocorrelacion")

# plt.figure(6)
# plt.plot(tt,nq,'.')
# plt.grid()
# plt.title("Ruido de cuantizacion")




