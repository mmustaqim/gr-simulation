#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Fm Reconstruction
# Generated: Thu Jun  5 04:13:47 2014
##################################################

from PyQt4 import Qt
from PyQt4.QtCore import QObject, pyqtSlot
from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.filter import pfb
from optparse import OptionParser
import PyQt4.Qwt5 as Qwt
import sip
import sys
import time

class fm_reconstruction(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Fm Reconstruction")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Fm Reconstruction")
        try:
             self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
             pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "fm_reconstruction")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.synth_channels = synth_channels = 6
        self.channels = channels = 10
        self.ch_rate = ch_rate = 100e3
        self.samp_rate = samp_rate = ch_rate*channels
        self.gain = gain = 40
        self.fm_quad_rate = fm_quad_rate = ch_rate*synth_channels
        self.ch_tb = ch_tb = 20e3
        self.ch_bw = ch_bw = ch_rate/2
        self.center_freq = center_freq = 100.1e6
        self.audio_rate = audio_rate = 60e3
        self.atten = atten = 80
        self.volume = volume = 0.1
        self.tun_gain = tun_gain = gain
        self.tun_freq = tun_freq = center_freq
        self.pfb_taps = pfb_taps = firdes.low_pass_2(1, samp_rate, ch_bw, ch_tb, atten, firdes.WIN_BLACKMAN_HARRIS)
        self.pfb_synth_taps = pfb_synth_taps = firdes.low_pass_2(channels/2, synth_channels*ch_rate, ch_bw, ch_tb, atten, firdes.WIN_BLACKMAN_HARRIS)
        self.fm_audio_decim = fm_audio_decim = int(fm_quad_rate/audio_rate)*2
        self.channel = channel = 0
        self.address = address = ""

        ##################################################
        # Blocks
        ##################################################
        self._volume_layout = Qt.QVBoxLayout()
        self._volume_tool_bar = Qt.QToolBar(self)
        self._volume_layout.addWidget(self._volume_tool_bar)
        self._volume_tool_bar.addWidget(Qt.QLabel("Volume"+": "))
        class qwt_counter_pyslot(Qwt.QwtCounter):
            def __init__(self, parent=None):
                Qwt.QwtCounter.__init__(self, parent)
            @pyqtSlot('double')
            def setValue(self, value):
                super(Qwt.QwtCounter, self).setValue(value)
        self._volume_counter = qwt_counter_pyslot()
        self._volume_counter.setRange(0, 10, 0.1)
        self._volume_counter.setNumButtons(2)
        self._volume_counter.setValue(self.volume)
        self._volume_tool_bar.addWidget(self._volume_counter)
        self._volume_counter.valueChanged.connect(self.set_volume)
        self._volume_slider = Qwt.QwtSlider(None, Qt.Qt.Horizontal, Qwt.QwtSlider.BottomScale, Qwt.QwtSlider.BgSlot)
        self._volume_slider.setRange(0, 10, 0.1)
        self._volume_slider.setValue(self.volume)
        self._volume_slider.setMinimumWidth(200)
        self._volume_slider.valueChanged.connect(self.set_volume)
        self._volume_layout.addWidget(self._volume_slider)
        self.top_grid_layout.addLayout(self._volume_layout, 3,0,1,1)
        self._tun_gain_layout = Qt.QVBoxLayout()
        self._tun_gain_tool_bar = Qt.QToolBar(self)
        self._tun_gain_layout.addWidget(self._tun_gain_tool_bar)
        self._tun_gain_tool_bar.addWidget(Qt.QLabel("Gain (dB)"+": "))
        class qwt_counter_pyslot(Qwt.QwtCounter):
            def __init__(self, parent=None):
                Qwt.QwtCounter.__init__(self, parent)
            @pyqtSlot('double')
            def setValue(self, value):
                super(Qwt.QwtCounter, self).setValue(value)
        self._tun_gain_counter = qwt_counter_pyslot()
        self._tun_gain_counter.setRange(0, 70, 1)
        self._tun_gain_counter.setNumButtons(2)
        self._tun_gain_counter.setValue(self.tun_gain)
        self._tun_gain_tool_bar.addWidget(self._tun_gain_counter)
        self._tun_gain_counter.valueChanged.connect(self.set_tun_gain)
        self._tun_gain_slider = Qwt.QwtSlider(None, Qt.Qt.Horizontal, Qwt.QwtSlider.BottomScale, Qwt.QwtSlider.BgSlot)
        self._tun_gain_slider.setRange(0, 70, 1)
        self._tun_gain_slider.setValue(self.tun_gain)
        self._tun_gain_slider.setMinimumWidth(200)
        self._tun_gain_slider.valueChanged.connect(self.set_tun_gain)
        self._tun_gain_layout.addWidget(self._tun_gain_slider)
        self.top_grid_layout.addLayout(self._tun_gain_layout, 2,1,1,1)
        self._tun_freq_layout = Qt.QVBoxLayout()
        self._tun_freq_tool_bar = Qt.QToolBar(self)
        self._tun_freq_layout.addWidget(self._tun_freq_tool_bar)
        self._tun_freq_tool_bar.addWidget(Qt.QLabel("Frequency"+": "))
        class qwt_counter_pyslot(Qwt.QwtCounter):
            def __init__(self, parent=None):
                Qwt.QwtCounter.__init__(self, parent)
            @pyqtSlot('double')
            def setValue(self, value):
                super(Qwt.QwtCounter, self).setValue(value)
        self._tun_freq_counter = qwt_counter_pyslot()
        self._tun_freq_counter.setRange(center_freq - 1e6, center_freq + 1e6, 100e3)
        self._tun_freq_counter.setNumButtons(2)
        self._tun_freq_counter.setValue(self.tun_freq)
        self._tun_freq_tool_bar.addWidget(self._tun_freq_counter)
        self._tun_freq_counter.valueChanged.connect(self.set_tun_freq)
        self._tun_freq_slider = Qwt.QwtSlider(None, Qt.Qt.Horizontal, Qwt.QwtSlider.BottomScale, Qwt.QwtSlider.BgSlot)
        self._tun_freq_slider.setRange(center_freq - 1e6, center_freq + 1e6, 100e3)
        self._tun_freq_slider.setValue(self.tun_freq)
        self._tun_freq_slider.setMinimumWidth(200)
        self._tun_freq_slider.valueChanged.connect(self.set_tun_freq)
        self._tun_freq_layout.addWidget(self._tun_freq_slider)
        self.top_grid_layout.addLayout(self._tun_freq_layout, 3,1,1,1)
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	device_addr=address,
        	stream_args=uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_0.set_time_now(uhd.time_spec(time.time()), uhd.ALL_MBOARDS)
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_center_freq(tun_freq, 0)
        self.uhd_usrp_source_0.set_gain(tun_gain, 0)
        self.uhd_usrp_source_0.set_antenna("TX/RX", 0)
        self.qtgui_freq_sink_x_0_0_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_FLATTOP, #wintype
        	0, #fc
        	ch_rate*synth_channels, #bw
        	"QT GUI Plot", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0_0_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_0_0.set_y_axis(-140, 10)
        self._qtgui_freq_sink_x_0_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_0_0_win, 1,1,1,1)
        self.qtgui_freq_sink_x_0_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_FLATTOP, #wintype
        	0, #fc
        	ch_rate*2, #bw
        	"QT GUI Plot", #name
        	synth_channels #number of inputs
        )
        self.qtgui_freq_sink_x_0_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_0.set_y_axis(-80, 0)
        self._qtgui_freq_sink_x_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_0_win, 1,0,1,1)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	tun_freq, #fc
        	samp_rate, #bw
        	"QT GUI Plot", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-80, 10)
        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_win, 0,0,1,2)
        self.pfb_synthesizer_ccf_0 = filter.pfb_synthesizer_ccf(
        	  synth_channels, (pfb_synth_taps), True)
        self.pfb_synthesizer_ccf_0.set_channel_map(([10, 11, 0, 1, 2, 3]))
        	
        self.pfb_channelizer_ccf_0 = pfb.channelizer_ccf(
        	  channels,
        	  (pfb_taps),
        	  2.0,
        	  atten)
        self.pfb_channelizer_ccf_0.set_channel_map(())
        	
        self.pfb_arb_resampler_xxx_0 = pfb.arb_resampler_fff(
        	  44.1e3/(fm_quad_rate/fm_audio_decim),
                  taps=None,
        	  flt_size=32)
        	
        self.fir_filter_xxx_0 = filter.fir_filter_ccc(2, (firdes.low_pass_2(1, ch_rate*synth_channels, 250e3, 300e3, 40, firdes.WIN_BLACKMAN_HARRIS) ))
        self.fir_filter_xxx_0.declare_sample_delay(0)
        self._channel_layout = Qt.QVBoxLayout()
        self._channel_tool_bar = Qt.QToolBar(self)
        self._channel_layout.addWidget(self._channel_tool_bar)
        self._channel_tool_bar.addWidget(Qt.QLabel("Output Channel"+": "))
        class qwt_counter_pyslot(Qwt.QwtCounter):
            def __init__(self, parent=None):
                Qwt.QwtCounter.__init__(self, parent)
            @pyqtSlot('double')
            def setValue(self, value):
                super(Qwt.QwtCounter, self).setValue(value)
        self._channel_counter = qwt_counter_pyslot()
        self._channel_counter.setRange(0, channels-1, 1)
        self._channel_counter.setNumButtons(2)
        self._channel_counter.setValue(self.channel)
        self._channel_tool_bar.addWidget(self._channel_counter)
        self._channel_counter.valueChanged.connect(self.set_channel)
        self._channel_slider = Qwt.QwtSlider(None, Qt.Qt.Horizontal, Qwt.QwtSlider.BottomScale, Qwt.QwtSlider.BgSlot)
        self._channel_slider.setRange(0, channels-1, 1)
        self._channel_slider.setValue(self.channel)
        self._channel_slider.setMinimumWidth(200)
        self._channel_slider.valueChanged.connect(self.set_channel)
        self._channel_layout.addWidget(self._channel_slider)
        self.top_grid_layout.addLayout(self._channel_layout, 2,0,1,1)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_multiply_const_vxx = blocks.multiply_const_vff((volume, ))
        self.audio_sink = audio.sink(44100, "", True)
        self.analog_wfm_rcv = analog.wfm_rcv(
        	quad_rate=fm_quad_rate,
        	audio_decimation=fm_audio_decim,
        )
        self.analog_agc2_xx_0 = analog.agc2_cc(1e-1, 1e-2, 1.0, 1.0)
        self.analog_agc2_xx_0.set_max_gain(65536)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.uhd_usrp_source_0, 0), (self.analog_agc2_xx_0, 0))
        self.connect((self.analog_agc2_xx_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.analog_agc2_xx_0, 0), (self.pfb_channelizer_ccf_0, 0))
        self.connect((self.fir_filter_xxx_0, 0), (self.qtgui_freq_sink_x_0_0_0, 0))
        self.connect((self.fir_filter_xxx_0, 0), (self.analog_wfm_rcv, 0))
        self.connect((self.pfb_arb_resampler_xxx_0, 0), (self.blocks_multiply_const_vxx, 0))
        self.connect((self.blocks_multiply_const_vxx, 0), (self.audio_sink, 0))
        self.connect((self.analog_wfm_rcv, 0), (self.pfb_arb_resampler_xxx_0, 0))
        self.connect((self.pfb_synthesizer_ccf_0, 0), (self.fir_filter_xxx_0, 0))
        self.connect((self.pfb_channelizer_ccf_0, 0), (self.pfb_synthesizer_ccf_0, 0))
        self.connect((self.pfb_channelizer_ccf_0, 1), (self.pfb_synthesizer_ccf_0, 1))
        self.connect((self.pfb_channelizer_ccf_0, 2), (self.pfb_synthesizer_ccf_0, 2))
        self.connect((self.pfb_channelizer_ccf_0, 3), (self.pfb_synthesizer_ccf_0, 3))
        self.connect((self.pfb_channelizer_ccf_0, 4), (self.pfb_synthesizer_ccf_0, 4))
        self.connect((self.pfb_channelizer_ccf_0, 5), (self.pfb_synthesizer_ccf_0, 5))
        self.connect((self.pfb_channelizer_ccf_0, 0), (self.qtgui_freq_sink_x_0_0, 0))
        self.connect((self.pfb_channelizer_ccf_0, 1), (self.qtgui_freq_sink_x_0_0, 1))
        self.connect((self.pfb_channelizer_ccf_0, 2), (self.qtgui_freq_sink_x_0_0, 2))
        self.connect((self.pfb_channelizer_ccf_0, 3), (self.qtgui_freq_sink_x_0_0, 3))
        self.connect((self.pfb_channelizer_ccf_0, 4), (self.qtgui_freq_sink_x_0_0, 4))
        self.connect((self.pfb_channelizer_ccf_0, 5), (self.qtgui_freq_sink_x_0_0, 5))
        self.connect((self.pfb_channelizer_ccf_0, 6), (self.blocks_null_sink_0, 0))
        self.connect((self.pfb_channelizer_ccf_0, 7), (self.blocks_null_sink_0, 1))
        self.connect((self.pfb_channelizer_ccf_0, 8), (self.blocks_null_sink_0, 2))
        self.connect((self.pfb_channelizer_ccf_0, 9), (self.blocks_null_sink_0, 3))


