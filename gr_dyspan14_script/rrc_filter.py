#!/usr/bin/env python
# Copyright Rondeau Research, 2014

from gnuradio import gr, digital, analog
from gnuradio import filter
from gnuradio import blocks
import sys

import scipy
from scipy import fftpack
from matplotlib import pyplot as plt
import matplotlib

def main():
    N = 10000
    fs = 100e3
    Ts = 1.0/fs
    t = scipy.arange(0, N*Ts, Ts)

    taps = filter.firdes.root_raised_cosine(1, fs, fs/4, 0.22, 101)

    nfft = 10000

    # Set axes (and other default) fonts
    font = {'size': 18}
    matplotlib.rc('font', **font)

    # Plot original prototype filter used in the channelizer
    fig = plt.figure(1, figsize=(20,12), facecolor='w')
    sp0 = fig.add_subplot(2,1,1)
    sp1 = fig.add_subplot(2,1,2)
    sp0.set_title("firdes.root_raised_cosine(gain, fs, symbol rate, alpha, ntaps)",
                  fontweight='bold', fontsize=20)

    H = 20.0*scipy.log10(abs(fftpack.fftshift(fftpack.fft(taps, nfft))))
    freq = scipy.linspace(-fs/2, fs/2, nfft)

    sp0.plot(freq, H, "b-", linewidth=3, alpha=0.75)
    sp0.grid()
    sp0.set_xlim([-fs/2, fs/2])
    sp0.set_ylim([-160, 40])
    sp0.set_xlabel("Frequency (kHz)", fontsize=18, fontweight='bold')
    sp0.set_ylabel("Magnitude (dB)", fontsize=18, fontweight='bold')

    a = plt.axes([0.12, 0.78, 0.15, 0.15], axisbg='w')
    a.plot(freq, H, "b-", linewidth=3)
    a.set_xlim([-12.5e3, 12.5e3])
    a.set_ylim([-0.75e-1, 0.75e-1])
    a.set_yticks([-0.75e-1, 0.75e-1])
    a.set_xticks([-12.5e3, 12.5e3])
    a.ticklabel_format(style='sci', axis='y', scilimits=(0,0))

    sp1.plot(taps, "b-o", linewidth=3, alpha=0.5, label="Blackman-harris")
    sp1.grid()
    sp1.set_xlabel("Tap Number", fontsize=18, fontweight='bold')
    sp1.set_ylabel("Amplitude", fontsize=18, fontweight='bold')

    fig.tight_layout()

    fig.savefig("rrc_filter.png",
                dpi=80, format='png',
                facecolor='w', edgecolor='w')

    plt.show()

if __name__ == "__main__":
    main()
