#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Ofdm02
# Generated: Mon Aug 11 11:43:29 2014
##################################################

from PyQt4 import Qt
from PyQt4.QtCore import QObject, pyqtSlot
from gnuradio import blocks
from gnuradio import channels
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import PyQt4.Qwt5 as Qwt
import numpy
import sip
import sys

class ofdm02(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Ofdm02")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Ofdm02")
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

        self.settings = Qt.QSettings("GNU Radio", "ofdm02")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.timing = timing = 1.0001
        self.samp_rate = samp_rate = 100000
        self.packet_len = packet_len = 50
        self.noise = noise = 0.01
        self.len_tag_key = len_tag_key = "packet_len"
        self.freq = freq = 0.01
        self.fft_len = fft_len = 128

        ##################################################
        # Blocks
        ##################################################
        self._timing_layout = Qt.QVBoxLayout()
        self._timing_tool_bar = Qt.QToolBar(self)
        self._timing_layout.addWidget(self._timing_tool_bar)
        self._timing_tool_bar.addWidget(Qt.QLabel("Timing Offset"+": "))
        class qwt_counter_pyslot(Qwt.QwtCounter):
            def __init__(self, parent=None):
                Qwt.QwtCounter.__init__(self, parent)
            @pyqtSlot('double')
            def setValue(self, value):
                super(Qwt.QwtCounter, self).setValue(value)
        self._timing_counter = qwt_counter_pyslot()
        self._timing_counter.setRange(0.999, 1.001, 0.0001)
        self._timing_counter.setNumButtons(2)
        self._timing_counter.setValue(self.timing)
        self._timing_tool_bar.addWidget(self._timing_counter)
        self._timing_counter.valueChanged.connect(self.set_timing)
        self._timing_slider = Qwt.QwtSlider(None, Qt.Qt.Horizontal, Qwt.QwtSlider.BottomScale, Qwt.QwtSlider.BgSlot)
        self._timing_slider.setRange(0.999, 1.001, 0.0001)
        self._timing_slider.setValue(self.timing)
        self._timing_slider.setMinimumWidth(200)
        self._timing_slider.valueChanged.connect(self.set_timing)
        self._timing_layout.addWidget(self._timing_slider)
        self.top_grid_layout.addLayout(self._timing_layout, 2,0,1,1)
        self._noise_layout = Qt.QVBoxLayout()
        self._noise_tool_bar = Qt.QToolBar(self)
        self._noise_layout.addWidget(self._noise_tool_bar)
        self._noise_tool_bar.addWidget(Qt.QLabel("Noise Voltage"+": "))
        class qwt_counter_pyslot(Qwt.QwtCounter):
            def __init__(self, parent=None):
                Qwt.QwtCounter.__init__(self, parent)
            @pyqtSlot('double')
            def setValue(self, value):
                super(Qwt.QwtCounter, self).setValue(value)
        self._noise_counter = qwt_counter_pyslot()
        self._noise_counter.setRange(0, 3, 0.01)
        self._noise_counter.setNumButtons(2)
        self._noise_counter.setValue(self.noise)
        self._noise_tool_bar.addWidget(self._noise_counter)
        self._noise_counter.valueChanged.connect(self.set_noise)
        self._noise_slider = Qwt.QwtSlider(None, Qt.Qt.Horizontal, Qwt.QwtSlider.BottomScale, Qwt.QwtSlider.BgSlot)
        self._noise_slider.setRange(0, 3, 0.01)
        self._noise_slider.setValue(self.noise)
        self._noise_slider.setMinimumWidth(200)
        self._noise_slider.valueChanged.connect(self.set_noise)
        self._noise_layout.addWidget(self._noise_slider)
        self.top_grid_layout.addLayout(self._noise_layout, 1,0,1,1)
        self._freq_layout = Qt.QVBoxLayout()
        self._freq_tool_bar = Qt.QToolBar(self)
        self._freq_layout.addWidget(self._freq_tool_bar)
        self._freq_tool_bar.addWidget(Qt.QLabel("Frequency Offset"+": "))
        class qwt_counter_pyslot(Qwt.QwtCounter):
            def __init__(self, parent=None):
                Qwt.QwtCounter.__init__(self, parent)
            @pyqtSlot('double')
            def setValue(self, value):
                super(Qwt.QwtCounter, self).setValue(value)
        self._freq_counter = qwt_counter_pyslot()
        self._freq_counter.setRange(-1, 1, 0.01)
        self._freq_counter.setNumButtons(2)
        self._freq_counter.setValue(self.freq)
        self._freq_tool_bar.addWidget(self._freq_counter)
        self._freq_counter.valueChanged.connect(self.set_freq)
        self._freq_slider = Qwt.QwtSlider(None, Qt.Qt.Horizontal, Qwt.QwtSlider.BottomScale, Qwt.QwtSlider.BgSlot)
        self._freq_slider.setRange(-1, 1, 0.01)
        self._freq_slider.setValue(self.freq)
        self._freq_slider.setMinimumWidth(200)
        self._freq_slider.valueChanged.connect(self.set_freq)
        self._freq_layout.addWidget(self._freq_slider)
        self.top_grid_layout.addLayout(self._freq_layout, 1,1,1,1)
        self.qtgui_waterfall_sink_x_0 = qtgui.waterfall_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"QT GUI Plot", #name
                1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0.set_update_time(0.10)
        self._qtgui_waterfall_sink_x_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_waterfall_sink_x_0_win, 0,1,1,1)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"QT GUI Plot", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-80, 10)
        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_win, 0,0,1,1)
        self.digital_ofdm_tx_0 = digital.ofdm_tx(
        	  fft_len=fft_len, cp_len=fft_len/4,
        	  packet_length_tag_key=len_tag_key,
        	  bps_header=1,
        	  bps_payload=2,
        	  rolloff=0,
        	  debug_log=False,
        	  scramble_bits=False
        	 )
        self.digital_ofdm_rx_0 = digital.ofdm_rx(
        	  fft_len=fft_len, cp_len=fft_len/4,
        	  frame_length_tag_key='frame_'+"rx_len",
        	  packet_length_tag_key="rx_len",
        	  bps_header=1,
        	  bps_payload=2,
        	  debug_log=False,
        	  scramble_bits=False
        	 )
        self.channels_fading_model_0 = channels.fading_model( 8, 10.0/samp_rate, False, 4.0, 0 )
        self.channels_channel_model_0 = channels.channel_model(
        	noise_voltage=noise,
        	frequency_offset=freq,
        	epsilon=timing,
        	taps=(1.0, ),
        	noise_seed=0,
        	block_tags=False
        )
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_tag_debug_0 = blocks.tag_debug(gr.sizeof_char*1, "", ""); self.blocks_tag_debug_0.set_display(True)
        self.blocks_stream_to_tagged_stream_0 = blocks.stream_to_tagged_stream(gr.sizeof_char, 1, packet_len, len_tag_key)
        self.analog_random_source_x_0 = blocks.vector_source_b(map(int, numpy.random.randint(0, 256, 1000)), True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.digital_ofdm_tx_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.analog_random_source_x_0, 0), (self.blocks_stream_to_tagged_stream_0, 0))
        self.connect((self.blocks_stream_to_tagged_stream_0, 0), (self.digital_ofdm_tx_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.channels_fading_model_0, 0))
        self.connect((self.channels_fading_model_0, 0), (self.channels_channel_model_0, 0))
        self.connect((self.channels_channel_model_0, 0), (self.digital_ofdm_rx_0, 0))
        self.connect((self.channels_channel_model_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.channels_channel_model_0, 0), (self.qtgui_waterfall_sink_x_0, 0))
        self.connect((self.digital_ofdm_rx_0, 0), (self.blocks_tag_debug_0, 0))


