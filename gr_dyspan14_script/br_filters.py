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

    # Build the filter(s)
    fl = 10e3  # Bandwidth of the channel
    fh = 20e3
    tb = 2.5e3
    taps_bh = filter.firdes.band_reject_2(1, fs,
                                        fl, fh, tb, 80,
                                        filter.firdes.WIN_BLACKMAN_hARRIS)
    taps_ham = filter.firdes.band_reject_2(1, fs,
                                         fl, fh, tb, 80,
                                         filter.firdes.WIN_HAMMING)
    taps_hann = filter.firdes.band_reject_2(1, fs,
                                          fl, fh, tb, 80,
                                          filter.firdes.WIN_HANN)

    nfft = 10000

    # Set axes (and other default) fonts
    font = {'size': 18}
    matplotlib.rc('font', **font)

    # Plot original prototype filter used in the channelizer
    fig = plt.figure(1, figsize=(20,12), facecolor='w')
    sp0 = fig.add_subplot(2,1,1)
    sp1 = fig.add_subplot(2,1,2)
    sp0.set_title("firdes.band_reject_2(gain, fs, f_low, f_hi, tb, atten, window)",
                  fontweight='bold', fontsize=20)

    H_bh = 20.0*scipy.log10(abs(fftpack.fftshift(fftpack.fft(taps_bh, nfft))))
    H_ham = 20.0*scipy.log10(abs(fftpack.fftshift(fftpack.fft(taps_ham, nfft))))
    H_hann = 20.0*scipy.log10(abs(fftpack.fftshift(fftpack.fft(taps_hann, nfft))))
    freq = scipy.linspace(-fs/2, fs/2, nfft)

    sp0.plot(freq, H_bh, "b-", linewidth=3, alpha=0.75, label="Blackman-harris")
    sp0.plot(freq, H_ham, "r-", linewidth=3, alpha=0.75, label="Hamming")
    sp0.plot(freq, H_hann, "m-", linewidth=3, alpha=0.75, label="Hann")
    sp0.grid()
    sp0.set_xlim([-fs/2, fs/2])
    sp0.set_ylim([-160, 40])
    sp0.set_xlabel("Frequency (kHz)", fontsize=18, fontweight='bold')
    sp0.set_ylabel("Magnitude (dB)", fontsize=18, fontweight='bold')
    sp0.legend(loc='lower right')

    a = plt.axes([0.12, 0.58, 0.15, 0.15], axisbg='w')
    a.plot(freq, H_bh, "b-", linewidth=3)
    a.plot(freq, H_ham, "r-", linewidth=3)
    a.plot(freq, H_hann, "m-", linewidth=3)
    a.set_xlim([-10e3, 10e3])
    a.set_ylim([-0.75e-1, 0.75e-1])
    a.set_yticks([-0.75e-1, 0.75e-1])
    a.set_xticks([-10e3, 10e3])
    a.ticklabel_format(style='sci', axis='y', scilimits=(0,0))

    sp1.plot(taps_bh, "b-o", linewidth=3, alpha=0.5, label="Blackman-harris")
    sp1.plot(taps_ham, "r-o", linewidth=3, alpha=0.5, label="Hamming")
    sp1.plot(taps_hann, "m-o", linewidth=3, alpha=0.5, label="Hann")
    sp1.grid()
    sp1.set_xlabel("Tap Number", fontsize=18, fontweight='bold')
    sp1.set_ylabel("Amplitude", fontsize=18, fontweight='bold')

    fig.tight_layout()

    fig.savefig("br_filters.png",
                dpi=80, format='png',
                facecolor='w', edgecolor='w')

    plt.show()

if __name__ == "__main__":
    main()
