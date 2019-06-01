#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Telecommand Rx
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
from gnuradio import analog
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
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


class telecommand_rx(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Telecommand Rx")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Telecommand Rx")
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

        self.settings = Qt.QSettings("GNU Radio", "telecommand_rx")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.ss_ted_gain_range = ss_ted_gain_range = 100
        self.ss_loopbw_range = ss_loopbw_range = 0.25
        self.ss_damping_factor_range = ss_damping_factor_range = 0.5
        self.samp_per_symb = samp_per_symb = 10
        self.pll_loopbw_range = pll_loopbw_range = 0.4
        self.lpf_dec = lpf_dec = 8
        self.f_if = f_if = 30000
        self.doppler = doppler = 0
        self.bit_rate = bit_rate = 12019
        self.ad9361_lo_freq = ad9361_lo_freq = 144100000

        ##################################################
        # Blocks
        ##################################################
        self.tab = Qt.QTabWidget()
        self.tab_widget_0 = Qt.QWidget()
        self.tab_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_0)
        self.tab_grid_layout_0 = Qt.QGridLayout()
        self.tab_layout_0.addLayout(self.tab_grid_layout_0)
        self.tab.addTab(self.tab_widget_0, 'Tab 0')
        self.tab_widget_1 = Qt.QWidget()
        self.tab_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_1)
        self.tab_grid_layout_1 = Qt.QGridLayout()
        self.tab_layout_1.addLayout(self.tab_grid_layout_1)
        self.tab.addTab(self.tab_widget_1, 'Tab 1')
        self.tab_widget_2 = Qt.QWidget()
        self.tab_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_2)
        self.tab_grid_layout_2 = Qt.QGridLayout()
        self.tab_layout_2.addLayout(self.tab_grid_layout_2)
        self.tab.addTab(self.tab_widget_2, 'Tab 2')
        self.tab_widget_3 = Qt.QWidget()
        self.tab_layout_3 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_3)
        self.tab_grid_layout_3 = Qt.QGridLayout()
        self.tab_layout_3.addLayout(self.tab_grid_layout_3)
        self.tab.addTab(self.tab_widget_3, 'Tab 3')
        self.tab_widget_4 = Qt.QWidget()
        self.tab_layout_4 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_4)
        self.tab_grid_layout_4 = Qt.QGridLayout()
        self.tab_layout_4.addLayout(self.tab_grid_layout_4)
        self.tab.addTab(self.tab_widget_4, 'Tab 4')
        self.top_grid_layout.addWidget(self.tab)
        self._ss_ted_gain_range_range = Range(1, 1000, 1, 100, 10000)
        self._ss_ted_gain_range_win = RangeWidget(self._ss_ted_gain_range_range, self.set_ss_ted_gain_range, 'Symbol Sync TED gain', "slider", float)
        self.tab_grid_layout_0.addWidget(self._ss_ted_gain_range_win)
        self._ss_loopbw_range_range = Range(0.001, 2, 0.001, 0.25, 10000)
        self._ss_loopbw_range_win = RangeWidget(self._ss_loopbw_range_range, self.set_ss_loopbw_range, 'Symbol Sync LBW', "slider", float)
        self.tab_grid_layout_0.addWidget(self._ss_loopbw_range_win)
        self._ss_damping_factor_range_range = Range(0.001, 2, 0.001, 0.5, 10000)
        self._ss_damping_factor_range_win = RangeWidget(self._ss_damping_factor_range_range, self.set_ss_damping_factor_range, 'Symbol Sync DF', "slider", float)
        self.tab_grid_layout_0.addWidget(self._ss_damping_factor_range_win)
        self._pll_loopbw_range_range = Range(0.001, 2, 0.001, 0.4, 10000)
        self._pll_loopbw_range_win = RangeWidget(self._pll_loopbw_range_range, self.set_pll_loopbw_range, 'PLL LBW', "slider", float)
        self.tab_grid_layout_0.addWidget(self._pll_loopbw_range_win)
        self._f_if_tool_bar = Qt.QToolBar(self)
        self._f_if_tool_bar.addWidget(Qt.QLabel('IF Frequency'+": "))
        self._f_if_line_edit = Qt.QLineEdit(str(self.f_if))
        self._f_if_tool_bar.addWidget(self._f_if_line_edit)
        self._f_if_line_edit.returnPressed.connect(
        	lambda: self.set_f_if(int(str(self._f_if_line_edit.text().toAscii()))))
        self.tab_grid_layout_0.addWidget(self._f_if_tool_bar)
        self._doppler_tool_bar = Qt.QToolBar(self)
        self._doppler_tool_bar.addWidget(Qt.QLabel('Doppler'+": "))
        self._doppler_line_edit = Qt.QLineEdit(str(self.doppler))
        self._doppler_tool_bar.addWidget(self._doppler_line_edit)
        self._doppler_line_edit.returnPressed.connect(
        	lambda: self.set_doppler(int(str(self._doppler_line_edit.text().toAscii()))))
        self.tab_grid_layout_0.addWidget(self._doppler_tool_bar)
        self._ad9361_lo_freq_tool_bar = Qt.QToolBar(self)
        self._ad9361_lo_freq_tool_bar.addWidget(Qt.QLabel('AD9361 LO Frequency'+": "))
        self._ad9361_lo_freq_line_edit = Qt.QLineEdit(str(self.ad9361_lo_freq))
        self._ad9361_lo_freq_tool_bar.addWidget(self._ad9361_lo_freq_line_edit)
        self._ad9361_lo_freq_line_edit.returnPressed.connect(
        	lambda: self.set_ad9361_lo_freq(int(str(self._ad9361_lo_freq_line_edit.text().toAscii()))))
        self.tab_grid_layout_0.addWidget(self._ad9361_lo_freq_tool_bar)
        self.root_raised_cosine_filter_0 = filter.fir_filter_fff(1, firdes.root_raised_cosine(
        	1, bit_rate*samp_per_symb, bit_rate, 0.7, 1000))
        self.qtgui_time_sink_x_0_0_0_0 = qtgui.time_sink_f(
        	1024, #size
        	bit_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0_0_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_0_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0_0_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0_0_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_0_0.enable_control_panel(True)
        self.qtgui_time_sink_x_0_0_0_0.enable_stem_plot(False)

        if not False:
          self.qtgui_time_sink_x_0_0_0_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [2, 2, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_0_0.pyqwidget(), Qt.QWidget)
        self.tab_grid_layout_4.addWidget(self._qtgui_time_sink_x_0_0_0_0_win)
        self.qtgui_time_sink_x_0_0_0 = qtgui.time_sink_f(
        	1024, #size
        	bit_rate*samp_per_symb, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_0.enable_control_panel(True)
        self.qtgui_time_sink_x_0_0_0.enable_stem_plot(False)

        if not False:
          self.qtgui_time_sink_x_0_0_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [2, 2, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_0.pyqwidget(), Qt.QWidget)
        self.tab_grid_layout_3.addWidget(self._qtgui_time_sink_x_0_0_0_win)
        self.qtgui_time_sink_x_0_0 = qtgui.time_sink_f(
        	1024, #size
        	bit_rate*samp_per_symb, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0.enable_autoscale(True)
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
        markers = [2, 2, -1, -1, -1,
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
        self.tab_grid_layout_2.addWidget(self._qtgui_time_sink_x_0_0_win)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_c(
        	1024, #size
        	bit_rate*samp_per_symb, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(True)
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
        markers = [2, 2, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(2):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.tab_grid_layout_1.addWidget(self._qtgui_time_sink_x_0_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	bit_rate*samp_per_symb, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(True)
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
        self.tab_grid_layout_1.addWidget(self._qtgui_freq_sink_x_0_win)
        self.low_pass_filter_0 = filter.fir_filter_ccf(lpf_dec, firdes.low_pass(
        	1, bit_rate*samp_per_symb*lpf_dec, bit_rate*samp_per_symb/2, bit_rate*samp_per_symb/20, firdes.WIN_HAMMING, 6.76))
        self.iio_fmcomms2_source_0 = iio.fmcomms2_source_f32c('192.168.1.10', ad9361_lo_freq-(f_if+doppler), bit_rate*samp_per_symb*lpf_dec, 1000000, False, True, 0x8000, True, True, True, "manual", 64.0, "fast_attack", 64.0, "A_BALANCED", '', True)
        self.digital_symbol_sync_xx_0 = digital.symbol_sync_ff(digital.TED_GARDNER, samp_per_symb, ss_loopbw_range, ss_damping_factor_range, ss_ted_gain_range, 2, 1, digital.constellation_bpsk().base(), digital.IR_PFB_NO_MF, 128, ([]))
        self.dc_blocker_xx_0 = filter.dc_blocker_ff(60000, True)
        self.blocks_tag_gate_0 = blocks.tag_gate(gr.sizeof_gr_complex * 1, False)
        self.blocks_tag_gate_0.set_single_key("")
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((30, ))
        self.analog_pll_freqdet_cf_0 = analog.pll_freqdet_cf(pll_loopbw_range, 50000*6.28/(bit_rate*samp_per_symb), 0*6.28/(bit_rate*samp_per_symb))



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_pll_freqdet_cf_0, 0), (self.dc_blocker_xx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.root_raised_cosine_filter_0, 0))
        self.connect((self.blocks_tag_gate_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.dc_blocker_xx_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.dc_blocker_xx_0, 0), (self.qtgui_time_sink_x_0_0, 0))
        self.connect((self.digital_symbol_sync_xx_0, 0), (self.qtgui_time_sink_x_0_0_0_0, 0))
        self.connect((self.iio_fmcomms2_source_0, 0), (self.blocks_tag_gate_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.analog_pll_freqdet_cf_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.root_raised_cosine_filter_0, 0), (self.digital_symbol_sync_xx_0, 0))
        self.connect((self.root_raised_cosine_filter_0, 0), (self.qtgui_time_sink_x_0_0_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "telecommand_rx")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

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

    def get_samp_per_symb(self):
        return self.samp_per_symb

    def set_samp_per_symb(self, samp_per_symb):
        self.samp_per_symb = samp_per_symb
        self.root_raised_cosine_filter_0.set_taps(firdes.root_raised_cosine(1, self.bit_rate*self.samp_per_symb, self.bit_rate, 0.7, 1000))
        self.qtgui_time_sink_x_0_0_0.set_samp_rate(self.bit_rate*self.samp_per_symb)
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.bit_rate*self.samp_per_symb)
        self.qtgui_time_sink_x_0.set_samp_rate(self.bit_rate*self.samp_per_symb)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.bit_rate*self.samp_per_symb)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.bit_rate*self.samp_per_symb*self.lpf_dec, self.bit_rate*self.samp_per_symb/2, self.bit_rate*self.samp_per_symb/20, firdes.WIN_HAMMING, 6.76))
        self.iio_fmcomms2_source_0.set_params(self.ad9361_lo_freq-(self.f_if+self.doppler), self.bit_rate*self.samp_per_symb*self.lpf_dec, 1000000, True, True, True, "manual", 64.0, "fast_attack", 64.0, "A_BALANCED", '', True)
        self.analog_pll_freqdet_cf_0.set_max_freq(50000*6.28/(self.bit_rate*self.samp_per_symb))
        self.analog_pll_freqdet_cf_0.set_min_freq(0*6.28/(self.bit_rate*self.samp_per_symb))

    def get_pll_loopbw_range(self):
        return self.pll_loopbw_range

    def set_pll_loopbw_range(self, pll_loopbw_range):
        self.pll_loopbw_range = pll_loopbw_range
        self.analog_pll_freqdet_cf_0.set_loop_bandwidth(self.pll_loopbw_range)

    def get_lpf_dec(self):
        return self.lpf_dec

    def set_lpf_dec(self, lpf_dec):
        self.lpf_dec = lpf_dec
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.bit_rate*self.samp_per_symb*self.lpf_dec, self.bit_rate*self.samp_per_symb/2, self.bit_rate*self.samp_per_symb/20, firdes.WIN_HAMMING, 6.76))
        self.iio_fmcomms2_source_0.set_params(self.ad9361_lo_freq-(self.f_if+self.doppler), self.bit_rate*self.samp_per_symb*self.lpf_dec, 1000000, True, True, True, "manual", 64.0, "fast_attack", 64.0, "A_BALANCED", '', True)

    def get_f_if(self):
        return self.f_if

    def set_f_if(self, f_if):
        self.f_if = f_if
        Qt.QMetaObject.invokeMethod(self._f_if_line_edit, "setText", Qt.Q_ARG("QString", str(self.f_if)))
        self.iio_fmcomms2_source_0.set_params(self.ad9361_lo_freq-(self.f_if+self.doppler), self.bit_rate*self.samp_per_symb*self.lpf_dec, 1000000, True, True, True, "manual", 64.0, "fast_attack", 64.0, "A_BALANCED", '', True)

    def get_doppler(self):
        return self.doppler

    def set_doppler(self, doppler):
        self.doppler = doppler
        Qt.QMetaObject.invokeMethod(self._doppler_line_edit, "setText", Qt.Q_ARG("QString", str(self.doppler)))
        self.iio_fmcomms2_source_0.set_params(self.ad9361_lo_freq-(self.f_if+self.doppler), self.bit_rate*self.samp_per_symb*self.lpf_dec, 1000000, True, True, True, "manual", 64.0, "fast_attack", 64.0, "A_BALANCED", '', True)

    def get_bit_rate(self):
        return self.bit_rate

    def set_bit_rate(self, bit_rate):
        self.bit_rate = bit_rate
        self.root_raised_cosine_filter_0.set_taps(firdes.root_raised_cosine(1, self.bit_rate*self.samp_per_symb, self.bit_rate, 0.7, 1000))
        self.qtgui_time_sink_x_0_0_0_0.set_samp_rate(self.bit_rate)
        self.qtgui_time_sink_x_0_0_0.set_samp_rate(self.bit_rate*self.samp_per_symb)
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.bit_rate*self.samp_per_symb)
        self.qtgui_time_sink_x_0.set_samp_rate(self.bit_rate*self.samp_per_symb)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.bit_rate*self.samp_per_symb)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.bit_rate*self.samp_per_symb*self.lpf_dec, self.bit_rate*self.samp_per_symb/2, self.bit_rate*self.samp_per_symb/20, firdes.WIN_HAMMING, 6.76))
        self.iio_fmcomms2_source_0.set_params(self.ad9361_lo_freq-(self.f_if+self.doppler), self.bit_rate*self.samp_per_symb*self.lpf_dec, 1000000, True, True, True, "manual", 64.0, "fast_attack", 64.0, "A_BALANCED", '', True)
        self.analog_pll_freqdet_cf_0.set_max_freq(50000*6.28/(self.bit_rate*self.samp_per_symb))
        self.analog_pll_freqdet_cf_0.set_min_freq(0*6.28/(self.bit_rate*self.samp_per_symb))

    def get_ad9361_lo_freq(self):
        return self.ad9361_lo_freq

    def set_ad9361_lo_freq(self, ad9361_lo_freq):
        self.ad9361_lo_freq = ad9361_lo_freq
        Qt.QMetaObject.invokeMethod(self._ad9361_lo_freq_line_edit, "setText", Qt.Q_ARG("QString", str(self.ad9361_lo_freq)))
        self.iio_fmcomms2_source_0.set_params(self.ad9361_lo_freq-(self.f_if+self.doppler), self.bit_rate*self.samp_per_symb*self.lpf_dec, 1000000, True, True, True, "manual", 64.0, "fast_attack", 64.0, "A_BALANCED", '', True)


def main(top_block_cls=telecommand_rx, options=None):

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
