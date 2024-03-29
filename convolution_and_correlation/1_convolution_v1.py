# -*- coding: utf-8 -*-
"""
Created on Tue May  2 02:22:03 2023

@author: yesed
"""

from matplotlib import style
import mysignals as sigs
from matplotlib import pyplot as plt
from scipy import signal

output_signal = signal.convolve(sigs.InputSignal_1kHz_15kHz,sigs.Impulse_response, mode  = "same")

style.use("dark_background")

f, plt_arr = plt.subplots(3, sharex=True)
f.suptitle("Convolution")
plt_arr[0].plot(sigs.InputSignal_1kHz_15kHz, color="red")
plt_arr[0].set_title("Input Signal")
plt_arr[1].plot(sigs.Impulse_response, color="pink")
plt_arr[1].set_title("Impulse Signal")
plt_arr[2].plot(output_signal, color="magenta")
plt_arr[2].set_title("Output Signal")
plt.show()