# QT sink close method reimplementation
    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "ofdm02")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_timing(self):
        return self.timing

    def set_timing(self, timing):
        self.timing = timing
        self.channels_channel_model_0.set_timing_offset(self.timing)
        Qt.QMetaObject.invokeMethod(self._timing_counter, "setValue", Qt.Q_ARG("double", self.timing))
        Qt.QMetaObject.invokeMethod(self._timing_slider, "setValue", Qt.Q_ARG("double", self.timing))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.channels_fading_model_0.set_fDTs(10.0/self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(0, self.samp_rate)

    def get_packet_len(self):
        return self.packet_len

    def set_packet_len(self, packet_len):
        self.packet_len = packet_len

    def get_noise(self):
        return self.noise

    def set_noise(self, noise):
        self.noise = noise
        self.channels_channel_model_0.set_noise_voltage(self.noise)
        Qt.QMetaObject.invokeMethod(self._noise_counter, "setValue", Qt.Q_ARG("double", self.noise))
        Qt.QMetaObject.invokeMethod(self._noise_slider, "setValue", Qt.Q_ARG("double", self.noise))

    def get_len_tag_key(self):
        return self.len_tag_key

    def set_len_tag_key(self, len_tag_key):
        self.len_tag_key = len_tag_key

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.channels_channel_model_0.set_frequency_offset(self.freq)
        Qt.QMetaObject.invokeMethod(self._freq_counter, "setValue", Qt.Q_ARG("double", self.freq))
        Qt.QMetaObject.invokeMethod(self._freq_slider, "setValue", Qt.Q_ARG("double", self.freq))

    def get_fft_len(self):
        return self.fft_len

    def set_fft_len(self, fft_len):
        self.fft_len = fft_len

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
    tb = ofdm02()
    tb.start()
    tb.show()
    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()
    tb = None #to clean up Qt widgets

