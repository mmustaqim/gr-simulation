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

    # Build the filter(s)
    M = 4
    bw = 1.0/2.0
    tb = 1.0/5.0
    taps_firdes = filter.firdes.low_pass_2(M, M, bw, tb, 80,
                                           filter.firdes.WIN_BLACKMAN_hARRIS)

    bw1 = bw-0.125
    tb1 = tb + 0.105
    print bw1, tb1
    taps_optfir = filter.optfir.low_pass(M, M, bw1, bw1+tb1, 0.1, 80)
    print "ntaps (firdes): ", len(taps_firdes), len(taps_firdes)/M
    print "ntaps (optfir): ", len(taps_optfir), len(taps_optfir)/M

    nfft = 10000

    # Set axes (and other default) fonts
    font = {'size': 18}
    matplotlib.rc('font', **font)

    # Plot original prototype filter used in the channelizer
    fig = plt.figure(1, figsize=(20,12), facecolor='w')
    sp0 = fig.add_subplot(1,1,1)
    sp0.set_title("Comparing firdes and optfir LPF",
                  fontweight='bold', fontsize=20)

    H_firdes = 20.0*scipy.log10(abs(fftpack.fftshift(fftpack.fft(taps_firdes, nfft))))
    H_optfir = 20.0*scipy.log10(abs(fftpack.fftshift(fftpack.fft(taps_optfir, nfft))))
    freq = scipy.linspace(-fs/2, fs/2, nfft)

    sp0.plot(freq, H_firdes, "b-", linewidth=3, alpha=0.75, label="firdes")
    sp0.plot(freq, H_optfir, "r-", linewidth=3, alpha=0.75, label="optfir")
    sp0.grid()
    sp0.set_xlim([-fs/2, fs/2])
    sp0.set_ylim([-160, 40])
    sp0.set_xlabel("Frequency (kHz)", fontsize=18, fontweight='bold')
    sp0.set_ylabel("Magnitude (dB)", fontsize=18, fontweight='bold')
    sp0.legend()

    fig.tight_layout()

    fig.savefig("lpf_firdes_optfir_comp.png",
                dpi=80, format='png',
                facecolor='w', edgecolor='w')

    plt.show()

if __name__ == "__main__":
    main()
