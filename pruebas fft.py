# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 08:40:00 2026

@author: Fede
"""
import numpy as np
import matplotlib.pyplot as plt
import gen_fun as gen


tt,xx= gen.senoidal(ff=4)
x = np.fft.fft(xx)
plt.figure()
plt.plot(tt,np.imag(x))
plt.grid()
plt.title("Senoidal")


tt,xx = gen.snr(ff=20,snr = 10)
x = np.fft.fft(xx)
plt.figure()
plt.plot(tt,np.imag(x))
plt.grid()
plt.title("Senoidal con ruido")