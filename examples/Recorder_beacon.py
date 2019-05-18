#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Recorder Beacon
# GNU Radio version: 3.7.13.4
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import iio
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import sip
import sys
from gnuradio import qtgui


class Recorder_beacon(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Recorder Beacon")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Recorder Beacon")
        qtgui.util.check_set_qss()
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

        self.settings = Qt.QSettings("GNU Radio", "Recorder_beacon")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.symb_rate = symb_rate = 52083
        self.sec_dec = sec_dec = 10
        self.samp_per_symb = samp_per_symb = 10
        self.first_dec = first_dec = 1
        self.f_if = f_if = int(100e3)
        self.doppler = doppler = 10000
        self.channel_bw = channel_bw = 2000000
        self.ad_samp_rate = ad_samp_rate = symb_rate*first_dec*sec_dec*samp_per_symb

        ##################################################
        # Blocks
        ##################################################
        self._doppler_range = Range(-50000, 50000, 1, 10000, 10000)
        self._doppler_win = RangeWidget(self._doppler_range, self.set_doppler, "doppler", "dial", int)
        self.top_grid_layout.addWidget(self._doppler_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	ad_samp_rate, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.iio_fmcomms2_source_0 = iio.fmcomms2_source_f32c('192.168.1.10', 438000000-f_if-doppler, ad_samp_rate, channel_bw, True, False, 0x8000, True, True, True, "fast_attack", 64.0, "manual", 64.0, "A_BALANCED", '', True)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_gr_complex*1, '/home/iust/Documents/zafar_prj/REC1_BEACON.bin', False)
        self.blocks_file_sink_0.set_unbuffered(False)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.iio_fmcomms2_source_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.iio_fmcomms2_source_0, 0), (self.qtgui_freq_sink_x_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "Recorder_beacon")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_symb_rate(self):
        return self.symb_rate

    def set_symb_rate(self, symb_rate):
        self.symb_rate = symb_rate
        self.set_ad_samp_rate(self.symb_rate*self.first_dec*self.sec_dec*self.samp_per_symb)

    def get_sec_dec(self):
        return self.sec_dec

    def set_sec_dec(self, sec_dec):
        self.sec_dec = sec_dec
        self.set_ad_samp_rate(self.symb_rate*self.first_dec*self.sec_dec*self.samp_per_symb)

    def get_samp_per_symb(self):
        return self.samp_per_symb

    def set_samp_per_symb(self, samp_per_symb):
        self.samp_per_symb = samp_per_symb
        self.set_ad_samp_rate(self.symb_rate*self.first_dec*self.sec_dec*self.samp_per_symb)

    def get_first_dec(self):
        return self.first_dec

    def set_first_dec(self, first_dec):
        self.first_dec = first_dec
        self.set_ad_samp_rate(self.symb_rate*self.first_dec*self.sec_dec*self.samp_per_symb)

    def get_f_if(self):
        return self.f_if

    def set_f_if(self, f_if):
        self.f_if = f_if
        self.iio_fmcomms2_source_0.set_params(438000000-self.f_if-self.doppler, self.ad_samp_rate, self.channel_bw, True, True, True, "fast_attack", 64.0, "manual", 64.0, "A_BALANCED", '', True)

    def get_doppler(self):
        return self.doppler

    def set_doppler(self, doppler):
        self.doppler = doppler
        self.iio_fmcomms2_source_0.set_params(438000000-self.f_if-self.doppler, self.ad_samp_rate, self.channel_bw, True, True, True, "fast_attack", 64.0, "manual", 64.0, "A_BALANCED", '', True)

    def get_channel_bw(self):
        return self.channel_bw

    def set_channel_bw(self, channel_bw):
        self.channel_bw = channel_bw
        self.iio_fmcomms2_source_0.set_params(438000000-self.f_if-self.doppler, self.ad_samp_rate, self.channel_bw, True, True, True, "fast_attack", 64.0, "manual", 64.0, "A_BALANCED", '', True)

    def get_ad_samp_rate(self):
        return self.ad_samp_rate

    def set_ad_samp_rate(self, ad_samp_rate):
        self.ad_samp_rate = ad_samp_rate
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.ad_samp_rate)
        self.iio_fmcomms2_source_0.set_params(438000000-self.f_if-self.doppler, self.ad_samp_rate, self.channel_bw, True, True, True, "fast_attack", 64.0, "manual", 64.0, "A_BALANCED", '', True)


def main(top_block_cls=Recorder_beacon, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
