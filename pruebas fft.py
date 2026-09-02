# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 08:40:00 2026

@author: Fede
"""
import numpy as np
import matplotlib.pyplot as plt
import gen_fun as gen
from scipy import stats as st



# -----------------------------------------Definiciones

fs = 1000
N = 1000
f = 4
snr = 40
Vfs = 1.65

# ----------------------------------------------Codigo

tt,xx= gen.triangular(pot = 12,ff = 2)
# tt,xx= gen.snr_norm(vmax = 1.41,ff=f,fs=fs,nn =N,snr = snr)

# frec = tt*(fs/N)
# frec = frec[:int(N/2)]

# X = 1/N * np.fft.fft(xx)

# pot_frec = np.sum((np.abs(X)**2))
# print(pot_frec)

# X_arg = np.angle(X)

# X_db = 10 * (np.log10((np.abs(X)**2)*2))

# xq,q = gen.cuant(xx,8,Vfs)

# nq = xq - xx
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



# ----------------------------------------------ploteos

plt.close("all")

plt.plot(tt,xx)
plt.grid()
plt.title("Senoidal")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud [V]")

# fig, ax = plt.subplots(2, 1, figsize=(10, 6),layout="constrained")

# ax[0].plot(frec,X_db[:int(N/2)])
# ax[0].grid()
# ax[0].set_title("Espectro")
# ax[0].set_xlabel("Frecuencia [Hz]")
# ax[0].set_ylabel("Amplitud [dB]")

# ax[1].plot(frec,X_arg[:int(N/2)])
# ax[1].grid()
# ax[1].set_title("Fase")
# ax[1].set_xlabel("Frecuencia [Hz]")
# ax[1].set_ylabel("Fase")

# plt.figure(4)
# plt.plot(tt,xq,'.')
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




