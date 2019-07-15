#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Telemetry Rx Final
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
from PyQt4.QtCore import QObject, pyqtSlot
from gnuradio import analog
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import fec
from gnuradio import filter
from gnuradio import gr
from gnuradio import iio
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import crypto
import iustsat
import pmt
import satellites
import sip
import sys
from gnuradio import qtgui


class telemetry_rx_final(gr.top_block, Qt.QWidget):

    def __init__(self, MTU=1500):
        gr.top_block.__init__(self, "Telemetry Rx Final")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Telemetry Rx Final")
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

        self.settings = Qt.QSettings("GNU Radio", "telemetry_rx_final")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Parameters
        ##################################################
        self.MTU = MTU

        ##################################################
        # Variables
        ##################################################
        self.symb_rate = symb_rate = 44643
        self.sec_dec = sec_dec = 10
        self.samp_per_symb = samp_per_symb = 10
        self.rate = rate = 2
        self.polys = polys = [109, 79]
        self.k = k = 7
        self.first_dec = first_dec = 1
        self.ss_ted_gain_range = ss_ted_gain_range = 100
        self.ss_loopbw_range = ss_loopbw_range = 0.4
        self.ss_damping_factor_range = ss_damping_factor_range = 0.5
        self.source_option = source_option = False
        self.pll_loopbw_range = pll_loopbw_range = 0.4
        self.doppler = doppler = 10000


        self.dec_cc = dec_cc = fec.cc_decoder.make(MTU*8, k, rate, (polys), 0, -1, fec.CC_TERMINATED, False)

        self.channel_bw = channel_bw = 1200000
        self.ad_samp_rate = ad_samp_rate = symb_rate*first_dec*sec_dec*samp_per_symb

        ##################################################
        # Blocks
        ##################################################
        self.tab = Qt.QTabWidget()
        self.tab_widget_0 = Qt.QWidget()
        self.tab_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_0)
        self.tab_grid_layout_0 = Qt.QGridLayout()
        self.tab_layout_0.addLayout(self.tab_grid_layout_0)
        self.tab.addTab(self.tab_widget_0, 'Frequency Plot')
        self.tab_widget_1 = Qt.QWidget()
        self.tab_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_1)
        self.tab_grid_layout_1 = Qt.QGridLayout()
        self.tab_layout_1.addLayout(self.tab_grid_layout_1)
        self.tab.addTab(self.tab_widget_1, 'Control Tab')
        self.tab_widget_2 = Qt.QWidget()
        self.tab_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_2)
        self.tab_grid_layout_2 = Qt.QGridLayout()
        self.tab_layout_2.addLayout(self.tab_grid_layout_2)
        self.tab.addTab(self.tab_widget_2, 'Time')
        self.tab_widget_3 = Qt.QWidget()
        self.tab_layout_3 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_3)
        self.tab_grid_layout_3 = Qt.QGridLayout()
        self.tab_layout_3.addLayout(self.tab_grid_layout_3)
        self.tab.addTab(self.tab_widget_3, 'Demoded Bits')
        self.tab_widget_4 = Qt.QWidget()
        self.tab_layout_4 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_4)
        self.tab_grid_layout_4 = Qt.QGridLayout()
        self.tab_layout_4.addLayout(self.tab_grid_layout_4)
        self.tab.addTab(self.tab_widget_4, 'Decoded Data')
        self.tab_widget_5 = Qt.QWidget()
        self.tab_layout_5 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_5)
        self.tab_grid_layout_5 = Qt.QGridLayout()
        self.tab_layout_5.addLayout(self.tab_grid_layout_5)
        self.tab.addTab(self.tab_widget_5, 'Decrypted Data')
        self.top_grid_layout.addWidget(self.tab, 0, 0, 4, 4)
        for r in range(0, 4):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._ss_ted_gain_range_range = Range(1, 1000, 1, 100, 10000)
        self._ss_ted_gain_range_win = RangeWidget(self._ss_ted_gain_range_range, self.set_ss_ted_gain_range, 'Symbol Sync TED gain', "dial", float)
        self.tab_grid_layout_1.addWidget(self._ss_ted_gain_range_win, 1, 2, 1, 1)
        for r in range(1, 2):
            self.tab_grid_layout_1.setRowStretch(r, 1)
        for c in range(2, 3):
            self.tab_grid_layout_1.setColumnStretch(c, 1)
        self._ss_loopbw_range_range = Range(0.001, 2, 0.001, 0.4, 10000)
        self._ss_loopbw_range_win = RangeWidget(self._ss_loopbw_range_range, self.set_ss_loopbw_range, 'Symbol Sync LBW', "dial", float)
        self.tab_grid_layout_1.addWidget(self._ss_loopbw_range_win, 1, 0, 1, 1)
        for r in range(1, 2):
            self.tab_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 1):
            self.tab_grid_layout_1.setColumnStretch(c, 1)
        self._ss_damping_factor_range_range = Range(0.001, 2, 0.001, 0.5, 10000)
        self._ss_damping_factor_range_win = RangeWidget(self._ss_damping_factor_range_range, self.set_ss_damping_factor_range, 'Symbol Sync DF', "dial", float)
        self.tab_grid_layout_1.addWidget(self._ss_damping_factor_range_win, 1, 1, 1, 1)
        for r in range(1, 2):
            self.tab_grid_layout_1.setRowStretch(r, 1)
        for c in range(1, 2):
            self.tab_grid_layout_1.setColumnStretch(c, 1)
        self._source_option_options = (True, False, )
        self._source_option_labels = ('AD9361', 'File', )
        self._source_option_group_box = Qt.QGroupBox('Source From')
        self._source_option_box = Qt.QHBoxLayout()
        class variable_chooser_button_group(Qt.QButtonGroup):
            def __init__(self, parent=None):
                Qt.QButtonGroup.__init__(self, parent)
            @pyqtSlot(int)
            def updateButtonChecked(self, button_id):
                self.button(button_id).setChecked(True)
        self._source_option_button_group = variable_chooser_button_group()
        self._source_option_group_box.setLayout(self._source_option_box)
        for i, label in enumerate(self._source_option_labels):
        	radio_button = Qt.QRadioButton(label)
        	self._source_option_box.addWidget(radio_button)
        	self._source_option_button_group.addButton(radio_button, i)
        self._source_option_callback = lambda i: Qt.QMetaObject.invokeMethod(self._source_option_button_group, "updateButtonChecked", Qt.Q_ARG("int", self._source_option_options.index(i)))
        self._source_option_callback(self.source_option)
        self._source_option_button_group.buttonClicked[int].connect(
        	lambda i: self.set_source_option(self._source_option_options[i]))
        self.tab_grid_layout_1.addWidget(self._source_option_group_box, 2, 0, 1, 1)
        for r in range(2, 3):
            self.tab_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 1):
            self.tab_grid_layout_1.setColumnStretch(c, 1)
        self._pll_loopbw_range_range = Range(0.001, 2, 0.001, 0.4, 10000)
        self._pll_loopbw_range_win = RangeWidget(self._pll_loopbw_range_range, self.set_pll_loopbw_range, 'PLL LBW', "dial", float)
        self.tab_grid_layout_1.addWidget(self._pll_loopbw_range_win, 0, 0, 1, 1)
        for r in range(0, 1):
            self.tab_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 1):
            self.tab_grid_layout_1.setColumnStretch(c, 1)
        self._doppler_range = Range(-50000, 50000, 1, 10000, 10000)
        self._doppler_win = RangeWidget(self._doppler_range, self.set_doppler, 'Doppler', "dial", int)
        self.tab_grid_layout_1.addWidget(self._doppler_win, 0, 1, 1, 1)
        for r in range(0, 1):
            self.tab_grid_layout_1.setRowStretch(r, 1)
        for c in range(1, 2):
            self.tab_grid_layout_1.setColumnStretch(c, 1)
        self.satellites_decode_rs_general_0 = satellites.decode_rs_general(285, 0, 1, 32, False, True)
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=first_dec,
                taps=None,
                fractional_bw=None,
        )
        self.qtgui_waterfall_sink_x_0 = qtgui.waterfall_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	ad_samp_rate/first_dec, #bw
        	"", #name
                1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_0.enable_grid(True)
        self.qtgui_waterfall_sink_x_0.enable_axis_labels(True)

        if not False:
          self.qtgui_waterfall_sink_x_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_waterfall_sink_x_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0.set_intensity_range(-140, 10)

        self._qtgui_waterfall_sink_x_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0.pyqwidget(), Qt.QWidget)
        self.tab_grid_layout_0.addWidget(self._qtgui_waterfall_sink_x_0_win, 2, 0, 2, 4)
        for r in range(2, 4):
            self.tab_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 4):
            self.tab_grid_layout_0.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0_0_0_0_1_0_0 = qtgui.time_sink_f(
        	203, #size
        	1, #samp_rate
        	"GCM-AES Decryptor Out", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_0_0_1_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0_0_0_1_0_0.set_y_axis(-10, 300)

        self.qtgui_time_sink_x_0_0_0_0_1_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0_0_0_1_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0_0_0_1_0_0.set_trigger_mode(qtgui.TRIG_MODE_TAG, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "frm_len")
        self.qtgui_time_sink_x_0_0_0_0_1_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0_0_0_1_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0_0_0_1_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_0_0_1_0_0.enable_control_panel(True)
        self.qtgui_time_sink_x_0_0_0_0_1_0_0.enable_stem_plot(False)

        if not False:
          self.qtgui_time_sink_x_0_0_0_0_1_0_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [2, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0_0_0_1_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0_0_0_1_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_0_0_1_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_0_0_1_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_0_0_1_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_0_0_1_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_0_0_1_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_0_0_1_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_0_0_1_0_0.pyqwidget(), Qt.QWidget)
        self.tab_grid_layout_5.addWidget(self._qtgui_time_sink_x_0_0_0_0_1_0_0_win, 0, 0, 2, 4)
        for r in range(0, 2):
            self.tab_grid_layout_5.setRowStretch(r, 1)
        for c in range(0, 4):
            self.tab_grid_layout_5.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0_0_0_0_1_0 = qtgui.time_sink_f(
        	255, #size
        	1, #samp_rate
        	"Viterbi Decoder Out", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_0_0_1_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0_0_0_1_0.set_y_axis(-10, 300)

        self.qtgui_time_sink_x_0_0_0_0_1_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0_0_0_1_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0_0_0_1_0.set_trigger_mode(qtgui.TRIG_MODE_TAG, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "pkt_len")
        self.qtgui_time_sink_x_0_0_0_0_1_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0_0_0_1_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0_0_0_1_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_0_0_1_0.enable_control_panel(True)
        self.qtgui_time_sink_x_0_0_0_0_1_0.enable_stem_plot(False)

        if not False:
          self.qtgui_time_sink_x_0_0_0_0_1_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [2, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0_0_0_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0_0_0_1_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_0_0_1_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_0_0_1_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_0_0_1_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_0_0_1_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_0_0_1_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_0_0_1_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_0_0_1_0.pyqwidget(), Qt.QWidget)
        self.tab_grid_layout_4.addWidget(self._qtgui_time_sink_x_0_0_0_0_1_0_win, 0, 0, 2, 4)
        for r in range(0, 2):
            self.tab_grid_layout_4.setRowStretch(r, 1)
        for c in range(0, 4):
            self.tab_grid_layout_4.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0_0_0_0_1 = qtgui.time_sink_f(
        	223, #size
        	1, #samp_rate
        	"Reed-Solomon Decoder Out", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_0_0_1.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0_0_0_1.set_y_axis(-10, 300)

        self.qtgui_time_sink_x_0_0_0_0_1.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0_0_0_1.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0_0_0_1.set_trigger_mode(qtgui.TRIG_MODE_TAG, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "pkt_len")
        self.qtgui_time_sink_x_0_0_0_0_1.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0_0_0_1.enable_grid(False)
        self.qtgui_time_sink_x_0_0_0_0_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_0_0_1.enable_control_panel(True)
        self.qtgui_time_sink_x_0_0_0_0_1.enable_stem_plot(False)

        if not False:
          self.qtgui_time_sink_x_0_0_0_0_1.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [2, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0_0_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0_0_0_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_0_0_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_0_0_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_0_0_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_0_0_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_0_0_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_0_0_1_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_0_0_1.pyqwidget(), Qt.QWidget)
        self.tab_grid_layout_4.addWidget(self._qtgui_time_sink_x_0_0_0_0_1_win, 2, 0, 2, 4)
        for r in range(2, 4):
            self.tab_grid_layout_4.setRowStretch(r, 1)
        for c in range(0, 4):
            self.tab_grid_layout_4.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0_0_0_0_0 = qtgui.time_sink_f(
        	4144, #size
        	ad_samp_rate/first_dec/sec_dec/samp_per_symb, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_0_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0_0_0_0.set_y_axis(-1, 2)

        self.qtgui_time_sink_x_0_0_0_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0_0_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_TAG, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "pkt_len")
        self.qtgui_time_sink_x_0_0_0_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0_0_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0_0_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_0_0_0.enable_control_panel(True)
        self.qtgui_time_sink_x_0_0_0_0_0.enable_stem_plot(False)

        if not False:
          self.qtgui_time_sink_x_0_0_0_0_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [2, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_0_0_0.pyqwidget(), Qt.QWidget)
        self.tab_grid_layout_3.addWidget(self._qtgui_time_sink_x_0_0_0_0_0_win, 2, 0, 2, 4)
        for r in range(2, 4):
            self.tab_grid_layout_3.setRowStretch(r, 1)
        for c in range(0, 4):
            self.tab_grid_layout_3.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0_0 = qtgui.time_sink_f(
        	1024, #size
        	ad_samp_rate/first_dec/sec_dec/samp_per_symb, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0.set_y_axis(-20, 20)

        self.qtgui_time_sink_x_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0.enable_control_panel(True)
        self.qtgui_time_sink_x_0_0.enable_stem_plot(False)

        if not False:
          self.qtgui_time_sink_x_0_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [2, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.tab_grid_layout_3.addWidget(self._qtgui_time_sink_x_0_0_win, 0, 0, 2, 2)
        for r in range(0, 2):
            self.tab_grid_layout_3.setRowStretch(r, 1)
        for c in range(0, 2):
            self.tab_grid_layout_3.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	1024, #size
        	ad_samp_rate/first_dec/sec_dec, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-20, 20)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(True)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)

        if not False:
          self.qtgui_time_sink_x_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [2, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.tab_grid_layout_2.addWidget(self._qtgui_time_sink_x_0_win)
        self.qtgui_number_sink_0_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_NONE,
            1
        )
        self.qtgui_number_sink_0_0.set_update_time(0.10)
        self.qtgui_number_sink_0_0.set_title("Decrypted Frame Counter")

        labels = ['Counter', 'Rate', '', '', '',
                  '', '', '', '', '']
        units = ['', '', '', '', '',
                 '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.qtgui_number_sink_0_0.set_min(i, -1)
            self.qtgui_number_sink_0_0.set_max(i, 1)
            self.qtgui_number_sink_0_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0_0.set_label(i, labels[i])
            self.qtgui_number_sink_0_0.set_unit(i, units[i])
            self.qtgui_number_sink_0_0.set_factor(i, factor[i])

        self.qtgui_number_sink_0_0.enable_autoscale(False)
        self._qtgui_number_sink_0_0_win = sip.wrapinstance(self.qtgui_number_sink_0_0.pyqwidget(), Qt.QWidget)
        self.tab_grid_layout_3.addWidget(self._qtgui_number_sink_0_0_win, 0, 3, 2, 1)
        for r in range(0, 2):
            self.tab_grid_layout_3.setRowStretch(r, 1)
        for c in range(3, 4):
            self.tab_grid_layout_3.setColumnStretch(c, 1)
        self.qtgui_number_sink_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_NONE,
            2
        )
        self.qtgui_number_sink_0.set_update_time(0.10)
        self.qtgui_number_sink_0.set_title("Received Frame Counter")

        labels = ['Counter', 'Rate', '', '', '',
                  '', '', '', '', '']
        units = ['', '', '', '', '',
                 '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(2):
            self.qtgui_number_sink_0.set_min(i, -1)
            self.qtgui_number_sink_0.set_max(i, 1)
            self.qtgui_number_sink_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0.set_label(i, labels[i])
            self.qtgui_number_sink_0.set_unit(i, units[i])
            self.qtgui_number_sink_0.set_factor(i, factor[i])

        self.qtgui_number_sink_0.enable_autoscale(False)
        self._qtgui_number_sink_0_win = sip.wrapinstance(self.qtgui_number_sink_0.pyqwidget(), Qt.QWidget)
        self.tab_grid_layout_3.addWidget(self._qtgui_number_sink_0_win, 0, 2, 2, 1)
        for r in range(0, 2):
            self.tab_grid_layout_3.setRowStretch(r, 1)
        for c in range(2, 3):
            self.tab_grid_layout_3.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	ad_samp_rate/first_dec, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-160, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)

        if not False:
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
        self.tab_grid_layout_0.addWidget(self._qtgui_freq_sink_x_0_win, 0, 0, 2, 4)
        for r in range(0, 2):
            self.tab_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 4):
            self.tab_grid_layout_0.setColumnStretch(c, 1)
        self.low_pass_filter_0 = filter.fir_filter_ccf(sec_dec, firdes.low_pass(
        	1, ad_samp_rate/first_dec, channel_bw, channel_bw/10, firdes.WIN_HAMMING, 6.76))
        self.iustsat_zafar_telemetry_frame_extractor_1 = iustsat.zafar_telemetry_frame_extractor("pkt_len")
        self.iustsat_zafar_telemetry_derand_0 = iustsat.zafar_telemetry_derand("pkt_len")
        self.iustsat_tag_counter_0 = iustsat.tag_counter('pkt_len')
        self.iustsat_synch_detect_tag_1_0 = iustsat.synch_detect_tag(60,'pkt_len',259*2*8)
        self.iustsat_synch_detect_tag_1 = iustsat.synch_detect_tag(60,'pkt_len',259*2*8)
        self.iustsat_rs_to_decrypt_0_0 = iustsat.rs_to_decrypt('iv', ([0xCA, 0xFE, 0xBA, 0xBE, 0xFA, 0xCE, 0xDB, 0xAD, 0xDE, 0xCA, 0xF8, 0x88]), 'aad', 'auth_tag')
        self.iustsat_pdu_to_message_0 = iustsat.pdu_to_message('frm_len')
        self.iustsat_frame_analysis_0 = iustsat.frame_analysis('frm_len')
        self.iio_fmcomms2_source_0 = iio.fmcomms2_source_f32c('192.168.1.10', 436500000+doppler, ad_samp_rate, channel_bw, True, False, 0x8000, True, True, True, "fast_attack", 64.0, "manual", 64.0, "A_BALANCED", '', True)
        self.fir_filter_xxx_0 = filter.fir_filter_fff(1, ([1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,-1,-1,1,1,-1,-1,-1,1,1,1,1,1,1,1,1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,1,1,-1,1,1,-1,-1,-1,-1,1,-1,1,1,1,-1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1]))
        self.fir_filter_xxx_0.declare_sample_delay(0)
        self.fec_async_decoder_0 = fec.async_decoder(dec_cc, True, False, MTU)
        self.digital_symbol_sync_xx_0 = digital.symbol_sync_ff(digital.TED_GARDNER, samp_per_symb, ss_loopbw_range, ss_damping_factor_range, ss_ted_gain_range, 1, 1, digital.constellation_bpsk().base(), digital.IR_PFB_NO_MF, 128, ([]))
        self.digital_binary_slicer_fb_0 = digital.binary_slicer_fb()
        self.dc_blocker_xx_0 = filter.dc_blocker_ff(100000, True)
        self.crypto_auth_dec_aes_gcm_0_0 = crypto.auth_dec_aes_gcm(([0xFE, 0xFF, 0xE9, 0x92, 0x86, 0x65, 0x73, 0x1C, 0x6D, 0x6A, 0x8F, 0x94, 0x67, 0x30, 0x83, 0x08]), 16, 96)
        self.blocks_uchar_to_float_1_0 = blocks.uchar_to_float()
        self.blocks_uchar_to_float_1 = blocks.uchar_to_float()
        self.blocks_uchar_to_float_0 = blocks.uchar_to_float()
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, ad_samp_rate,True)
        self.blocks_tag_gate_0 = blocks.tag_gate(gr.sizeof_gr_complex * 1, False)
        self.blocks_tag_gate_0.set_single_key("")
        self.blocks_pdu_to_tagged_stream_0_0_0_0 = blocks.pdu_to_tagged_stream(blocks.float_t, 'frm_len')
        self.blocks_pdu_to_tagged_stream_0_0_0 = blocks.pdu_to_tagged_stream(blocks.float_t, 'frm_len')
        self.blocks_pdu_to_tagged_stream_0_0 = blocks.pdu_to_tagged_stream(blocks.byte_t, 'pkt_len')
        self.blocks_pdu_to_tagged_stream_0 = blocks.pdu_to_tagged_stream(blocks.byte_t, 'pkt_len')
        self.blocks_multiply_const_vxx_2_0 = blocks.multiply_const_vcc((source_option, ))
        self.blocks_multiply_const_vxx_2 = blocks.multiply_const_vcc(((not source_option), ))
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_vff((0.066666667, ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((2, ))
        self.blocks_moving_average_xx_0 = blocks.moving_average_ff(samp_per_symb, 10, 4000, 1)
        self.blocks_message_debug_0_0 = blocks.message_debug()
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_gr_complex*1, '/home/iust/Documents/zafar_prj/gr-iustsat/examples/Records/REC7_GMSK.bin', True)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_delay_0_0 = blocks.delay(gr.sizeof_float*1, 63)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_float*1, 63)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.blocks_add_const_vxx_1 = blocks.add_const_vff((0, ))
        self.blocks_add_const_vxx_0 = blocks.add_const_vff((-1, ))
        self.analog_pll_freqdet_cf_0 = analog.pll_freqdet_cf(pll_loopbw_range, 700000*6.28/(ad_samp_rate/first_dec/sec_dec), 300000*6.28/(ad_samp_rate/first_dec/sec_dec))



        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.crypto_auth_dec_aes_gcm_0_0, 'pdus'), (self.iustsat_frame_analysis_0, 'in'))
        self.msg_connect((self.crypto_auth_dec_aes_gcm_0_0, 'pdus'), (self.iustsat_pdu_to_message_0, 'in'))
        self.msg_connect((self.fec_async_decoder_0, 'out'), (self.iustsat_zafar_telemetry_derand_0, 'in'))
        self.msg_connect((self.iustsat_frame_analysis_0, 'out'), (self.blocks_pdu_to_tagged_stream_0_0_0, 'pdus'))
        self.msg_connect((self.iustsat_pdu_to_message_0, 'out'), (self.blocks_pdu_to_tagged_stream_0_0_0_0, 'pdus'))
        self.msg_connect((self.iustsat_rs_to_decrypt_0_0, 'out'), (self.crypto_auth_dec_aes_gcm_0_0, 'pdus'))
        self.msg_connect((self.iustsat_zafar_telemetry_derand_0, 'out'), (self.blocks_pdu_to_tagged_stream_0_0, 'pdus'))
        self.msg_connect((self.iustsat_zafar_telemetry_derand_0, 'out'), (self.satellites_decode_rs_general_0, 'in'))
        self.msg_connect((self.iustsat_zafar_telemetry_frame_extractor_1, 'out'), (self.fec_async_decoder_0, 'in'))
        self.msg_connect((self.satellites_decode_rs_general_0, 'out'), (self.blocks_message_debug_0_0, 'print_pdu'))
        self.msg_connect((self.satellites_decode_rs_general_0, 'out'), (self.blocks_pdu_to_tagged_stream_0, 'pdus'))
        self.msg_connect((self.satellites_decode_rs_general_0, 'out'), (self.iustsat_rs_to_decrypt_0_0, 'in'))
        self.connect((self.analog_pll_freqdet_cf_0, 0), (self.dc_blocker_xx_0, 0))
        self.connect((self.blocks_add_const_vxx_0, 0), (self.fir_filter_xxx_0, 0))
        self.connect((self.blocks_add_const_vxx_1, 0), (self.digital_symbol_sync_xx_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.blocks_delay_0, 0), (self.iustsat_synch_detect_tag_1, 0))
        self.connect((self.blocks_delay_0_0, 0), (self.iustsat_synch_detect_tag_1_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_moving_average_xx_0, 0), (self.blocks_add_const_vxx_1, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_add_const_vxx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.blocks_delay_0, 0))
        self.connect((self.blocks_multiply_const_vxx_2, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_multiply_const_vxx_2_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_pdu_to_tagged_stream_0, 0), (self.blocks_uchar_to_float_1, 0))
        self.connect((self.blocks_pdu_to_tagged_stream_0_0, 0), (self.blocks_uchar_to_float_1_0, 0))
        self.connect((self.blocks_pdu_to_tagged_stream_0_0_0, 0), (self.qtgui_number_sink_0_0, 0))
        self.connect((self.blocks_pdu_to_tagged_stream_0_0_0_0, 0), (self.qtgui_time_sink_x_0_0_0_0_1_0_0, 0))
        self.connect((self.blocks_tag_gate_0, 0), (self.blocks_multiply_const_vxx_2_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_multiply_const_vxx_2, 0))
        self.connect((self.blocks_uchar_to_float_0, 0), (self.blocks_delay_0_0, 0))
        self.connect((self.blocks_uchar_to_float_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_uchar_to_float_1, 0), (self.qtgui_time_sink_x_0_0_0_0_1, 0))
        self.connect((self.blocks_uchar_to_float_1_0, 0), (self.qtgui_time_sink_x_0_0_0_0_1_0, 0))
        self.connect((self.dc_blocker_xx_0, 0), (self.blocks_moving_average_xx_0, 0))
        self.connect((self.dc_blocker_xx_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.digital_binary_slicer_fb_0, 0), (self.blocks_uchar_to_float_0, 0))
        self.connect((self.digital_symbol_sync_xx_0, 0), (self.blocks_multiply_const_vxx_1, 0))
        self.connect((self.digital_symbol_sync_xx_0, 0), (self.digital_binary_slicer_fb_0, 0))
        self.connect((self.digital_symbol_sync_xx_0, 0), (self.qtgui_time_sink_x_0_0, 0))
        self.connect((self.fir_filter_xxx_0, 0), (self.iustsat_synch_detect_tag_1, 1))
        self.connect((self.fir_filter_xxx_0, 0), (self.iustsat_synch_detect_tag_1_0, 1))
        self.connect((self.iio_fmcomms2_source_0, 0), (self.blocks_tag_gate_0, 0))
        self.connect((self.iustsat_synch_detect_tag_1, 0), (self.iustsat_tag_counter_0, 0))
        self.connect((self.iustsat_synch_detect_tag_1, 0), (self.iustsat_zafar_telemetry_frame_extractor_1, 0))
        self.connect((self.iustsat_synch_detect_tag_1_0, 0), (self.qtgui_time_sink_x_0_0_0_0_0, 0))
        self.connect((self.iustsat_tag_counter_0, 0), (self.qtgui_number_sink_0, 0))
        self.connect((self.iustsat_tag_counter_0, 1), (self.qtgui_number_sink_0, 1))
        self.connect((self.low_pass_filter_0, 0), (self.analog_pll_freqdet_cf_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.qtgui_waterfall_sink_x_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "telemetry_rx_final")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_MTU(self):
        return self.MTU

    def set_MTU(self, MTU):
        self.MTU = MTU

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
        self.qtgui_time_sink_x_0_0_0_0_0.set_samp_rate(self.ad_samp_rate/self.first_dec/self.sec_dec/self.samp_per_symb)
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.ad_samp_rate/self.first_dec/self.sec_dec/self.samp_per_symb)
        self.qtgui_time_sink_x_0.set_samp_rate(self.ad_samp_rate/self.first_dec/self.sec_dec)
        self.analog_pll_freqdet_cf_0.set_max_freq(700000*6.28/(self.ad_samp_rate/self.first_dec/self.sec_dec))
        self.analog_pll_freqdet_cf_0.set_min_freq(300000*6.28/(self.ad_samp_rate/self.first_dec/self.sec_dec))

    def get_samp_per_symb(self):
        return self.samp_per_symb

    def set_samp_per_symb(self, samp_per_symb):
        self.samp_per_symb = samp_per_symb
        self.set_ad_samp_rate(self.symb_rate*self.first_dec*self.sec_dec*self.samp_per_symb)
        self.qtgui_time_sink_x_0_0_0_0_0.set_samp_rate(self.ad_samp_rate/self.first_dec/self.sec_dec/self.samp_per_symb)
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.ad_samp_rate/self.first_dec/self.sec_dec/self.samp_per_symb)
        self.blocks_moving_average_xx_0.set_length_and_scale(self.samp_per_symb, 10)

    def get_rate(self):
        return self.rate

    def set_rate(self, rate):
        self.rate = rate

    def get_polys(self):
        return self.polys

    def set_polys(self, polys):
        self.polys = polys

    def get_k(self):
        return self.k

    def set_k(self, k):
        self.k = k

    def get_first_dec(self):
        return self.first_dec

    def set_first_dec(self, first_dec):
        self.first_dec = first_dec
        self.set_ad_samp_rate(self.symb_rate*self.first_dec*self.sec_dec*self.samp_per_symb)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(0, self.ad_samp_rate/self.first_dec)
        self.qtgui_time_sink_x_0_0_0_0_0.set_samp_rate(self.ad_samp_rate/self.first_dec/self.sec_dec/self.samp_per_symb)
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.ad_samp_rate/self.first_dec/self.sec_dec/self.samp_per_symb)
        self.qtgui_time_sink_x_0.set_samp_rate(self.ad_samp_rate/self.first_dec/self.sec_dec)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.ad_samp_rate/self.first_dec)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.ad_samp_rate/self.first_dec, self.channel_bw, self.channel_bw/10, firdes.WIN_HAMMING, 6.76))
        self.analog_pll_freqdet_cf_0.set_max_freq(700000*6.28/(self.ad_samp_rate/self.first_dec/self.sec_dec))
        self.analog_pll_freqdet_cf_0.set_min_freq(300000*6.28/(self.ad_samp_rate/self.first_dec/self.sec_dec))

    def get_ss_ted_gain_range(self):
        return self.ss_ted_gain_range

    def set_ss_ted_gain_range(self, ss_ted_gain_range):
        self.ss_ted_gain_range = ss_ted_gain_range
        self.digital_symbol_sync_xx_0.set_ted_gain(self.ss_ted_gain_range)

    def get_ss_loopbw_range(self):
        return self.ss_loopbw_range

    def set_ss_loopbw_range(self, ss_loopbw_range):
        self.ss_loopbw_range = ss_loopbw_range
        self.digital_symbol_sync_xx_0.set_loop_bandwidth(self.ss_loopbw_range)

    def get_ss_damping_factor_range(self):
        return self.ss_damping_factor_range

    def set_ss_damping_factor_range(self, ss_damping_factor_range):
        self.ss_damping_factor_range = ss_damping_factor_range
        self.digital_symbol_sync_xx_0.set_damping_factor(self.ss_damping_factor_range)

    def get_source_option(self):
        return self.source_option

    def set_source_option(self, source_option):
        self.source_option = source_option
        self._source_option_callback(self.source_option)
        self.blocks_multiply_const_vxx_2_0.set_k((self.source_option, ))
        self.blocks_multiply_const_vxx_2.set_k(((not self.source_option), ))

    def get_pll_loopbw_range(self):
        return self.pll_loopbw_range

    def set_pll_loopbw_range(self, pll_loopbw_range):
        self.pll_loopbw_range = pll_loopbw_range
        self.analog_pll_freqdet_cf_0.set_loop_bandwidth(self.pll_loopbw_range)

    def get_doppler(self):
        return self.doppler

    def set_doppler(self, doppler):
        self.doppler = doppler
        self.iio_fmcomms2_source_0.set_params(436500000+self.doppler, self.ad_samp_rate, self.channel_bw, True, True, True, "fast_attack", 64.0, "manual", 64.0, "A_BALANCED", '', True)

    def get_dec_cc(self):
        return self.dec_cc

    def set_dec_cc(self, dec_cc):
        self.dec_cc = dec_cc

    def get_channel_bw(self):
        return self.channel_bw

    def set_channel_bw(self, channel_bw):
        self.channel_bw = channel_bw
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.ad_samp_rate/self.first_dec, self.channel_bw, self.channel_bw/10, firdes.WIN_HAMMING, 6.76))
        self.iio_fmcomms2_source_0.set_params(436500000+self.doppler, self.ad_samp_rate, self.channel_bw, True, True, True, "fast_attack", 64.0, "manual", 64.0, "A_BALANCED", '', True)

    def get_ad_samp_rate(self):
        return self.ad_samp_rate

    def set_ad_samp_rate(self, ad_samp_rate):
        self.ad_samp_rate = ad_samp_rate
        self.qtgui_waterfall_sink_x_0.set_frequency_range(0, self.ad_samp_rate/self.first_dec)
        self.qtgui_time_sink_x_0_0_0_0_0.set_samp_rate(self.ad_samp_rate/self.first_dec/self.sec_dec/self.samp_per_symb)
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.ad_samp_rate/self.first_dec/self.sec_dec/self.samp_per_symb)
        self.qtgui_time_sink_x_0.set_samp_rate(self.ad_samp_rate/self.first_dec/self.sec_dec)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.ad_samp_rate/self.first_dec)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.ad_samp_rate/self.first_dec, self.channel_bw, self.channel_bw/10, firdes.WIN_HAMMING, 6.76))
        self.iio_fmcomms2_source_0.set_params(436500000+self.doppler, self.ad_samp_rate, self.channel_bw, True, True, True, "fast_attack", 64.0, "manual", 64.0, "A_BALANCED", '', True)
        self.blocks_throttle_0.set_sample_rate(self.ad_samp_rate)
        self.analog_pll_freqdet_cf_0.set_max_freq(700000*6.28/(self.ad_samp_rate/self.first_dec/self.sec_dec))
        self.analog_pll_freqdet_cf_0.set_min_freq(300000*6.28/(self.ad_samp_rate/self.first_dec/self.sec_dec))


def argument_parser():
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option)
    parser.add_option(
        "", "--MTU", dest="MTU", type="intx", default=1500,
        help="Set MTU [default=%default]")
    return parser


def main(top_block_cls=telemetry_rx_final, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls(MTU=options.MTU)
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
