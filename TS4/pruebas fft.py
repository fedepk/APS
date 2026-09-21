# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 10:22:10 2026

@author: Fede
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.signal.windows as sp



#%% --------------------------------- Definiciones

fs = 1000
N = 1000
a = 2
v_max = np.sqrt(2)
M = 200
snrs = [3, 10]
bin_f0 = N//4
snr = 10

ventanas = {
    'Rectangular': np.ones(N),
    'Flat-top': sp.flattop(N),
    'Blackman': sp.blackmanharris(N),
    'Hann': sp.hann(N)     # Otra ventana de scipy
}

resultados = {snr: {name: {} for name in ventanas} for snr in snrs}


#%% ------------------------- Calculos para todas las ventanas y snrs

df = fs/N

tt=np.arange(0,N,1)
fr = np.random.uniform(-a,a,M)
f = (fs/4+fr*fs/N)
tt = tt.reshape(N, 1)
frec = np.arange(int(N / 2)) * (fs / N)

for snr in snrs:
    
    xx = v_max * np.sin(2 * np.pi * f * tt / fs)
    pot = np.sqrt(10**(-snr/10))
    n_a = np.random.normal(0, pot, (N, M))
    xx = xx + n_a
    
    for nombre_vent, ventana in ventanas.items():
        ventana_col = ventana.reshape(N, 1)
        x_v = xx * ventana_col
        X_V = (2/N)*np.fft.fft(x_v, axis=0)
        X_V = X_V[:(N//2),:]
        
        X_V_pot = (np.abs(X_V)**2) / df
        X_V_db = 10 * np.log10(X_V_pot)
        
        # escala = 2 / np.sum(ventana)
        
        a_est = np.abs(X_V[bin_f0, :]) #* escala  --------- estimador a
        
        bines_maximo = np.argmax(np.abs(X_V), axis=0)
        omega_est = bines_maximo * (2 * np.pi / N)

        resultados[snr][nombre_vent]['a_est'] = a_est
        resultados[snr][nombre_vent]['omega_est'] = omega_est
        
        a_est = (np.abs(X_V[bin_f0,:])) *2
        esperado = np.mean(a_est) 
        print(esperado)

#%% -------------------------- Ploteo histogramas

for snr in snrs:
    fig, ax = plt.subplots(figsize=(10, 6), layout="constrained")
    ax.set_title(f'Distribución de Estimación de Amplitud (SNR = {snr} dB)', fontsize=12, fontweight='bold')
    ax.set_xlabel(r'Amplitud estimada $\hat{a}_1$')
    ax.set_ylabel('Frecuencia Relativa')
    
    for nombre_vent in ventanas.keys():
        ax.hist(resultados[snr][nombre_vent]['a_est'], bins=20, alpha=0.5, label=nombre_vent)
        
    ax.axvline(v_max, color='red', linestyle='dashed', linewidth=2, label=f'Valor Real ($a_0={v_max:.3f}$)')
    ax.legend()
    ax.grid(True, linestyle=':', alpha=0.7)
    plt.show()
    
    #%% ------------------------------ Ploteos PSD

for snr in snrs:
    for nombre_vent in ventanas.keys():
        fig, ax = plt.subplots(1, 1, figsize=(10, 6),layout="constrained")

        # --- Subplot 0: Espectro de Magnitud ---
        ax.plot(frec,X_db, linewidth=1.2)
        ax.set_xlim([240,260])
        ax.set_ylim(-60)
        ax.set_title("Espectro de potencia normalizado", fontsize=11, fontweight='bold')
        ax.set_ylabel("Potencia [dB]", fontsize=10)
        ax.set_xlabel("Frecuencia [Hz]")
        ax.grid(True, which='both', linestyle=':', alpha=0.5)
        ax.minorticks_on()

        fig2, ax = plt.subplots(1, 1, figsize=(10, 6),layout="constrained")

        # --- Subplot 0: Espectro de Magnitud ---
        ax.plot(frec,X_V_db, linewidth=1.2)
        ax.set_xlim([240,260])
        ax.set_ylim(-60)
        ax.set_title("Espectro de potencia normalizado", fontsize=11, fontweight='bold')
        ax.set_ylabel("Potencia [dB]", fontsize=10)
        ax.set_xlabel("Frecuencia [Hz]")
        ax.grid(True, which='both', linestyle=':', alpha=0.5)
        ax.minorticks_on()
