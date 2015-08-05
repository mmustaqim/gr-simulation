#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Demo Quantization
# Generated: Tue Oct 14 10:03:55 2014
##################################################

from PyQt4 import Qt
from PyQt4.QtCore import QObject, pyqtSlot
from gnuradio import analog
from gnuradio import blocks
from gnuradio import channels
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import PyQt4.Qwt5 as Qwt
import math
import sip
import sys

class demo_quantization(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Demo Quantization")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Demo Quantization")
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

        self.settings = Qt.QSettings("GNU Radio", "demo_quantization")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 100000
        self.signal_amp = signal_amp = -150
        self.sigfreq = sigfreq = samp_rate*1.0247385/11.0
        self.noise_amp = noise_amp = -150
        self.center = center = samp_rate/11.0
        self.bw = bw = samp_rate/2
        self.bits = bits = 2

        ##################################################
        # Blocks
        ##################################################
        self._signal_amp_layout = Qt.QVBoxLayout()
        self._signal_amp_tool_bar = Qt.QToolBar(self)
        self._signal_amp_layout.addWidget(self._signal_amp_tool_bar)
        self._signal_amp_tool_bar.addWidget(Qt.QLabel("Singal Power"+": "))
        class qwt_counter_pyslot(Qwt.QwtCounter):
            def __init__(self, parent=None):
                Qwt.QwtCounter.__init__(self, parent)
            @pyqtSlot('double')
            def setValue(self, value):
                super(Qwt.QwtCounter, self).setValue(value)
        self._signal_amp_counter = qwt_counter_pyslot()
        self._signal_amp_counter.setRange(-150, 0, 5)
        self._signal_amp_counter.setNumButtons(2)
        self._signal_amp_counter.setValue(self.signal_amp)
        self._signal_amp_tool_bar.addWidget(self._signal_amp_counter)
        self._signal_amp_counter.valueChanged.connect(self.set_signal_amp)
        self._signal_amp_slider = Qwt.QwtSlider(None, Qt.Qt.Horizontal, Qwt.QwtSlider.BottomScale, Qwt.QwtSlider.BgSlot)
        self._signal_amp_slider.setRange(-150, 0, 5)
        self._signal_amp_slider.setValue(self.signal_amp)
        self._signal_amp_slider.setMinimumWidth(200)
        self._signal_amp_slider.valueChanged.connect(self.set_signal_amp)
        self._signal_amp_layout.addWidget(self._signal_amp_slider)
        self.top_grid_layout.addLayout(self._signal_amp_layout, 2,0,1,1)
        self._sigfreq_layout = Qt.QVBoxLayout()
        self._sigfreq_tool_bar = Qt.QToolBar(self)
        self._sigfreq_layout.addWidget(self._sigfreq_tool_bar)
        self._sigfreq_tool_bar.addWidget(Qt.QLabel("Signal Freq"+": "))
        class qwt_counter_pyslot(Qwt.QwtCounter):
            def __init__(self, parent=None):
                Qwt.QwtCounter.__init__(self, parent)
            @pyqtSlot('double')
            def setValue(self, value):
                super(Qwt.QwtCounter, self).setValue(value)
        self._sigfreq_counter = qwt_counter_pyslot()
        self._sigfreq_counter.setRange(0, samp_rate/2, 1000)
        self._sigfreq_counter.setNumButtons(2)
        self._sigfreq_counter.setValue(self.sigfreq)
        self._sigfreq_tool_bar.addWidget(self._sigfreq_counter)
        self._sigfreq_counter.valueChanged.connect(self.set_sigfreq)
        self._sigfreq_slider = Qwt.QwtSlider(None, Qt.Qt.Horizontal, Qwt.QwtSlider.BottomScale, Qwt.QwtSlider.BgSlot)
        self._sigfreq_slider.setRange(0, samp_rate/2, 1000)
        self._sigfreq_slider.setValue(self.sigfreq)
        self._sigfreq_slider.setMinimumWidth(200)
        self._sigfreq_slider.valueChanged.connect(self.set_sigfreq)
        self._sigfreq_layout.addWidget(self._sigfreq_slider)
        self.top_grid_layout.addLayout(self._sigfreq_layout, 3,0,1,1)
        self._noise_amp_layout = Qt.QVBoxLayout()
        self._noise_amp_tool_bar = Qt.QToolBar(self)
        self._noise_amp_layout.addWidget(self._noise_amp_tool_bar)
        self._noise_amp_tool_bar.addWidget(Qt.QLabel("Noise Power"+": "))
        class qwt_counter_pyslot(Qwt.QwtCounter):
            def __init__(self, parent=None):
                Qwt.QwtCounter.__init__(self, parent)
            @pyqtSlot('double')
            def setValue(self, value):
                super(Qwt.QwtCounter, self).setValue(value)
        self._noise_amp_counter = qwt_counter_pyslot()
        self._noise_amp_counter.setRange(-150, 0, 5)
        self._noise_amp_counter.setNumButtons(2)
        self._noise_amp_counter.setValue(self.noise_amp)
        self._noise_amp_tool_bar.addWidget(self._noise_amp_counter)
        self._noise_amp_counter.valueChanged.connect(self.set_noise_amp)
        self._noise_amp_slider = Qwt.QwtSlider(None, Qt.Qt.Horizontal, Qwt.QwtSlider.BottomScale, Qwt.QwtSlider.BgSlot)
        self._noise_amp_slider.setRange(-150, 0, 5)
        self._noise_amp_slider.setValue(self.noise_amp)
        self._noise_amp_slider.setMinimumWidth(200)
        self._noise_amp_slider.valueChanged.connect(self.set_noise_amp)
        self._noise_amp_layout.addWidget(self._noise_amp_slider)
        self.top_grid_layout.addLayout(self._noise_amp_layout, 2,1,1,1)
        self._center_layout = Qt.QVBoxLayout()
        self._center_tool_bar = Qt.QToolBar(self)
        self._center_layout.addWidget(self._center_tool_bar)
        self._center_tool_bar.addWidget(Qt.QLabel("Center Freq"+": "))
        class qwt_counter_pyslot(Qwt.QwtCounter):
            def __init__(self, parent=None):
                Qwt.QwtCounter.__init__(self, parent)
            @pyqtSlot('double')
            def setValue(self, value):
                super(Qwt.QwtCounter, self).setValue(value)
        self._center_counter = qwt_counter_pyslot()
        self._center_counter.setRange(0, samp_rate/2, 100)
        self._center_counter.setNumButtons(2)
        self._center_counter.setValue(self.center)
        self._center_tool_bar.addWidget(self._center_counter)
        self._center_counter.valueChanged.connect(self.set_center)
        self._center_slider = Qwt.QwtSlider(None, Qt.Qt.Horizontal, Qwt.QwtSlider.BottomScale, Qwt.QwtSlider.BgSlot)
        self._center_slider.setRange(0, samp_rate/2, 100)
        self._center_slider.setValue(self.center)
        self._center_slider.setMinimumWidth(200)
        self._center_slider.valueChanged.connect(self.set_center)
        self._center_layout.addWidget(self._center_slider)
        self.top_grid_layout.addLayout(self._center_layout, 3,1,1,1)
        self._bw_layout = Qt.QVBoxLayout()
        self._bw_tool_bar = Qt.QToolBar(self)
        self._bw_layout.addWidget(self._bw_tool_bar)
        self._bw_tool_bar.addWidget(Qt.QLabel("BW"+": "))
        class qwt_counter_pyslot(Qwt.QwtCounter):
            def __init__(self, parent=None):
                Qwt.QwtCounter.__init__(self, parent)
            @pyqtSlot('double')
            def setValue(self, value):
                super(Qwt.QwtCounter, self).setValue(value)
        self._bw_counter = qwt_counter_pyslot()
        self._bw_counter.setRange(samp_rate/100.0, samp_rate/2, 100)
        self._bw_counter.setNumButtons(2)
        self._bw_counter.setValue(self.bw)
        self._bw_tool_bar.addWidget(self._bw_counter)
        self._bw_counter.valueChanged.connect(self.set_bw)
        self._bw_slider = Qwt.QwtSlider(None, Qt.Qt.Horizontal, Qwt.QwtSlider.BottomScale, Qwt.QwtSlider.BgSlot)
        self._bw_slider.setRange(samp_rate/100.0, samp_rate/2, 100)
        self._bw_slider.setValue(self.bw)
        self._bw_slider.setMinimumWidth(200)
        self._bw_slider.valueChanged.connect(self.set_bw)
        self._bw_layout.addWidget(self._bw_slider)
        self.top_grid_layout.addLayout(self._bw_layout, 4,1,1,1)
        self._bits_options = [2,4,6,8,10,12,14,16]
        self._bits_labels = map(str, self._bits_options)
        self._bits_tool_bar = Qt.QToolBar(self)
        self._bits_tool_bar.addWidget(Qt.QLabel("Bits"+": "))
        self._bits_combo_box = Qt.QComboBox()
        self._bits_tool_bar.addWidget(self._bits_combo_box)
        for label in self._bits_labels: self._bits_combo_box.addItem(label)
        self._bits_callback = lambda i: Qt.QMetaObject.invokeMethod(self._bits_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._bits_options.index(i)))
        self._bits_callback(self.bits)
        self._bits_combo_box.currentIndexChanged.connect(
        	lambda i: self.set_bits(self._bits_options[i]))
        self.top_grid_layout.addWidget(self._bits_tool_bar, 4,0,1,1)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	128, #size
        	samp_rate, #samp_rate
        	"QT GUI Plot", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1 - pow(2,bits-1), 1 + pow(2,bits-1))
        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_NORM, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_win, 1,0,1,2)
        self.qtgui_histogram_sink_x_0 = qtgui.histogram_sink_f(
        	10000,
        	100,
                -1 - pow(2,bits-1),
                1 + pow(2,bits-1),
        	"QT GUI Plot",
        	1
        )
        self.qtgui_histogram_sink_x_0.set_update_time(0.10)
        self._qtgui_histogram_sink_x_0_win = sip.wrapinstance(self.qtgui_histogram_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_histogram_sink_x_0_win, 0,1,1,1)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_f(
        	2048, #size
        	firdes.WIN_FLATTOP, #wintype
        	0, #fc
        	samp_rate, #bw
        	"QT GUI Plot", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-180, 0)
        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_win, 0,0,1,1)
        self.channels_quantizer_0 = channels.quantizer(bits)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((pow(2,bits-1), ))
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.band_pass_filter_0 = filter.fir_filter_fff(1, firdes.band_pass(
        	1, samp_rate, max(bw/15.0,center-bw/2.0), min(samp_rate/2.0-bw/15.0,center+bw/2.0), bw/5.0, firdes.WIN_HANN, 6.76))
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, sigfreq, pow(10.0,signal_amp/20.0), 0)
        self.analog_noise_source_x_0 = analog.noise_source_f(analog.GR_GAUSSIAN, pow(10.0,noise_amp/20.0), 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.band_pass_filter_0, 0))
        self.connect((self.band_pass_filter_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.channels_quantizer_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.qtgui_histogram_sink_x_0, 0))
        self.connect((self.channels_quantizer_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.channels_quantizer_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.qtgui_time_sink_x_0, 0))


