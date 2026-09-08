# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 14:26:13 2026

@author: Fede
"""

import gen_fun as gen

#%% definiciones

N = 1000
fs = 1000
f = 60

tt,xx = gen.senoidal(vmax = 2,ff = f)

gen.graficar_amplitud(tt, xx,fs,f,zoom =60)

gen.espectro(xx, tt, N, fs)