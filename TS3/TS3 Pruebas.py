import sys
from pathlib import Path
directorio_padre = str(Path.cwd().parent)
sys.path.insert(0, directorio_padre)
import gen_fun as gen
import numpy as np
import matplotlib.pyplot as plt


#%%   ------------------ Definiciones

N = 1000
fs = 1000
Vfs = 2
k0 = N/4
muestras_tiempo = 10 
factor = 10


#%%   ------------------- Genero funciones 

f0 = (k0)*fs/N
tt , xx0 = gen.senoidal(pot=1,ff=f0,fs=fs,nn =N )

f1=(k0+0.25)*fs/N
_ , xx1 = gen.senoidal(pot=1,ff=f1,fs=fs,nn =N )

f2=(k0+0.5)*fs/N
_ , xx2 = gen.senoidal(pot=1,ff=f2,fs=fs,nn =N )



#%% ------------------- Transformadas

df = fs/N
#%% ------------------- Padeo con 0

xx0 ,tt =gen.zero_padding(xx0)
xx1 ,_ =gen.zero_padding(xx1)
xx2 ,_ =gen.zero_padding(xx2)

N2 = N*factor
frec = np.arange(int(N2 / 2)) * (fs / N2)
X0 = 1/N * np.fft.fft(xx0)         # FFT normalizada
p_X0 = np.abs(X0)**2               # Paso a potencia 
p_X0[1:] = p_X0[1:] * 2            # Multiplico por 2 excepto la primer muestra (nivel de dc)
p_X0 = p_X0 / df                   # Calculo densidad de potencia espectral
X0_db = 10 * np.log10(p_X0)        # Paso a db

X1 = 1/N * np.fft.fft(xx1)
p_X1 = np.abs(X1)**2
p_X1[1:] = p_X1[1:] * 2
p_X1 = p_X1 / df
X1_db = 10 * np.log10(p_X1)

X2 = 1/N * np.fft.fft(xx2)
p_X2 = np.abs(X2)**2
p_X2[1:] = p_X2[1:] * 2
p_X2 = p_X2 / df
X2_db = 10 * np.log10(p_X2)


pot_frec = sum((np.abs(X0)**2))/factor
print(pot_frec)

pot_frec = sum((np.abs(X1)**2))/factor
print(pot_frec)

pot_frec = sum((np.abs(X2)**2))/factor
print(pot_frec)

# frec = tt * (fs / N)
# frec = frec[:(N // 2)]

tt = tt /fs * 1000   # Tiempo en ms

#%%  Ploteos
# =====================================================================

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))

# # Subplot 1: Señales de amplitud en el tiempo
sen1, = ax1.plot(frec, X0_db[:(N2 // 2)])
sen2, = ax1.plot(frec, X1_db[:(N2 // 2)])
sen3, = ax1.plot(frec, X2_db[:(N2 // 2)])
lineas = [sen1, sen2, sen3]
etiquetas_k = [r'$k_0 = \frac{N}{4}$', r'$k_0 = \frac{N}{4}+0,25$', r'$k_0 = \frac{N}{4}+0,5$']
leyenda_derecha = ax1.legend(lineas, etiquetas_k, loc='upper right')
ax1.add_artist(leyenda_derecha) 
etiquetas_pot = [rf'$Potencia = {pot_frec:.2f}W$', rf'$Potencia = {pot_frec:.2f}W$', rf'$Potencia = {pot_frec:.2f}W$']
ax1.legend(lineas, etiquetas_pot, loc='upper left')
ax1.set_title(r'Densidad Espectral de Potencia para: sen($f_0$), $f_0 = k_0 \cdot \Delta f, f_0 = 250Hz$')
ax1.set_xlabel('Frecuencia [Hz]')
ax1.set_ylabel('Densidad de potencia [dB/Hz]')
ax1.set_ylim(-120)
ax1.grid(True)

# Subplot 2: Espectros de potencia en frecuencia
ax2.plot(frec, X0_db[:(N2 // 2)], label=r'$k_0 = \frac{N}{4}$')
ax2.plot(frec, X1_db[:(N2 // 2)], label=r'$k_0 = \frac{N}{4}+0,25$')
ax2.plot(frec, X2_db[:(N2 // 2)], label=r'$k_0 = \frac{N}{4}+0,5$')
ax2.set_title(r'Densidad Espectral de Potencia (magnificado)')
ax2.set_xlabel('Frecuencia [Hz]')
ax2.set_ylabel('Densidad de potencia [dB/Hz]')
ax2.set_ylim(-50)
ax2.set_xlim([240,260])
ax2.grid(True)
ax2.legend()
plt.tight_layout()
plt.show()