# QT sink close method reimplementation
    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "fm_reconstruction")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_synth_channels(self):
        return self.synth_channels

    def set_synth_channels(self, synth_channels):
        self.synth_channels = synth_channels
        self.set_pfb_synth_taps(firdes.low_pass_2(self.channels/2, self.synth_channels*self.ch_rate, self.ch_bw, self.ch_tb, self.atten, firdes.WIN_BLACKMAN_HARRIS))
        self.set_fm_quad_rate(self.ch_rate*self.synth_channels)
        self.fir_filter_xxx_0.set_taps((firdes.low_pass_2(1, self.ch_rate*self.synth_channels, 250e3, 300e3, 40, firdes.WIN_BLACKMAN_HARRIS) ))
        self.qtgui_freq_sink_x_0_0_0.set_frequency_range(0, self.ch_rate*self.synth_channels)

    def get_channels(self):
        return self.channels

    def set_channels(self, channels):
        self.channels = channels
        self.set_pfb_synth_taps(firdes.low_pass_2(self.channels/2, self.synth_channels*self.ch_rate, self.ch_bw, self.ch_tb, self.atten, firdes.WIN_BLACKMAN_HARRIS))
        self.set_samp_rate(self.ch_rate*self.channels)

    def get_ch_rate(self):
        return self.ch_rate

    def set_ch_rate(self, ch_rate):
        self.ch_rate = ch_rate
        self.set_pfb_synth_taps(firdes.low_pass_2(self.channels/2, self.synth_channels*self.ch_rate, self.ch_bw, self.ch_tb, self.atten, firdes.WIN_BLACKMAN_HARRIS))
        self.set_ch_bw(self.ch_rate/2)
        self.set_fm_quad_rate(self.ch_rate*self.synth_channels)
        self.set_samp_rate(self.ch_rate*self.channels)
        self.fir_filter_xxx_0.set_taps((firdes.low_pass_2(1, self.ch_rate*self.synth_channels, 250e3, 300e3, 40, firdes.WIN_BLACKMAN_HARRIS) ))
        self.qtgui_freq_sink_x_0_0_0.set_frequency_range(0, self.ch_rate*self.synth_channels)
        self.qtgui_freq_sink_x_0_0.set_frequency_range(0, self.ch_rate*2)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_pfb_taps(firdes.low_pass_2(1, self.samp_rate, self.ch_bw, self.ch_tb, self.atten, firdes.WIN_BLACKMAN_HARRIS))
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.tun_freq, self.samp_rate)

    def get_gain(self):
        return self.gain

    def set_gain(self, gain):
        self.gain = gain
        self.set_tun_gain(self.gain)

    def get_fm_quad_rate(self):
        return self.fm_quad_rate

    def set_fm_quad_rate(self, fm_quad_rate):
        self.fm_quad_rate = fm_quad_rate
        self.set_fm_audio_decim(int(self.fm_quad_rate/self.audio_rate)*2)
        self.pfb_arb_resampler_xxx_0.set_rate(44.1e3/(self.fm_quad_rate/self.fm_audio_decim))

    def get_ch_tb(self):
        return self.ch_tb

    def set_ch_tb(self, ch_tb):
        self.ch_tb = ch_tb
        self.set_pfb_synth_taps(firdes.low_pass_2(self.channels/2, self.synth_channels*self.ch_rate, self.ch_bw, self.ch_tb, self.atten, firdes.WIN_BLACKMAN_HARRIS))
        self.set_pfb_taps(firdes.low_pass_2(1, self.samp_rate, self.ch_bw, self.ch_tb, self.atten, firdes.WIN_BLACKMAN_HARRIS))

    def get_ch_bw(self):
        return self.ch_bw

    def set_ch_bw(self, ch_bw):
        self.ch_bw = ch_bw
        self.set_pfb_synth_taps(firdes.low_pass_2(self.channels/2, self.synth_channels*self.ch_rate, self.ch_bw, self.ch_tb, self.atten, firdes.WIN_BLACKMAN_HARRIS))
        self.set_pfb_taps(firdes.low_pass_2(1, self.samp_rate, self.ch_bw, self.ch_tb, self.atten, firdes.WIN_BLACKMAN_HARRIS))

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq
        self.set_tun_freq(self.center_freq)

    def get_audio_rate(self):
        return self.audio_rate

    def set_audio_rate(self, audio_rate):
        self.audio_rate = audio_rate
        self.set_fm_audio_decim(int(self.fm_quad_rate/self.audio_rate)*2)

    def get_atten(self):
        return self.atten

    def set_atten(self, atten):
        self.atten = atten
        self.set_pfb_synth_taps(firdes.low_pass_2(self.channels/2, self.synth_channels*self.ch_rate, self.ch_bw, self.ch_tb, self.atten, firdes.WIN_BLACKMAN_HARRIS))
        self.set_pfb_taps(firdes.low_pass_2(1, self.samp_rate, self.ch_bw, self.ch_tb, self.atten, firdes.WIN_BLACKMAN_HARRIS))

    def get_volume(self):
        return self.volume

    def set_volume(self, volume):
        self.volume = volume
        Qt.QMetaObject.invokeMethod(self._volume_counter, "setValue", Qt.Q_ARG("double", self.volume))
        Qt.QMetaObject.invokeMethod(self._volume_slider, "setValue", Qt.Q_ARG("double", self.volume))
        self.blocks_multiply_const_vxx.set_k((self.volume, ))

    def get_tun_gain(self):
        return self.tun_gain

    def set_tun_gain(self, tun_gain):
        self.tun_gain = tun_gain
        Qt.QMetaObject.invokeMethod(self._tun_gain_counter, "setValue", Qt.Q_ARG("double", self.tun_gain))
        Qt.QMetaObject.invokeMethod(self._tun_gain_slider, "setValue", Qt.Q_ARG("double", self.tun_gain))
        self.uhd_usrp_source_0.set_gain(self.tun_gain, 0)

    def get_tun_freq(self):
        return self.tun_freq

    def set_tun_freq(self, tun_freq):
        self.tun_freq = tun_freq
        Qt.QMetaObject.invokeMethod(self._tun_freq_counter, "setValue", Qt.Q_ARG("double", self.tun_freq))
        Qt.QMetaObject.invokeMethod(self._tun_freq_slider, "setValue", Qt.Q_ARG("double", self.tun_freq))
        self.uhd_usrp_source_0.set_center_freq(self.tun_freq, 0)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.tun_freq, self.samp_rate)

    def get_pfb_taps(self):
        return self.pfb_taps

    def set_pfb_taps(self, pfb_taps):
        self.pfb_taps = pfb_taps
        self.pfb_channelizer_ccf_0.set_taps((self.pfb_taps))

    def get_pfb_synth_taps(self):
        return self.pfb_synth_taps

    def set_pfb_synth_taps(self, pfb_synth_taps):
        self.pfb_synth_taps = pfb_synth_taps
        self.pfb_synthesizer_ccf_0.set_taps((self.pfb_synth_taps))

    def get_fm_audio_decim(self):
        return self.fm_audio_decim

    def set_fm_audio_decim(self, fm_audio_decim):
        self.fm_audio_decim = fm_audio_decim
        self.pfb_arb_resampler_xxx_0.set_rate(44.1e3/(self.fm_quad_rate/self.fm_audio_decim))

    def get_channel(self):
        return self.channel

    def set_channel(self, channel):
        self.channel = channel
        Qt.QMetaObject.invokeMethod(self._channel_counter, "setValue", Qt.Q_ARG("double", self.channel))
        Qt.QMetaObject.invokeMethod(self._channel_slider, "setValue", Qt.Q_ARG("double", self.channel))

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    Qt.QApplication.setGraphicsSystem(gr.prefs().get_string('qtgui','style','raster'))
    qapp = Qt.QApplication(sys.argv)
    tb = fm_reconstruction()
    tb.start()
    tb.show()
    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()
    tb = None #to clean up Qt widgets

