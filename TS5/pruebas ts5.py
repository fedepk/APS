# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 10:22:10 2026

@author: Fede
"""
import sys
from pathlib import Path
directorio_padre = str(Path.cwd().parent)
sys.path.insert(0, directorio_padre)
import gen_fun as gen
import numpy as np
from scipy import signal as sig
import scipy.io as sio
from scipy.io.wavfile import write

import matplotlib.pyplot as plt
   
# import scipy.io as sio
# from scipy.io.wavfile import write

#%% --------------------------------- Definiciones
fs_ecg = 1000 # Hz


#%% ------------------------- Programa

ecg_one_lead = np.load('ecg_sin_ruido.npy')
len_ecg = len(ecg_one_lead)
combinaciones = [
    (len_ecg/6),
    (len_ecg/12),
    (len_ecg/30),
    (len_ecg/37.5)
]

plt.close()

#%% ------------------------------ Ploteos PSD

fig, axs = plt.subplots(2, 2, figsize=(12, 8))

for ax, (nperseg) in zip(axs.ravel(), combinaciones):

    f_ecg, psd_ecg = sig.welch(
        ecg_one_lead,
        fs=fs_ecg,
        nperseg=nperseg,
        noverlap=nperseg//2,
        detrend='linear'
    )
    bw = gen.bw(f_ecg,psd_ecg,0.98) 

    ax.plot(f_ecg, psd_ecg , label='Señal ECG')
    ax.axvline(x=bw, linestyle='--', color='red', label = f'Bw = {bw} Hz')
    ax.set_title(f'Long. de segmento = {nperseg}, Overlap = 50%')
    ax.set_xlabel('Frecuencia [Hz]')
    ax.set_ylabel('PSD [Muestras²/Hz]')
    ax.ticklabel_format(axis='y', style='sci', scilimits=(0, 0))
    ax.set_xlim(0, 40)
    ax.grid(True, which='both', linestyle=':', alpha=0.5)
    ax.minorticks_on()
    ax.legend()

plt.suptitle('Análisis espectral del ECG mediante método de Welch')
plt.tight_layout()
plt.show()


fs_audio, wav_data = sio.wavfile.read('la cucaracha.wav')

len_wav = len(wav_data)

print(len_wav)
print(fs_audio)