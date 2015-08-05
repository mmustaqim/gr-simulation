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

    # When playing with the number of channels, be careful about the filter
    # specs and the channel map of the synthesizer set below.
    nchans = 10

    # Build the filter(s)
    bw = fs/2  # Bandwidth of the channel
    tb = 20e3
    proto_taps = filter.firdes.low_pass_2(1, nchans*fs,
                                          bw, tb, 80,
                                          filter.firdes.WIN_BLACKMAN_hARRIS)
    proto_taps = list(proto_taps)
    proto_taps = proto_taps
    syn_taps = [((nchans)/2)*t for t in proto_taps]

    tpc = int(scipy.ceil(len(proto_taps)/float(nchans)))
    print "Filter length: ", len(proto_taps)
    print "Taps/Channel: {0} ({1})".format(tpc, len(proto_taps)/float(nchans))
    print "Taps/Channel: {0} ({1})".format(tpc, len(syn_taps)/float(nchans))

    channelizer = filter.pfb.channelizer_ccf(nchans, proto_taps, 2)
    synthesizer = filter.pfb_synthesizer_ccf(nchans, syn_taps, True)
    ch_taps = channelizer.taps()
    sy_taps = synthesizer.taps()

    # Set the synthesizer map. The numbers are the output channel
    # locations and the indices are the input channel numbers.
    #synthesizer.set_channel_map([4, 8, 10, 0, 2, 6])

    nfft = 10000

    sig = blocks.vector_source_c(10*[0,] + [1,] + (nfft-11)*[0,], False)
    noise = analog.noise_source_c(analog.GR_GAUSSIAN, 0.000)
    src = blocks.add_cc()
    snk = blocks.vector_sink_c()

    tb = gr.top_block()
    tb.connect(sig, (src,0))
    tb.connect(noise, (src,1))
    tb.connect(src, channelizer)
    tb.connect(synthesizer, snk)

    snks = []
    for i in xrange(nchans):
        snks.append(blocks.vector_sink_c())
        tb.connect((channelizer,i), snks[i])
        tb.connect((channelizer,i), (synthesizer,i))
    tb.run()

    # Set axes (and other default) fonts
    font = {'size': 18}
    matplotlib.rc('font', **font)

    # Plot original prototype filter used in the channelizer
    #fig1 = plt.figure(1, figsize=(12,10), facecolor='w')
    #sp11 = fig1.add_subplot(1,1,1)
    #H = 20.0*scipy.log10(abs(fftpack.fftshift(fftpack.fft(proto_taps, nfft))))
    #freq = scipy.linspace(-nchans*fs/2, fs*nchans/2, nfft)
    #sp11.plot(freq, H, linewidth=3)
    #sp11.grid()
    #sp11.set_xlim([-nchans*fs/2, fs*nchans/2])
    #sp11.set_ylim([-160, 20])
    #sp11.set_xlabel("Frequency (kHz)", fontsize=18, fontweight='bold')
    #sp11.set_ylabel("Magnitude (dB)", fontsize=18, fontweight='bold')
    #sp11.set_xticks([-nchans*fs/2, -nchans*fs/4, 0, nchans*fs/4, fs*nchans/2])
    #sp11.set_xticklabels([-nchans*fs/2/1000, -nchans*fs/4/1000, 0, nchans*fs/4/1000, fs*nchans/2/1000])

    #a = plt.axes([0.125, 0.725, 0.2, 0.2], axisbg='w')
    #a.plot(freq, H, linewidth=3)
    #a.set_xlim([-fs, fs])
    #a.set_ylim([-1e-4, 2e-4])
    #a.set_yticks([-1e-4, 2e-4])
    #a.set_xticks([-fs/2, fs/2])
    #a.ticklabel_format(style='sci', axis='y', scilimits=(0,0))

    # Plot the results. We will plot each channelizer output on one
    # subfigure and the output of each synthesis filterbank in two
    # other subfigures so that we can properly represent the frequency
    # domain or each.
    fig2 = plt.figure(2, figsize=(12,10), facecolor='w')
    data = []
    sp21 = fig2.add_subplot(2,1,1)
    sp22 = fig2.add_subplot(2,1,2)
    for i in xrange(nchans):
        data.append(scipy.array(snks[i].data()))

        X = 10.0*scipy.log10(abs(fftpack.fftshift(fftpack.fft(data[0], nfft))))

        freq = scipy.linspace(-2*fs/2, 2*fs/2, nfft)

        if(i == nchans/2):
            f0 = scipy.linspace(fs*(nchans/2 - 1), fs*(nchans/2), nfft/2)
            f1 = scipy.linspace(-fs*(nchans/2), -fs*(nchans/2 - 1), nfft/2)
            p = sp21.plot(f0, X[0:nfft/2], linewidth=2)
            sp21.plot(f1, X[nfft/2:nfft], color=p[0].get_color(), linewidth=2)
        else:
            x = i
            if(x > nchans/2):
                x -= nchans
            f0 = scipy.linspace(-fs, fs, nfft)
            f0 = f0 + x*fs
            sp21.plot(f0, X, linewidth=2)

    data_s = scipy.array(snk.data())
    Y = 10.0*scipy.log10(abs(fftpack.fftshift(fftpack.fft(data_s, nfft))))
    freq = scipy.linspace(-2*nchans*fs/2, 2*fs*nchans/2, nfft)
    sp22.plot(freq, Y, linewidth=3)
    sp21.grid()
    sp22.grid()
    sp21.set_xlim([-nchans*fs/2, fs*nchans/2])
    sp22.set_xlim([-2*nchans*fs/2, 2*fs*nchans/2])

    sp21.set_xticks([-nchans*fs/2, -nchans*fs/4, 0, nchans*fs/4, fs*nchans/2])
    sp21.set_xticklabels([-nchans*fs/2/1000, -nchans*fs/4/1000, 0, nchans*fs/4/1000, fs*nchans/2/1000])
    sp22.set_xticks([-2*nchans*fs/2, -2*nchans*fs/4, 0,
                      2*fs*nchans/4, 2*fs*nchans/2])
    sp22.set_xticklabels([-2*nchans*fs/2/1000, -2*nchans*fs/4/1000, 0,
                           2*fs*nchans/4/1000, 2*fs*nchans/2/1000])

    #a = plt.axes([0.125, 0.25, 0.2, 0.2], axisbg='w')
    #a.plot(freq, Y, linewidth=3)
    #a.set_xlim([-fs, nchans*fs])
    #a.set_ylim([-1e-4, 2e-4])
    #a.set_yticks([-1e-4, 2e-4])
    #a.set_xticks([-fs/2, nchans*fs])
    #a.set_xticklabels([-fs/2/1000, (nchans*fs)/1000])
    #a.ticklabel_format(style='sci', axis='y', scilimits=(0,0))

    sp21.set_xlabel("Frequency (kHz)", fontsize=18, fontweight='bold')
    sp21.set_ylabel("Magnitude (dB)", fontsize=18, fontweight='bold')
    sp22.set_xlabel("Frequency (kHz)", fontsize=18, fontweight='bold')
    sp22.set_ylabel("Magnitude (dB)", fontsize=18, fontweight='bold')

    #fig1.tight_layout()
    fig2.tight_layout()

    #fig1.savefig("impulse_prototype_filter.png",
    #             dpi=300, format='png',
    #             facecolor='w', edgecolor='w')
    #
    #fig2.savefig("impulse_chan_and_synth.png",
    #             dpi=300, format='png',
    #             facecolor='w', edgecolor='w')


    plt.show()

if __name__ == "__main__":
    main()
