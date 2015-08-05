#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Ofdm05
# Generated: Sun Jun 22 20:28:19 2014
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

class ofdm05(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Ofdm05")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Ofdm05")
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

        self.settings = Qt.QSettings("GNU Radio", "ofdm05")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.timing = timing = 1.0001
        self.samp_rate = samp_rate = 7.68e6
        self.q_offset = q_offset = 0
        self.phase_noise = phase_noise = 0
        self.packet_len = packet_len = 50
        self.noise = noise = 1.2
        self.len_tag_key = len_tag_key = "packet_len"
        self.iq_ph = iq_ph = 0
        self.iq_mag = iq_mag = 0
        self.i_offset = i_offset = 0
        self.freq = freq = 0.01
        self.fft_len = fft_len = 128
        self.dist3 = dist3 = 0
        self.dist2 = dist2 = 0

        ##################################################
        # Blocks
        ##################################################
        self._timing_layout = Qt.QVBoxLayout()
        self._timing_label = Qt.QLabel("Timing Offset")
        self._timing_slider = Qwt.QwtSlider(None, Qt.Qt.Horizontal, Qwt.QwtSlider.BottomScale, Qwt.QwtSlider.BgSlot)
        self._timing_slider.setRange(0.999, 1.001, 0.0001)
        self._timing_slider.setValue(self.timing)
        self._timing_slider.setMinimumWidth(200)
        self._timing_slider.valueChanged.connect(self.set_timing)
        self._timing_label.setAlignment(Qt.Qt.AlignBottom | Qt.Qt.AlignHCenter)
        self._timing_layout.addWidget(self._timing_label)
        self._timing_layout.addWidget(self._timing_slider)
        self.top_grid_layout.addLayout(self._timing_layout, 1,2,1,1)
        self._q_offset_layout = Qt.QVBoxLayout()
        self._q_offset_label = Qt.QLabel("Quadrature Offset")
        self._q_offset_slider = Qwt.QwtSlider(None, Qt.Qt.Horizontal, Qwt.QwtSlider.BottomScale, Qwt.QwtSlider.BgSlot)
        self._q_offset_slider.setRange(-1, 1, 0.01)
        self._q_offset_slider.setValue(self.q_offset)
        self._q_offset_slider.setMinimumWidth(200)
        self._q_offset_slider.valueChanged.connect(self.set_q_offset)
        self._q_offset_label.setAlignment(Qt.Qt.AlignBottom | Qt.Qt.AlignHCenter)
        self._q_offset_layout.addWidget(self._q_offset_label)
        self._q_offset_layout.addWidget(self._q_offset_slider)
        self.top_grid_layout.addLayout(self._q_offset_layout, 2,3,1,1)
        self._phase_noise_layout = Qt.QVBoxLayout()
        self._phase_noise_label = Qt.QLabel("Phase Noise")
        self._phase_noise_slider = Qwt.QwtSlider(None, Qt.Qt.Horizontal, Qwt.QwtSlider.BottomScale, Qwt.QwtSlider.BgSlot)
        self._phase_noise_slider.setRange(0, 40, 0.5)
        self._phase_noise_slider.setValue(self.phase_noise)
        self._phase_noise_slider.setMinimumWidth(200)
        self._phase_noise_slider.valueChanged.connect(self.set_phase_noise)
        self._phase_noise_label.setAlignment(Qt.Qt.AlignBottom | Qt.Qt.AlignHCenter)
        self._phase_noise_layout.addWidget(self._phase_noise_label)
        self._phase_noise_layout.addWidget(self._phase_noise_slider)
        self.top_grid_layout.addLayout(self._phase_noise_layout, 1,3,1,1)
        self._noise_layout = Qt.QVBoxLayout()
        self._noise_label = Qt.QLabel("Noise Voltage")
        self._noise_slider = Qwt.QwtSlider(None, Qt.Qt.Horizontal, Qwt.QwtSlider.BottomScale, Qwt.QwtSlider.BgSlot)
        self._noise_slider.setRange(0, 2, 0.01)
        self._noise_slider.setValue(self.noise)
        self._noise_slider.setMinimumWidth(200)
        self._noise_slider.valueChanged.connect(self.set_noise)
        self._noise_label.setAlignment(Qt.Qt.AlignBottom | Qt.Qt.AlignHCenter)
        self._noise_layout.addWidget(self._noise_label)
        self._noise_layout.addWidget(self._noise_slider)
        self.top_grid_layout.addLayout(self._noise_layout, 1,0,1,1)
        self._iq_ph_layout = Qt.QVBoxLayout()
        self._iq_ph_label = Qt.QLabel("IQ Phase Imbalance")
        self._iq_ph_slider = Qwt.QwtSlider(None, Qt.Qt.Horizontal, Qwt.QwtSlider.BottomScale, Qwt.QwtSlider.BgSlot)
        self._iq_ph_slider.setRange(-3.14, 3.14, 0.01)
        self._iq_ph_slider.setValue(self.iq_ph)
        self._iq_ph_slider.setMinimumWidth(200)
        self._iq_ph_slider.valueChanged.connect(self.set_iq_ph)
        self._iq_ph_label.setAlignment(Qt.Qt.AlignBottom | Qt.Qt.AlignHCenter)
        self._iq_ph_layout.addWidget(self._iq_ph_label)
        self._iq_ph_layout.addWidget(self._iq_ph_slider)
        self.top_grid_layout.addLayout(self._iq_ph_layout, 2,1,1,1)
        self._iq_mag_layout = Qt.QVBoxLayout()
        self._iq_mag_label = Qt.QLabel("IQ Mag. Imbalance")
        self._iq_mag_slider = Qwt.QwtSlider(None, Qt.Qt.Horizontal, Qwt.QwtSlider.BottomScale, Qwt.QwtSlider.BgSlot)
        self._iq_mag_slider.setRange(0, 1, 0.01)
        self._iq_mag_slider.setValue(self.iq_mag)
        self._iq_mag_slider.setMinimumWidth(200)
        self._iq_mag_slider.valueChanged.connect(self.set_iq_mag)
        self._iq_mag_label.setAlignment(Qt.Qt.AlignBottom | Qt.Qt.AlignHCenter)
        self._iq_mag_layout.addWidget(self._iq_mag_label)
        self._iq_mag_layout.addWidget(self._iq_mag_slider)
        self.top_grid_layout.addLayout(self._iq_mag_layout, 2,0,1,1)
        self._i_offset_layout = Qt.QVBoxLayout()
        self._i_offset_label = Qt.QLabel("Inphase Offset")
        self._i_offset_slider = Qwt.QwtSlider(None, Qt.Qt.Horizontal, Qwt.QwtSlider.BottomScale, Qwt.QwtSlider.BgSlot)
        self._i_offset_slider.setRange(-1, 1, 0.01)
        self._i_offset_slider.setValue(self.i_offset)
        self._i_offset_slider.setMinimumWidth(200)
        self._i_offset_slider.valueChanged.connect(self.set_i_offset)
        self._i_offset_label.setAlignment(Qt.Qt.AlignBottom | Qt.Qt.AlignHCenter)
        self._i_offset_layout.addWidget(self._i_offset_label)
        self._i_offset_layout.addWidget(self._i_offset_slider)
        self.top_grid_layout.addLayout(self._i_offset_layout, 2,2,1,1)
        self._freq_layout = Qt.QVBoxLayout()
        self._freq_label = Qt.QLabel("Frequency Offset")
        self._freq_slider = Qwt.QwtSlider(None, Qt.Qt.Horizontal, Qwt.QwtSlider.BottomScale, Qwt.QwtSlider.BgSlot)
        self._freq_slider.setRange(-1, 1, 0.01)
        self._freq_slider.setValue(self.freq)
        self._freq_slider.setMinimumWidth(200)
        self._freq_slider.valueChanged.connect(self.set_freq)
        self._freq_label.setAlignment(Qt.Qt.AlignBottom | Qt.Qt.AlignHCenter)
        self._freq_layout.addWidget(self._freq_label)
        self._freq_layout.addWidget(self._freq_slider)
        self.top_grid_layout.addLayout(self._freq_layout, 1,1,1,1)
        self._dist3_layout = Qt.QVBoxLayout()
        self._dist3_label = Qt.QLabel("Third Order Dist")
        self._dist3_slider = Qwt.QwtSlider(None, Qt.Qt.Horizontal, Qwt.QwtSlider.BottomScale, Qwt.QwtSlider.BgSlot)
        self._dist3_slider.setRange(0, 0.1, 0.0001)
        self._dist3_slider.setValue(self.dist3)
        self._dist3_slider.setMinimumWidth(200)
        self._dist3_slider.valueChanged.connect(self.set_dist3)
        self._dist3_label.setAlignment(Qt.Qt.AlignBottom | Qt.Qt.AlignHCenter)
        self._dist3_layout.addWidget(self._dist3_label)
        self._dist3_layout.addWidget(self._dist3_slider)
        self.top_grid_layout.addLayout(self._dist3_layout, 3,1,1,1)
        self._dist2_layout = Qt.QVBoxLayout()
        self._dist2_label = Qt.QLabel("2nd Order Dist.")
        self._dist2_slider = Qwt.QwtSlider(None, Qt.Qt.Horizontal, Qwt.QwtSlider.BottomScale, Qwt.QwtSlider.BgSlot)
        self._dist2_slider.setRange(0, 0.1, 0.0001)
        self._dist2_slider.setValue(self.dist2)
        self._dist2_slider.setMinimumWidth(200)
        self._dist2_slider.valueChanged.connect(self.set_dist2)
        self._dist2_label.setAlignment(Qt.Qt.AlignBottom | Qt.Qt.AlignHCenter)
        self._dist2_layout.addWidget(self._dist2_label)
        self._dist2_layout.addWidget(self._dist2_slider)
        self.top_grid_layout.addLayout(self._dist2_layout, 3,0,1,1)
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
        self.top_grid_layout.addWidget(self._qtgui_waterfall_sink_x_0_win, 0,2,1,2)
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
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_win, 0,0,1,2)
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
        self.channels_impairments_0 = channels.impairments(phase_noise, iq_mag, iq_ph, q_offset, i_offset, 0, dist2, dist3)
        self.channels_channel_model_0 = channels.channel_model(
        	noise_voltage=noise,
        	frequency_offset=freq,
        	epsilon=timing,
        	taps=(1.0, ),
        	noise_seed=0,
        	block_tags=False
        )
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_tag_debug_0 = blocks.tag_debug(gr.sizeof_char*1, "", "packet_num"); self.blocks_tag_debug_0.set_display(True)
        self.blocks_stream_to_tagged_stream_0 = blocks.stream_to_tagged_stream(gr.sizeof_char, 1, packet_len, len_tag_key)
        self.analog_random_source_x_0 = blocks.vector_source_b(map(int, numpy.random.randint(0, 256, 1000)), True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.digital_ofdm_tx_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.channels_impairments_0, 0), (self.digital_ofdm_rx_0, 0))
        self.connect((self.blocks_stream_to_tagged_stream_0, 0), (self.digital_ofdm_tx_0, 0))
        self.connect((self.analog_random_source_x_0, 0), (self.blocks_stream_to_tagged_stream_0, 0))
        self.connect((self.channels_channel_model_0, 0), (self.channels_impairments_0, 0))
        self.connect((self.channels_impairments_0, 0), (self.qtgui_waterfall_sink_x_0, 0))
        self.connect((self.channels_impairments_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.digital_ofdm_rx_0, 0), (self.blocks_tag_debug_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.channels_channel_model_0, 0))


