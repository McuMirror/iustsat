#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Telecommand Tx
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


class telecommand_tx(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Telecommand Tx")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Telecommand Tx")
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

        self.settings = Qt.QSettings("GNU Radio", "telecommand_tx")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.rrc_inter = rrc_inter = 10
        self.bit_rate = bit_rate = 12019
        self.tx_gain2 = tx_gain2 = 5
        self.tx_gain = tx_gain = 1
        self.fdev = fdev = bit_rate*rrc_inter/4
        self.data_src = data_src = (0,1)

        ##################################################
        # Blocks
        ##################################################
        self.tab_ctrl = Qt.QTabWidget()
        self.tab_ctrl_widget_0 = Qt.QWidget()
        self.tab_ctrl_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_ctrl_widget_0)
        self.tab_ctrl_grid_layout_0 = Qt.QGridLayout()
        self.tab_ctrl_layout_0.addLayout(self.tab_ctrl_grid_layout_0)
        self.tab_ctrl.addTab(self.tab_ctrl_widget_0, 'Control')
        self.top_grid_layout.addWidget(self.tab_ctrl, 0, 0, 4, 1)
        for r in range(0, 4):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._tx_gain2_range = Range(0.01, 10, 0.01, 5, 1000)
        self._tx_gain2_win = RangeWidget(self._tx_gain2_range, self.set_tx_gain2, 'TX Gain2', "counter_slider", float)
        self.tab_ctrl_grid_layout_0.addWidget(self._tx_gain2_win)
        self._tx_gain_range = Range(0.01, 10, 0.01, 1, 1000)
        self._tx_gain_win = RangeWidget(self._tx_gain_range, self.set_tx_gain, 'TX Gain', "counter_slider", float)
        self.tab_ctrl_grid_layout_0.addWidget(self._tx_gain_win)
        self.tab_plot = Qt.QTabWidget()
        self.tab_plot_widget_0 = Qt.QWidget()
        self.tab_plot_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_plot_widget_0)
        self.tab_plot_grid_layout_0 = Qt.QGridLayout()
        self.tab_plot_layout_0.addLayout(self.tab_plot_grid_layout_0)
        self.tab_plot.addTab(self.tab_plot_widget_0, 'Tab 0')
        self.tab_plot_widget_1 = Qt.QWidget()
        self.tab_plot_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_plot_widget_1)
        self.tab_plot_grid_layout_1 = Qt.QGridLayout()
        self.tab_plot_layout_1.addLayout(self.tab_plot_grid_layout_1)
        self.tab_plot.addTab(self.tab_plot_widget_1, 'Tab 1')
        self.tab_plot_widget_2 = Qt.QWidget()
        self.tab_plot_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_plot_widget_2)
        self.tab_plot_grid_layout_2 = Qt.QGridLayout()
        self.tab_plot_layout_2.addLayout(self.tab_plot_grid_layout_2)
        self.tab_plot.addTab(self.tab_plot_widget_2, 'Tab 2')
        self.tab_plot_widget_3 = Qt.QWidget()
        self.tab_plot_layout_3 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_plot_widget_3)
        self.tab_plot_grid_layout_3 = Qt.QGridLayout()
        self.tab_plot_layout_3.addLayout(self.tab_plot_grid_layout_3)
        self.tab_plot.addTab(self.tab_plot_widget_3, 'Tab 3')
        self.tab_plot_widget_4 = Qt.QWidget()
        self.tab_plot_layout_4 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_plot_widget_4)
        self.tab_plot_grid_layout_4 = Qt.QGridLayout()
        self.tab_plot_layout_4.addLayout(self.tab_plot_grid_layout_4)
        self.tab_plot.addTab(self.tab_plot_widget_4, 'Tab 4')
        self.top_grid_layout.addWidget(self.tab_plot, 0, 1, 4, 3)
        for r in range(0, 4):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._fdev_range = Range(100, 500000, 1, bit_rate*rrc_inter/4, 1000)
        self._fdev_win = RangeWidget(self._fdev_range, self.set_fdev, 'Frequency Deviation', "counter_slider", float)
        self.tab_ctrl_grid_layout_0.addWidget(self._fdev_win)
        self.root_raised_cosine_filter_0 = filter.interp_fir_filter_fff(rrc_inter, firdes.root_raised_cosine(
        	1, bit_rate*rrc_inter, bit_rate, 0.7, 1000))
        self.qtgui_time_sink_x_0_0_0 = qtgui.time_sink_c(
        	1000, #size
        	bit_rate*rrc_inter, #samp_rate
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

        for i in xrange(2):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_0_0_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0_0_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_0.pyqwidget(), Qt.QWidget)
        self.tab_plot_grid_layout_1.addWidget(self._qtgui_time_sink_x_0_0_0_win)
        self.qtgui_time_sink_x_0_0 = qtgui.time_sink_c(
        	1000*8, #size
        	bit_rate*rrc_inter*8, #samp_rate
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

        for i in xrange(2):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_0_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.tab_plot_grid_layout_2.addWidget(self._qtgui_time_sink_x_0_0_win)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	1000, #size
        	bit_rate*rrc_inter, #samp_rate
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
        self.tab_plot_grid_layout_0.addWidget(self._qtgui_time_sink_x_0_win)
        self.qtgui_freq_sink_x_0_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	bit_rate*rrc_inter*8, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_0.enable_grid(False)
        self.qtgui_freq_sink_x_0_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_0.enable_control_panel(False)

        if not False:
          self.qtgui_freq_sink_x_0_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0_0.set_plot_pos_half(not True)

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
                self.qtgui_freq_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.tab_plot_grid_layout_2.addWidget(self._qtgui_freq_sink_x_0_0_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	bit_rate*rrc_inter, #bw
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
        self.tab_plot_grid_layout_1.addWidget(self._qtgui_freq_sink_x_0_win)
        self.low_pass_filter_0 = filter.interp_fir_filter_ccf(8, firdes.low_pass(
        	1, bit_rate*rrc_inter*8, bit_rate*rrc_inter/2, bit_rate*rrc_inter/20, firdes.WIN_HAMMING, 6.76))
        self.iio_fmcomms2_sink_0 = iio.fmcomms2_sink_f32c('192.168.1.10', 144100000, bit_rate*rrc_inter*8, 100000, True, False, 0x8000, False, "A", 10, 10, '', True)
        self.digital_map_bb_0 = digital.map_bb(([-1,1]))
        self._data_src_options = ((1,0), (0,1), )
        self._data_src_labels = ('Source', 'Preamble', )
        self._data_src_tool_bar = Qt.QToolBar(self)
        self._data_src_tool_bar.addWidget(Qt.QLabel('Data Source'+": "))
        self._data_src_combo_box = Qt.QComboBox()
        self._data_src_tool_bar.addWidget(self._data_src_combo_box)
        for label in self._data_src_labels: self._data_src_combo_box.addItem(label)
        self._data_src_callback = lambda i: Qt.QMetaObject.invokeMethod(self._data_src_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._data_src_options.index(i)))
        self._data_src_callback(self.data_src)
        self._data_src_combo_box.currentIndexChanged.connect(
        	lambda i: self.set_data_src(self._data_src_options[i]))
        self.tab_ctrl_grid_layout_0.addWidget(self._data_src_tool_bar)
        self.blocks_vector_source_x_0_0 = blocks.vector_source_b([0x55, 0x55, 0x55, 0x55], True, 1, [])
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_char*1, bit_rate,True)
        self.blocks_repack_bits_bb_0 = blocks.repack_bits_bb(8, 1, "", False, gr.GR_MSB_FIRST)
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_vff((tx_gain, ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((tx_gain2, ))
        self.blocks_float_to_char_0 = blocks.float_to_char(1, 1)
        self.blocks_char_to_float_1_0 = blocks.char_to_float(1, 1)
        self.blocks_char_to_float_0 = blocks.char_to_float(1, 1)
        self.analog_frequency_modulator_fc_0 = analog.frequency_modulator_fc(fdev*6.28/(bit_rate*rrc_inter))



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_frequency_modulator_fc_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.analog_frequency_modulator_fc_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.analog_frequency_modulator_fc_0, 0), (self.qtgui_time_sink_x_0_0_0, 0))
        self.connect((self.blocks_char_to_float_0, 0), (self.root_raised_cosine_filter_0, 0))
        self.connect((self.blocks_char_to_float_1_0, 0), (self.blocks_float_to_char_0, 0))
        self.connect((self.blocks_float_to_char_0, 0), (self.blocks_repack_bits_bb_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.iio_fmcomms2_sink_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.qtgui_freq_sink_x_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.qtgui_time_sink_x_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.analog_frequency_modulator_fc_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_repack_bits_bb_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.digital_map_bb_0, 0))
        self.connect((self.blocks_vector_source_x_0_0, 0), (self.blocks_char_to_float_1_0, 0))
        self.connect((self.digital_map_bb_0, 0), (self.blocks_char_to_float_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.root_raised_cosine_filter_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "telecommand_tx")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_rrc_inter(self):
        return self.rrc_inter

    def set_rrc_inter(self, rrc_inter):
        self.rrc_inter = rrc_inter
        self.set_fdev(self.bit_rate*self.rrc_inter/4)
        self.root_raised_cosine_filter_0.set_taps(firdes.root_raised_cosine(1, self.bit_rate*self.rrc_inter, self.bit_rate, 0.7, 1000))
        self.qtgui_time_sink_x_0_0_0.set_samp_rate(self.bit_rate*self.rrc_inter)
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.bit_rate*self.rrc_inter*8)
        self.qtgui_time_sink_x_0.set_samp_rate(self.bit_rate*self.rrc_inter)
        self.qtgui_freq_sink_x_0_0.set_frequency_range(0, self.bit_rate*self.rrc_inter*8)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.bit_rate*self.rrc_inter)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.bit_rate*self.rrc_inter*8, self.bit_rate*self.rrc_inter/2, self.bit_rate*self.rrc_inter/20, firdes.WIN_HAMMING, 6.76))
        self.iio_fmcomms2_sink_0.set_params(144100000, self.bit_rate*self.rrc_inter*8, 100000, "A", 10, 10, '', True)
        self.analog_frequency_modulator_fc_0.set_sensitivity(self.fdev*6.28/(self.bit_rate*self.rrc_inter))

    def get_bit_rate(self):
        return self.bit_rate

    def set_bit_rate(self, bit_rate):
        self.bit_rate = bit_rate
        self.set_fdev(self.bit_rate*self.rrc_inter/4)
        self.root_raised_cosine_filter_0.set_taps(firdes.root_raised_cosine(1, self.bit_rate*self.rrc_inter, self.bit_rate, 0.7, 1000))
        self.qtgui_time_sink_x_0_0_0.set_samp_rate(self.bit_rate*self.rrc_inter)
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.bit_rate*self.rrc_inter*8)
        self.qtgui_time_sink_x_0.set_samp_rate(self.bit_rate*self.rrc_inter)
        self.qtgui_freq_sink_x_0_0.set_frequency_range(0, self.bit_rate*self.rrc_inter*8)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.bit_rate*self.rrc_inter)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.bit_rate*self.rrc_inter*8, self.bit_rate*self.rrc_inter/2, self.bit_rate*self.rrc_inter/20, firdes.WIN_HAMMING, 6.76))
        self.iio_fmcomms2_sink_0.set_params(144100000, self.bit_rate*self.rrc_inter*8, 100000, "A", 10, 10, '', True)
        self.blocks_throttle_0.set_sample_rate(self.bit_rate)
        self.analog_frequency_modulator_fc_0.set_sensitivity(self.fdev*6.28/(self.bit_rate*self.rrc_inter))

    def get_tx_gain2(self):
        return self.tx_gain2

    def set_tx_gain2(self, tx_gain2):
        self.tx_gain2 = tx_gain2
        self.blocks_multiply_const_vxx_0.set_k((self.tx_gain2, ))

    def get_tx_gain(self):
        return self.tx_gain

    def set_tx_gain(self, tx_gain):
        self.tx_gain = tx_gain
        self.blocks_multiply_const_vxx_0_0.set_k((self.tx_gain, ))

    def get_fdev(self):
        return self.fdev

    def set_fdev(self, fdev):
        self.fdev = fdev
        self.analog_frequency_modulator_fc_0.set_sensitivity(self.fdev*6.28/(self.bit_rate*self.rrc_inter))

    def get_data_src(self):
        return self.data_src

    def set_data_src(self, data_src):
        self.data_src = data_src
        self._data_src_callback(self.data_src)


def main(top_block_cls=telecommand_tx, options=None):

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
