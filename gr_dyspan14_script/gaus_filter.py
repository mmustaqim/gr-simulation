#!/usr/bin/env python
# Copyright Rondeau Research, 2014

from gnuradio import filter
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

    taps = filter.firdes.gaussian(1, 20, .35, 101)

    nfft = 10000

    # Set axes (and other default) fonts
    font = {'size': 18}
    matplotlib.rc('font', **font)

    # Plot original prototype filter used in the channelizer
    fig = plt.figure(1, figsize=(20,12), facecolor='w')
    sp0 = fig.add_subplot(2,1,1)
    sp1 = fig.add_subplot(2,1,2)
    sp0.set_title("firdes.gaussian(gain, spb, bt, ntaps)",
                  fontweight='bold', fontsize=20)

    H = 20.0*scipy.log10(abs(fftpack.fftshift(fftpack.fft(taps, nfft))))
    freq = scipy.linspace(-fs/2, fs/2, nfft)

    sp0.plot(freq, H, "b-", linewidth=3, alpha=0.75)
    sp0.grid()
    sp0.set_xlim([-fs/2, fs/2])
    sp0.set_ylim([-200, 40])
    sp0.set_xlabel("Frequency (kHz)", fontsize=18, fontweight='bold')
    sp0.set_ylabel("Magnitude (dB)", fontsize=18, fontweight='bold')

    sp1.plot(taps, "b-o", linewidth=3, alpha=0.5, label="Blackman-harris")
    sp1.grid()
    sp1.set_xlabel("Tap Number", fontsize=18, fontweight='bold')
    sp1.set_ylabel("Amplitude", fontsize=18, fontweight='bold')

    fig.tight_layout()

    fig.savefig("gaussian.png",
                dpi=80, format='png',
                facecolor='w', edgecolor='w')

    plt.show()

if __name__ == "__main__":
    main()