# QT sink close method reimplementation
    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "demo_quantization")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, max(self.bw/15.0,self.center-self.bw/2.0), min(self.samp_rate/2.0-self.bw/15.0,self.center+self.bw/2.0), self.bw/5.0, firdes.WIN_HANN, 6.76))
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.set_sigfreq(self.samp_rate*1.0247385/11.0)
        self.set_center(self.samp_rate/11.0)
        self.set_bw(self.samp_rate/2)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)

    def get_signal_amp(self):
        return self.signal_amp

    def set_signal_amp(self, signal_amp):
        self.signal_amp = signal_amp
        self.analog_sig_source_x_0.set_amplitude(pow(10.0,self.signal_amp/20.0))
        Qt.QMetaObject.invokeMethod(self._signal_amp_counter, "setValue", Qt.Q_ARG("double", self.signal_amp))
        Qt.QMetaObject.invokeMethod(self._signal_amp_slider, "setValue", Qt.Q_ARG("double", self.signal_amp))

    def get_sigfreq(self):
        return self.sigfreq

    def set_sigfreq(self, sigfreq):
        self.sigfreq = sigfreq
        self.analog_sig_source_x_0.set_frequency(self.sigfreq)
        Qt.QMetaObject.invokeMethod(self._sigfreq_counter, "setValue", Qt.Q_ARG("double", self.sigfreq))
        Qt.QMetaObject.invokeMethod(self._sigfreq_slider, "setValue", Qt.Q_ARG("double", self.sigfreq))

    def get_noise_amp(self):
        return self.noise_amp

    def set_noise_amp(self, noise_amp):
        self.noise_amp = noise_amp
        self.analog_noise_source_x_0.set_amplitude(pow(10.0,self.noise_amp/20.0))
        Qt.QMetaObject.invokeMethod(self._noise_amp_counter, "setValue", Qt.Q_ARG("double", self.noise_amp))
        Qt.QMetaObject.invokeMethod(self._noise_amp_slider, "setValue", Qt.Q_ARG("double", self.noise_amp))

    def get_center(self):
        return self.center

    def set_center(self, center):
        self.center = center
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, max(self.bw/15.0,self.center-self.bw/2.0), min(self.samp_rate/2.0-self.bw/15.0,self.center+self.bw/2.0), self.bw/5.0, firdes.WIN_HANN, 6.76))
        Qt.QMetaObject.invokeMethod(self._center_counter, "setValue", Qt.Q_ARG("double", self.center))
        Qt.QMetaObject.invokeMethod(self._center_slider, "setValue", Qt.Q_ARG("double", self.center))

    def get_bw(self):
        return self.bw

    def set_bw(self, bw):
        self.bw = bw
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, max(self.bw/15.0,self.center-self.bw/2.0), min(self.samp_rate/2.0-self.bw/15.0,self.center+self.bw/2.0), self.bw/5.0, firdes.WIN_HANN, 6.76))
        Qt.QMetaObject.invokeMethod(self._bw_counter, "setValue", Qt.Q_ARG("double", self.bw))
        Qt.QMetaObject.invokeMethod(self._bw_slider, "setValue", Qt.Q_ARG("double", self.bw))

    def get_bits(self):
        return self.bits

    def set_bits(self, bits):
        self.bits = bits
        self.blocks_multiply_const_vxx_0.set_k((pow(2,self.bits-1), ))
        self.qtgui_time_sink_x_0.set_y_axis(-1 - pow(2,self.bits-1), 1 + pow(2,self.bits-1))
        self.channels_quantizer_0.set_bits(self.bits)
        self._bits_callback(self.bits)

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
    tb = demo_quantization()
    tb.start()
    tb.show()
    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()
    tb = None #to clean up Qt widgets