# QT sink close method reimplementation
    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "ofdm05")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_timing(self):
        return self.timing

    def set_timing(self, timing):
        self.timing = timing
        Qt.QMetaObject.invokeMethod(self._timing_slider, "setValue", Qt.Q_ARG("double", self.timing))
        self.channels_channel_model_0.set_timing_offset(self.timing)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_waterfall_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_q_offset(self):
        return self.q_offset

    def set_q_offset(self, q_offset):
        self.q_offset = q_offset
        self.channels_impairments_0.set_q_ofs(self.q_offset)
        Qt.QMetaObject.invokeMethod(self._q_offset_slider, "setValue", Qt.Q_ARG("double", self.q_offset))

    def get_phase_noise(self):
        return self.phase_noise

    def set_phase_noise(self, phase_noise):
        self.phase_noise = phase_noise
        self.channels_impairments_0.set_phase_noise_mag(self.phase_noise)
        Qt.QMetaObject.invokeMethod(self._phase_noise_slider, "setValue", Qt.Q_ARG("double", self.phase_noise))

    def get_packet_len(self):
        return self.packet_len

    def set_packet_len(self, packet_len):
        self.packet_len = packet_len

    def get_noise(self):
        return self.noise

    def set_noise(self, noise):
        self.noise = noise
        Qt.QMetaObject.invokeMethod(self._noise_slider, "setValue", Qt.Q_ARG("double", self.noise))
        self.channels_channel_model_0.set_noise_voltage(self.noise)

    def get_len_tag_key(self):
        return self.len_tag_key

    def set_len_tag_key(self, len_tag_key):
        self.len_tag_key = len_tag_key

    def get_iq_ph(self):
        return self.iq_ph

    def set_iq_ph(self, iq_ph):
        self.iq_ph = iq_ph
        self.channels_impairments_0.set_phasebal(self.iq_ph)
        Qt.QMetaObject.invokeMethod(self._iq_ph_slider, "setValue", Qt.Q_ARG("double", self.iq_ph))

    def get_iq_mag(self):
        return self.iq_mag

    def set_iq_mag(self, iq_mag):
        self.iq_mag = iq_mag
        self.channels_impairments_0.set_magbal(self.iq_mag)
        Qt.QMetaObject.invokeMethod(self._iq_mag_slider, "setValue", Qt.Q_ARG("double", self.iq_mag))

    def get_i_offset(self):
        return self.i_offset

    def set_i_offset(self, i_offset):
        self.i_offset = i_offset
        self.channels_impairments_0.set_i_ofs(self.i_offset)
        Qt.QMetaObject.invokeMethod(self._i_offset_slider, "setValue", Qt.Q_ARG("double", self.i_offset))

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        Qt.QMetaObject.invokeMethod(self._freq_slider, "setValue", Qt.Q_ARG("double", self.freq))
        self.channels_channel_model_0.set_frequency_offset(self.freq)

    def get_fft_len(self):
        return self.fft_len

    def set_fft_len(self, fft_len):
        self.fft_len = fft_len

    def get_dist3(self):
        return self.dist3

    def set_dist3(self, dist3):
        self.dist3 = dist3
        self.channels_impairments_0.set_beta(self.dist3)
        Qt.QMetaObject.invokeMethod(self._dist3_slider, "setValue", Qt.Q_ARG("double", self.dist3))

    def get_dist2(self):
        return self.dist2

    def set_dist2(self, dist2):
        self.dist2 = dist2
        self.channels_impairments_0.set_gamma(self.dist2)
        Qt.QMetaObject.invokeMethod(self._dist2_slider, "setValue", Qt.Q_ARG("double", self.dist2))

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
    tb = ofdm05()
    tb.start()
    tb.show()
    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()
    tb = None #to clean up Qt widgets

