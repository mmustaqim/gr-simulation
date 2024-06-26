#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Demo Phase Noise
# Generated: Fri Aug 22 08:13:47 2014
##################################################

from PyQt4 import Qt
from PyQt4.QtCore import QObject, pyqtSlot
from gnuradio import analog
from gnuradio import blocks
from gnuradio import channels
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import PyQt4.Qwt5 as Qwt
import math
import sip
import sys

class demo_phase_noise(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Demo Phase Noise")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Demo Phase Noise")
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

        self.settings = Qt.QSettings("GNU Radio", "demo_phase_noise")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 1000000
        self.signal_amp = signal_amp = 0
        self.sigfreq = sigfreq = samp_rate/10.0
        self.phase_noise = phase_noise = 0
        self.noise_amp = noise_amp = -150

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
        self._signal_amp_counter.setRange(-150, 10, 5)
        self._signal_amp_counter.setNumButtons(2)
        self._signal_amp_counter.setValue(self.signal_amp)
        self._signal_amp_tool_bar.addWidget(self._signal_amp_counter)
        self._signal_amp_counter.valueChanged.connect(self.set_signal_amp)
        self._signal_amp_slider = Qwt.QwtSlider(None, Qt.Qt.Horizontal, Qwt.QwtSlider.BottomScale, Qwt.QwtSlider.BgSlot)
        self._signal_amp_slider.setRange(-150, 10, 5)
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
        self._phase_noise_layout = Qt.QVBoxLayout()
        self._phase_noise_tool_bar = Qt.QToolBar(self)
        self._phase_noise_layout.addWidget(self._phase_noise_tool_bar)
        self._phase_noise_tool_bar.addWidget(Qt.QLabel("Phase Noise"+": "))
        class qwt_counter_pyslot(Qwt.QwtCounter):
            def __init__(self, parent=None):
                Qwt.QwtCounter.__init__(self, parent)
            @pyqtSlot('double')
            def setValue(self, value):
                super(Qwt.QwtCounter, self).setValue(value)
        self._phase_noise_counter = qwt_counter_pyslot()
        self._phase_noise_counter.setRange(0, 1, 0.001)
        self._phase_noise_counter.setNumButtons(2)
        self._phase_noise_counter.setValue(self.phase_noise)
        self._phase_noise_tool_bar.addWidget(self._phase_noise_counter)
        self._phase_noise_counter.valueChanged.connect(self.set_phase_noise)
        self._phase_noise_slider = Qwt.QwtSlider(None, Qt.Qt.Horizontal, Qwt.QwtSlider.BottomScale, Qwt.QwtSlider.BgSlot)
        self._phase_noise_slider.setRange(0, 1, 0.001)
        self._phase_noise_slider.setValue(self.phase_noise)
        self._phase_noise_slider.setMinimumWidth(200)
        self._phase_noise_slider.valueChanged.connect(self.set_phase_noise)
        self._phase_noise_layout.addWidget(self._phase_noise_slider)
        self.top_grid_layout.addLayout(self._phase_noise_layout, 3,1,1,1)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	2048, #size
        	firdes.WIN_FLATTOP, #wintype
        	0, #fc
        	samp_rate, #bw
        	"QT GUI Plot", #name
        	2 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-200, 0)
        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_win, 0,0,1,2)
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
        self.channels_phase_noise_gen_0 = channels.phase_noise_gen(phase_noise, 0.1)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, sigfreq, pow(10.0,signal_amp/20.0), 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.channels_phase_noise_gen_0, 0))
        self.connect((self.channels_phase_noise_gen_0, 0), (self.qtgui_freq_sink_x_0, 1))
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_freq_sink_x_0, 0))


# QT sink close method reimplementation
    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "demo_phase_noise")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.set_sigfreq(self.samp_rate/10.0)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)

    def get_signal_amp(self):
        return self.signal_amp

    def set_signal_amp(self, signal_amp):
        self.signal_amp = signal_amp
        Qt.QMetaObject.invokeMethod(self._signal_amp_counter, "setValue", Qt.Q_ARG("double", self.signal_amp))
        Qt.QMetaObject.invokeMethod(self._signal_amp_slider, "setValue", Qt.Q_ARG("double", self.signal_amp))
        self.analog_sig_source_x_0.set_amplitude(pow(10.0,self.signal_amp/20.0))

    def get_sigfreq(self):
        return self.sigfreq

    def set_sigfreq(self, sigfreq):
        self.sigfreq = sigfreq
        self.analog_sig_source_x_0.set_frequency(self.sigfreq)
        Qt.QMetaObject.invokeMethod(self._sigfreq_counter, "setValue", Qt.Q_ARG("double", self.sigfreq))
        Qt.QMetaObject.invokeMethod(self._sigfreq_slider, "setValue", Qt.Q_ARG("double", self.sigfreq))

    def get_phase_noise(self):
        return self.phase_noise

    def set_phase_noise(self, phase_noise):
        self.phase_noise = phase_noise
        Qt.QMetaObject.invokeMethod(self._phase_noise_counter, "setValue", Qt.Q_ARG("double", self.phase_noise))
        Qt.QMetaObject.invokeMethod(self._phase_noise_slider, "setValue", Qt.Q_ARG("double", self.phase_noise))
        self.channels_phase_noise_gen_0.set_noise_mag(self.phase_noise)

    def get_noise_amp(self):
        return self.noise_amp

    def set_noise_amp(self, noise_amp):
        self.noise_amp = noise_amp
        Qt.QMetaObject.invokeMethod(self._noise_amp_counter, "setValue", Qt.Q_ARG("double", self.noise_amp))
        Qt.QMetaObject.invokeMethod(self._noise_amp_slider, "setValue", Qt.Q_ARG("double", self.noise_amp))

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
    tb = demo_phase_noise()
    tb.start()
    tb.show()
    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()
    tb = None #to clean up Qt widgets

