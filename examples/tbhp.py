#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Tbhp
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
import satellites
import sip
import sys
from gnuradio import qtgui


class tbhp(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Tbhp")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Tbhp")
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

        self.settings = Qt.QSettings("GNU Radio", "tbhp")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.tm_symb_rate = tm_symb_rate = 52083
        self.tm_samp_per_symb = tm_samp_per_symb = 10
        self.tm_dec1 = tm_dec1 = 6
        self.rate = rate = 2
        self.polys = polys = [109, 79]
        self.k = k = 7
        self.frx_if = frx_if = 75000
        self.bc_symb_rate = bc_symb_rate = 270
        self.bc_samp_per_symb = bc_samp_per_symb = 19.29
        self.bc_f_if = bc_f_if = 30000
        self.adrx_samp_rate = adrx_samp_rate = tm_symb_rate*tm_dec1*tm_samp_per_symb
        self.MTU = MTU = 1500
        self.tm_waterfall_per = tm_waterfall_per = 0.1
        self.tm_ss_ted_gain_range = tm_ss_ted_gain_range = 100
        self.tm_ss_loopbw_range = tm_ss_loopbw_range = 0.2
        self.tm_ss_damping_factor_range = tm_ss_damping_factor_range = 0.5
        self.tm_pll_loopbw_range = tm_pll_loopbw_range = 0.3
        self.tm_gain_before_tr = tm_gain_before_tr = 30
        self.tm_channel_bw = tm_channel_bw = tm_symb_rate*3+frx_if


        self.dec_cc = dec_cc = fec.cc_decoder.make(MTU*8, k, rate, (polys), 0, -1, fec.CC_TERMINATED, False)

        self.bc_waterfall_per = bc_waterfall_per = 0.1
        self.bc_ss_ted_gain_range = bc_ss_ted_gain_range = 300
        self.bc_ss_loopbw_range = bc_ss_loopbw_range = 0.2
        self.bc_ss_damping_factor_range = bc_ss_damping_factor_range = 0.5
        self.bc_rrc_dec = bc_rrc_dec = 15
        self.bc_pll_loopbw_range = bc_pll_loopbw_range = 0.15
        self.bc_gain_before_tr = bc_gain_before_tr = 30
        self.bc_filt_sharp = bc_filt_sharp = 10
        self.bc_dec1 = bc_dec1 = 40
        self.bc_channel_bw = bc_channel_bw = bc_symb_rate*bc_samp_per_symb*3.5+bc_f_if
        self.adrx_channel_bw = adrx_channel_bw = adrx_samp_rate/2
        self.ad9361rx_lo_freq = ad9361rx_lo_freq = 437000000

        ##################################################
        # Blocks
        ##################################################
        self.tabs = Qt.QTabWidget()
        self.tabs_widget_0 = Qt.QWidget()
        self.tabs_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tabs_widget_0)
        self.tabs_grid_layout_0 = Qt.QGridLayout()
        self.tabs_layout_0.addLayout(self.tabs_grid_layout_0)
        self.tabs.addTab(self.tabs_widget_0, 'Telemetry')
        self.tabs_widget_1 = Qt.QWidget()
        self.tabs_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tabs_widget_1)
        self.tabs_grid_layout_1 = Qt.QGridLayout()
        self.tabs_layout_1.addLayout(self.tabs_grid_layout_1)
        self.tabs.addTab(self.tabs_widget_1, 'Telecommand')
        self.tabs_widget_2 = Qt.QWidget()
        self.tabs_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tabs_widget_2)
        self.tabs_grid_layout_2 = Qt.QGridLayout()
        self.tabs_layout_2.addLayout(self.tabs_grid_layout_2)
        self.tabs.addTab(self.tabs_widget_2, 'Beacon')
        self.top_grid_layout.addWidget(self.tabs)
        self.tm_tab_control = Qt.QTabWidget()
        self.tm_tab_control_widget_0 = Qt.QWidget()
        self.tm_tab_control_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tm_tab_control_widget_0)
        self.tm_tab_control_grid_layout_0 = Qt.QGridLayout()
        self.tm_tab_control_layout_0.addLayout(self.tm_tab_control_grid_layout_0)
        self.tm_tab_control.addTab(self.tm_tab_control_widget_0, 'General')
        self.tm_tab_control_widget_1 = Qt.QWidget()
        self.tm_tab_control_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tm_tab_control_widget_1)
        self.tm_tab_control_grid_layout_1 = Qt.QGridLayout()
        self.tm_tab_control_layout_1.addLayout(self.tm_tab_control_grid_layout_1)
        self.tm_tab_control.addTab(self.tm_tab_control_widget_1, 'GMSK Demodulator')
        self.tm_tab_control_widget_2 = Qt.QWidget()
        self.tm_tab_control_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tm_tab_control_widget_2)
        self.tm_tab_control_grid_layout_2 = Qt.QGridLayout()
        self.tm_tab_control_layout_2.addLayout(self.tm_tab_control_grid_layout_2)
        self.tm_tab_control.addTab(self.tm_tab_control_widget_2, 'Gardner Timing Recovery')
        self.tabs_grid_layout_0.addWidget(self.tm_tab_control, 0, 0, 3, 1)
        for r in range(0, 3):
            self.tabs_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.tabs_grid_layout_0.setColumnStretch(c, 1)
        self.bc_tab_control = Qt.QTabWidget()
        self.bc_tab_control_widget_0 = Qt.QWidget()
        self.bc_tab_control_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.bc_tab_control_widget_0)
        self.bc_tab_control_grid_layout_0 = Qt.QGridLayout()
        self.bc_tab_control_layout_0.addLayout(self.bc_tab_control_grid_layout_0)
        self.bc_tab_control.addTab(self.bc_tab_control_widget_0, 'General')
        self.bc_tab_control_widget_1 = Qt.QWidget()
        self.bc_tab_control_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.bc_tab_control_widget_1)
        self.bc_tab_control_grid_layout_1 = Qt.QGridLayout()
        self.bc_tab_control_layout_1.addLayout(self.bc_tab_control_grid_layout_1)
        self.bc_tab_control.addTab(self.bc_tab_control_widget_1, 'GMSK Demodulator')
        self.bc_tab_control_widget_2 = Qt.QWidget()
        self.bc_tab_control_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.bc_tab_control_widget_2)
        self.bc_tab_control_grid_layout_2 = Qt.QGridLayout()
        self.bc_tab_control_layout_2.addLayout(self.bc_tab_control_grid_layout_2)
        self.bc_tab_control.addTab(self.bc_tab_control_widget_2, 'Gardner Timing Recovery')
        self.tabs_grid_layout_2.addWidget(self.bc_tab_control, 0, 0, 3, 1)
        for r in range(0, 3):
            self.tabs_grid_layout_2.setRowStretch(r, 1)
        for c in range(0, 1):
            self.tabs_grid_layout_2.setColumnStretch(c, 1)
        self._tm_waterfall_per_tool_bar = Qt.QToolBar(self)
        self._tm_waterfall_per_tool_bar.addWidget(Qt.QLabel('Waterfall Plot Period'+": "))
        self._tm_waterfall_per_line_edit = Qt.QLineEdit(str(self.tm_waterfall_per))
        self._tm_waterfall_per_tool_bar.addWidget(self._tm_waterfall_per_line_edit)
        self._tm_waterfall_per_line_edit.returnPressed.connect(
        	lambda: self.set_tm_waterfall_per(eng_notation.str_to_num(str(self._tm_waterfall_per_line_edit.text().toAscii()))))
        self.tm_tab_control_grid_layout_0.addWidget(self._tm_waterfall_per_tool_bar, 3, 0, 1, 4)
        for r in range(3, 4):
            self.tm_tab_control_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 4):
            self.tm_tab_control_grid_layout_0.setColumnStretch(c, 1)
        self.tm_tab_stat = Qt.QTabWidget()
        self.tm_tab_stat_widget_0 = Qt.QWidget()
        self.tm_tab_stat_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tm_tab_stat_widget_0)
        self.tm_tab_stat_grid_layout_0 = Qt.QGridLayout()
        self.tm_tab_stat_layout_0.addLayout(self.tm_tab_stat_grid_layout_0)
        self.tm_tab_stat.addTab(self.tm_tab_stat_widget_0, 'General')
        self.tabs_grid_layout_0.addWidget(self.tm_tab_stat, 3, 0, 1, 1)
        for r in range(3, 4):
            self.tabs_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.tabs_grid_layout_0.setColumnStretch(c, 1)
        self.tm_tab_plot = Qt.QTabWidget()
        self.tm_tab_plot_widget_0 = Qt.QWidget()
        self.tm_tab_plot_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tm_tab_plot_widget_0)
        self.tm_tab_plot_grid_layout_0 = Qt.QGridLayout()
        self.tm_tab_plot_layout_0.addLayout(self.tm_tab_plot_grid_layout_0)
        self.tm_tab_plot.addTab(self.tm_tab_plot_widget_0, 'Frequency Plot')
        self.tm_tab_plot_widget_1 = Qt.QWidget()
        self.tm_tab_plot_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tm_tab_plot_widget_1)
        self.tm_tab_plot_grid_layout_1 = Qt.QGridLayout()
        self.tm_tab_plot_layout_1.addLayout(self.tm_tab_plot_grid_layout_1)
        self.tm_tab_plot.addTab(self.tm_tab_plot_widget_1, 'Time Plot')
        self.tm_tab_plot_widget_2 = Qt.QWidget()
        self.tm_tab_plot_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tm_tab_plot_widget_2)
        self.tm_tab_plot_grid_layout_2 = Qt.QGridLayout()
        self.tm_tab_plot_layout_2.addLayout(self.tm_tab_plot_grid_layout_2)
        self.tm_tab_plot.addTab(self.tm_tab_plot_widget_2, 'Demoded Bits 1')
        self.tm_tab_plot_widget_3 = Qt.QWidget()
        self.tm_tab_plot_layout_3 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tm_tab_plot_widget_3)
        self.tm_tab_plot_grid_layout_3 = Qt.QGridLayout()
        self.tm_tab_plot_layout_3.addLayout(self.tm_tab_plot_grid_layout_3)
        self.tm_tab_plot.addTab(self.tm_tab_plot_widget_3, 'Demoded Bits 2')
        self.tm_tab_plot_widget_4 = Qt.QWidget()
        self.tm_tab_plot_layout_4 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tm_tab_plot_widget_4)
        self.tm_tab_plot_grid_layout_4 = Qt.QGridLayout()
        self.tm_tab_plot_layout_4.addLayout(self.tm_tab_plot_grid_layout_4)
        self.tm_tab_plot.addTab(self.tm_tab_plot_widget_4, 'Decoded Data (Viterbi)')
        self.tm_tab_plot_widget_5 = Qt.QWidget()
        self.tm_tab_plot_layout_5 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tm_tab_plot_widget_5)
        self.tm_tab_plot_grid_layout_5 = Qt.QGridLayout()
        self.tm_tab_plot_layout_5.addLayout(self.tm_tab_plot_grid_layout_5)
        self.tm_tab_plot.addTab(self.tm_tab_plot_widget_5, 'Decoded Data (RS)')
        self.tm_tab_plot_widget_6 = Qt.QWidget()
        self.tm_tab_plot_layout_6 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tm_tab_plot_widget_6)
        self.tm_tab_plot_grid_layout_6 = Qt.QGridLayout()
        self.tm_tab_plot_layout_6.addLayout(self.tm_tab_plot_grid_layout_6)
        self.tm_tab_plot.addTab(self.tm_tab_plot_widget_6, 'Decrypted Data')
        self.tabs_grid_layout_0.addWidget(self.tm_tab_plot, 0, 1, 4, 3)
        for r in range(0, 4):
            self.tabs_grid_layout_0.setRowStretch(r, 1)
        for c in range(1, 4):
            self.tabs_grid_layout_0.setColumnStretch(c, 1)
        self._tm_ss_ted_gain_range_range = Range(1, 1000, 1, 100, 10000)
        self._tm_ss_ted_gain_range_win = RangeWidget(self._tm_ss_ted_gain_range_range, self.set_tm_ss_ted_gain_range, 'Symbol Sync TED gain', "slider", float)
        self.tm_tab_control_grid_layout_2.addWidget(self._tm_ss_ted_gain_range_win, 1, 0, 1, 4)
        for r in range(1, 2):
            self.tm_tab_control_grid_layout_2.setRowStretch(r, 1)
        for c in range(0, 4):
            self.tm_tab_control_grid_layout_2.setColumnStretch(c, 1)
        self._tm_ss_loopbw_range_range = Range(0.001, 2, 0.001, 0.2, 10000)
        self._tm_ss_loopbw_range_win = RangeWidget(self._tm_ss_loopbw_range_range, self.set_tm_ss_loopbw_range, 'Symbol Sync LBW', "slider", float)
        self.tm_tab_control_grid_layout_2.addWidget(self._tm_ss_loopbw_range_win, 0, 0, 1, 4)
        for r in range(0, 1):
            self.tm_tab_control_grid_layout_2.setRowStretch(r, 1)
        for c in range(0, 4):
            self.tm_tab_control_grid_layout_2.setColumnStretch(c, 1)
        self._tm_ss_damping_factor_range_range = Range(0.001, 2, 0.001, 0.5, 10000)
        self._tm_ss_damping_factor_range_win = RangeWidget(self._tm_ss_damping_factor_range_range, self.set_tm_ss_damping_factor_range, 'Symbol Sync DF', "slider", float)
        self.tm_tab_control_grid_layout_2.addWidget(self._tm_ss_damping_factor_range_win, 2, 0, 1, 4)
        for r in range(2, 3):
            self.tm_tab_control_grid_layout_2.setRowStretch(r, 1)
        for c in range(0, 4):
            self.tm_tab_control_grid_layout_2.setColumnStretch(c, 1)
        self._tm_pll_loopbw_range_range = Range(0.001, 2, 0.001, 0.3, 10000)
        self._tm_pll_loopbw_range_win = RangeWidget(self._tm_pll_loopbw_range_range, self.set_tm_pll_loopbw_range, 'PLL LBW', "slider", float)
        self.tm_tab_control_grid_layout_1.addWidget(self._tm_pll_loopbw_range_win, 0, 0, 1, 4)
        for r in range(0, 1):
            self.tm_tab_control_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 4):
            self.tm_tab_control_grid_layout_1.setColumnStretch(c, 1)
        self._tm_gain_before_tr_range = Range(0.1, 100, 0.1, 30, 1000)
        self._tm_gain_before_tr_win = RangeWidget(self._tm_gain_before_tr_range, self.set_tm_gain_before_tr, 'Gain', "slider", float)
        self.tm_tab_control_grid_layout_1.addWidget(self._tm_gain_before_tr_win, 1, 0, 1, 4)
        for r in range(1, 2):
            self.tm_tab_control_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 4):
            self.tm_tab_control_grid_layout_1.setColumnStretch(c, 1)
        self._frx_if_tool_bar = Qt.QToolBar(self)
        self._frx_if_tool_bar.addWidget(Qt.QLabel('IF Frequency'+": "))
        self._frx_if_line_edit = Qt.QLineEdit(str(self.frx_if))
        self._frx_if_tool_bar.addWidget(self._frx_if_line_edit)
        self._frx_if_line_edit.returnPressed.connect(
        	lambda: self.set_frx_if(int(str(self._frx_if_line_edit.text().toAscii()))))
        self.tm_tab_control_grid_layout_0.addWidget(self._frx_if_tool_bar, 1, 0, 1, 2)
        for r in range(1, 2):
            self.tm_tab_control_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 2):
            self.tm_tab_control_grid_layout_0.setColumnStretch(c, 1)
        self.bc_tab_stat = Qt.QTabWidget()
        self.bc_tab_stat_widget_0 = Qt.QWidget()
        self.bc_tab_stat_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.bc_tab_stat_widget_0)
        self.bc_tab_stat_grid_layout_0 = Qt.QGridLayout()
        self.bc_tab_stat_layout_0.addLayout(self.bc_tab_stat_grid_layout_0)
        self.bc_tab_stat.addTab(self.bc_tab_stat_widget_0, 'General')
        self.tabs_grid_layout_2.addWidget(self.bc_tab_stat, 3, 0, 1, 1)
        for r in range(3, 4):
            self.tabs_grid_layout_2.setRowStretch(r, 1)
        for c in range(0, 1):
            self.tabs_grid_layout_2.setColumnStretch(c, 1)
        self.bc_tab_plot = Qt.QTabWidget()
        self.bc_tab_plot_widget_0 = Qt.QWidget()
        self.bc_tab_plot_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.bc_tab_plot_widget_0)
        self.bc_tab_plot_grid_layout_0 = Qt.QGridLayout()
        self.bc_tab_plot_layout_0.addLayout(self.bc_tab_plot_grid_layout_0)
        self.bc_tab_plot.addTab(self.bc_tab_plot_widget_0, 'Frequency Plot')
        self.bc_tab_plot_widget_1 = Qt.QWidget()
        self.bc_tab_plot_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.bc_tab_plot_widget_1)
        self.bc_tab_plot_grid_layout_1 = Qt.QGridLayout()
        self.bc_tab_plot_layout_1.addLayout(self.bc_tab_plot_grid_layout_1)
        self.bc_tab_plot.addTab(self.bc_tab_plot_widget_1, 'Time Plot')
        self.bc_tab_plot_widget_2 = Qt.QWidget()
        self.bc_tab_plot_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.bc_tab_plot_widget_2)
        self.bc_tab_plot_grid_layout_2 = Qt.QGridLayout()
        self.bc_tab_plot_layout_2.addLayout(self.bc_tab_plot_grid_layout_2)
        self.bc_tab_plot.addTab(self.bc_tab_plot_widget_2, 'Demoded Bits 1')
        self.bc_tab_plot_widget_3 = Qt.QWidget()
        self.bc_tab_plot_layout_3 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.bc_tab_plot_widget_3)
        self.bc_tab_plot_grid_layout_3 = Qt.QGridLayout()
        self.bc_tab_plot_layout_3.addLayout(self.bc_tab_plot_grid_layout_3)
        self.bc_tab_plot.addTab(self.bc_tab_plot_widget_3, 'Demoded Bits 2')
        self.bc_tab_plot_widget_4 = Qt.QWidget()
        self.bc_tab_plot_layout_4 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.bc_tab_plot_widget_4)
        self.bc_tab_plot_grid_layout_4 = Qt.QGridLayout()
        self.bc_tab_plot_layout_4.addLayout(self.bc_tab_plot_grid_layout_4)
        self.bc_tab_plot.addTab(self.bc_tab_plot_widget_4, 'Decoded Data (Viterbi)')
        self.bc_tab_plot_widget_5 = Qt.QWidget()
        self.bc_tab_plot_layout_5 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.bc_tab_plot_widget_5)
        self.bc_tab_plot_grid_layout_5 = Qt.QGridLayout()
        self.bc_tab_plot_layout_5.addLayout(self.bc_tab_plot_grid_layout_5)
        self.bc_tab_plot.addTab(self.bc_tab_plot_widget_5, 'Decoded Data (RS)')
        self.bc_tab_plot_widget_6 = Qt.QWidget()
        self.bc_tab_plot_layout_6 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.bc_tab_plot_widget_6)
        self.bc_tab_plot_grid_layout_6 = Qt.QGridLayout()
        self.bc_tab_plot_layout_6.addLayout(self.bc_tab_plot_grid_layout_6)
        self.bc_tab_plot.addTab(self.bc_tab_plot_widget_6, 'Decrypted Data')
        self.tabs_grid_layout_2.addWidget(self.bc_tab_plot, 0, 1, 4, 3)
        for r in range(0, 4):
            self.tabs_grid_layout_2.setRowStretch(r, 1)
        for c in range(1, 4):
            self.tabs_grid_layout_2.setColumnStretch(c, 1)
        self._bc_ss_ted_gain_range_range = Range(1, 1000, 1, 300, 10000)
        self._bc_ss_ted_gain_range_win = RangeWidget(self._bc_ss_ted_gain_range_range, self.set_bc_ss_ted_gain_range, 'Symbol Sync TED gain', "slider", float)
        self.bc_tab_control_grid_layout_2.addWidget(self._bc_ss_ted_gain_range_win, 1, 0, 1, 4)
        for r in range(1, 2):
            self.bc_tab_control_grid_layout_2.setRowStretch(r, 1)
        for c in range(0, 4):
            self.bc_tab_control_grid_layout_2.setColumnStretch(c, 1)
        self._bc_ss_loopbw_range_range = Range(0.001, 2, 0.001, 0.2, 10000)
        self._bc_ss_loopbw_range_win = RangeWidget(self._bc_ss_loopbw_range_range, self.set_bc_ss_loopbw_range, 'Symbol Sync LBW', "slider", float)
        self.bc_tab_control_grid_layout_2.addWidget(self._bc_ss_loopbw_range_win, 0, 0, 1, 4)
        for r in range(0, 1):
            self.bc_tab_control_grid_layout_2.setRowStretch(r, 1)
        for c in range(0, 4):
            self.bc_tab_control_grid_layout_2.setColumnStretch(c, 1)
        self._bc_ss_damping_factor_range_range = Range(0.001, 2, 0.001, 0.5, 10000)
        self._bc_ss_damping_factor_range_win = RangeWidget(self._bc_ss_damping_factor_range_range, self.set_bc_ss_damping_factor_range, 'Symbol Sync DF', "slider", float)
        self.bc_tab_control_grid_layout_2.addWidget(self._bc_ss_damping_factor_range_win, 2, 0, 1, 4)
        for r in range(2, 3):
            self.bc_tab_control_grid_layout_2.setRowStretch(r, 1)
        for c in range(0, 4):
            self.bc_tab_control_grid_layout_2.setColumnStretch(c, 1)
        self._bc_pll_loopbw_range_range = Range(0.001, 2, 0.001, 0.15, 10000)
        self._bc_pll_loopbw_range_win = RangeWidget(self._bc_pll_loopbw_range_range, self.set_bc_pll_loopbw_range, 'PLL LBW', "slider", float)
        self.bc_tab_control_grid_layout_1.addWidget(self._bc_pll_loopbw_range_win, 0, 0, 1, 4)
        for r in range(0, 1):
            self.bc_tab_control_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 4):
            self.bc_tab_control_grid_layout_1.setColumnStretch(c, 1)
        self._bc_gain_before_tr_range = Range(0.1, 100, 0.1, 30, 1000)
        self._bc_gain_before_tr_win = RangeWidget(self._bc_gain_before_tr_range, self.set_bc_gain_before_tr, 'Gain', "slider", float)
        self.bc_tab_control_grid_layout_1.addWidget(self._bc_gain_before_tr_win, 1, 0, 1, 4)
        for r in range(1, 2):
            self.bc_tab_control_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 4):
            self.bc_tab_control_grid_layout_1.setColumnStretch(c, 1)
        self._bc_f_if_tool_bar = Qt.QToolBar(self)
        self._bc_f_if_tool_bar.addWidget(Qt.QLabel('IF Frequency'+": "))
        self._bc_f_if_line_edit = Qt.QLineEdit(str(self.bc_f_if))
        self._bc_f_if_tool_bar.addWidget(self._bc_f_if_line_edit)
        self._bc_f_if_line_edit.returnPressed.connect(
        	lambda: self.set_bc_f_if(int(str(self._bc_f_if_line_edit.text().toAscii()))))
        self.bc_tab_control_grid_layout_0.addWidget(self._bc_f_if_tool_bar, 1, 0, 1, 2)
        for r in range(1, 2):
            self.bc_tab_control_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 2):
            self.bc_tab_control_grid_layout_0.setColumnStretch(c, 1)
        self._ad9361rx_lo_freq_tool_bar = Qt.QToolBar(self)
        self._ad9361rx_lo_freq_tool_bar.addWidget(Qt.QLabel('AD9361 LO Frequency'+": "))
        self._ad9361rx_lo_freq_line_edit = Qt.QLineEdit(str(self.ad9361rx_lo_freq))
        self._ad9361rx_lo_freq_tool_bar.addWidget(self._ad9361rx_lo_freq_line_edit)
        self._ad9361rx_lo_freq_line_edit.returnPressed.connect(
        	lambda: self.set_ad9361rx_lo_freq(int(str(self._ad9361rx_lo_freq_line_edit.text().toAscii()))))
        self.tm_tab_control_grid_layout_0.addWidget(self._ad9361rx_lo_freq_tool_bar, 0, 0, 1, 4)
        for r in range(0, 1):
            self.tm_tab_control_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 4):
            self.tm_tab_control_grid_layout_0.setColumnStretch(c, 1)
        self.satellites_decode_rs_general_0 = satellites.decode_rs_general(285, 0, 1, 32, False, False)
        self.root_raised_cosine_filter_0 = filter.fir_filter_fff(bc_rrc_dec, firdes.root_raised_cosine(
        	1, adrx_samp_rate/bc_dec1, bc_symb_rate, 0.7, 32))
        self.qtgui_waterfall_sink_x_0 = qtgui.waterfall_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	adrx_samp_rate, #bw
        	"", #name
                1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0.set_update_time(tm_waterfall_per)
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
        self.tm_tab_plot_grid_layout_0.addWidget(self._qtgui_waterfall_sink_x_0_win)
        self.qtgui_time_sink_x_0_0_0_0_0_0 = qtgui.time_sink_f(
        	90*2*8+200, #size
        	bc_symb_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_0_0_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0_0_0_0_0.set_y_axis(-1.5, 1.5)

        self.qtgui_time_sink_x_0_0_0_0_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0_0_0_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0_0_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_TAG, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "pkt_len")
        self.qtgui_time_sink_x_0_0_0_0_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0_0_0_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0_0_0_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_0_0_0_0.enable_control_panel(True)
        self.qtgui_time_sink_x_0_0_0_0_0_0.enable_stem_plot(False)

        if not False:
          self.qtgui_time_sink_x_0_0_0_0_0_0.disable_legend()

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
                self.qtgui_time_sink_x_0_0_0_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0_0_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_0_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_0_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_0_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_0_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_0_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_0_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_0_0_0_0.pyqwidget(), Qt.QWidget)
        self.bc_tab_plot_grid_layout_2.addWidget(self._qtgui_time_sink_x_0_0_0_0_0_0_win)
        self.qtgui_time_sink_x_0_0_0_0_0 = qtgui.time_sink_f(
        	4144, #size
        	tm_symb_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_0_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0_0_0_0.set_y_axis(-1, 1)

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
        styles = [0, 1, 1, 1, 1,
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
        self.tm_tab_plot_grid_layout_3.addWidget(self._qtgui_time_sink_x_0_0_0_0_0_win, 0, 0, 2, 4)
        for r in range(0, 2):
            self.tm_tab_plot_grid_layout_3.setRowStretch(r, 1)
        for c in range(0, 4):
            self.tm_tab_plot_grid_layout_3.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0_0 = qtgui.time_sink_f(
        	3000, #size
        	adrx_samp_rate/bc_dec1, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0.set_y_axis(-10, 10)

        self.qtgui_time_sink_x_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0.enable_tags(-1, False)
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
        self.bc_tab_plot_grid_layout_1.addWidget(self._qtgui_time_sink_x_0_0_win)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	3000, #size
        	adrx_samp_rate/tm_dec1, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-10, 10)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(-1, False)
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
        self.tm_tab_plot_grid_layout_1.addWidget(self._qtgui_time_sink_x_0_win)
        self.qtgui_number_sink_0_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_NONE,
            2
        )
        self.qtgui_number_sink_0_0.set_update_time(0.10)
        self.qtgui_number_sink_0_0.set_title("Received Frame Counter")

        labels = ['Counter', 'Rate (bps)', '', '', '',
                  '', '', '', '', '']
        units = ['', '', '', '', '',
                 '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(2):
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
        self.bc_tab_stat_grid_layout_0.addWidget(self._qtgui_number_sink_0_0_win, 0, 2, 2, 1)
        for r in range(0, 2):
            self.bc_tab_stat_grid_layout_0.setRowStretch(r, 1)
        for c in range(2, 3):
            self.bc_tab_stat_grid_layout_0.setColumnStretch(c, 1)
        self.qtgui_number_sink_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_NONE,
            2
        )
        self.qtgui_number_sink_0.set_update_time(0.10)
        self.qtgui_number_sink_0.set_title("Received Frame Counter")

        labels = ['Counter', 'Rate (bps)', '', '', '',
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
        self.tm_tab_stat_grid_layout_0.addWidget(self._qtgui_number_sink_0_win, 0, 2, 2, 1)
        for r in range(0, 2):
            self.tm_tab_stat_grid_layout_0.setRowStretch(r, 1)
        for c in range(2, 3):
            self.tm_tab_stat_grid_layout_0.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	adrx_samp_rate, #bw
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
        self.tm_tab_plot_grid_layout_0.addWidget(self._qtgui_freq_sink_x_0_win)
        self.low_pass_filter_0_0 = filter.fir_filter_ccf(bc_dec1, firdes.low_pass(
        	1, adrx_samp_rate, bc_channel_bw, bc_channel_bw/bc_filt_sharp, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0 = filter.fir_filter_ccf(tm_dec1, firdes.low_pass(
        	1, adrx_samp_rate, tm_channel_bw, tm_channel_bw/20, firdes.WIN_HAMMING, 6.76))
        self.iustsat_zafar_telemetry_frame_extractor_1_0 = iustsat.zafar_telemetry_frame_extractor("pkt_len")
        self.iustsat_zafar_telemetry_frame_extractor_1 = iustsat.zafar_telemetry_frame_extractor("pkt_len")
        self.iustsat_zafar_telemetry_derand_0_0 = iustsat.zafar_telemetry_derand("pkt_len")
        self.iustsat_zafar_telemetry_derand_0 = iustsat.zafar_telemetry_derand("pkt_len")
        self.iustsat_vt_to_decrypt_0 = iustsat.vt_to_decrypt('iv', ([0xCA, 0xFE, 0xBA, 0xBE, 0xFA, 0xCE, 0xDB, 0xAD, 0xDE, 0xCA, 0xF8, 0x88]), 'aad', 'auth_tag')
        self.iustsat_tag_counter_0_0 = iustsat.tag_counter('pkt_len')
        self.iustsat_tag_counter_0 = iustsat.tag_counter('pkt_len')
        self.iustsat_synch_detect_tag_1_0 = iustsat.synch_detect_tag(60,'pkt_len',93*2*8)
        self.iustsat_synch_detect_tag_1 = iustsat.synch_detect_tag(60,'pkt_len',259*2*8)
        self.iustsat_rs_to_decrypt_0_0 = iustsat.rs_to_decrypt('iv', ([0xCA, 0xFE, 0xBA, 0xBE, 0xFA, 0xCE, 0xDB, 0xAD, 0xDE, 0xCA, 0xF8, 0x88]), 'aad', 'auth_tag')
        self.iustsat_pdu_to_message_0_0 = iustsat.pdu_to_message('frm_len')
        self.iustsat_pdu_to_message_0 = iustsat.pdu_to_message('frm_len')
        self.iustsat_pdu_debug_0_0_0 = iustsat.pdu_debug('auth_tag')
        self.iio_fmcomms2_source_0 = iio.fmcomms2_source_f32c('192.168.1.10', ad9361rx_lo_freq-frx_if, adrx_samp_rate, adrx_channel_bw*5, True, False, 0x8000, True, True, True, "fast_attack", 64.0, "manual", 64.0, "A_BALANCED", '', True)
        self.fir_filter_xxx_0_0 = filter.fir_filter_fff(1, ([1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,-1,-1,1,1,-1,-1,-1,1,1,1,1,1,1,1,1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,1,1,-1,1,1,-1,-1,-1,-1,1,-1,1,1,1,-1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1]))
        self.fir_filter_xxx_0_0.declare_sample_delay(0)
        self.fir_filter_xxx_0 = filter.fir_filter_fff(1, ([1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,1,-1,-1,1,1,-1,-1,-1,1,1,1,1,1,1,1,1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,1,1,-1,1,1,-1,-1,-1,-1,1,-1,1,1,1,-1,1,-1,1,1,1,-1,-1,-1,-1,-1,-1]))
        self.fir_filter_xxx_0.declare_sample_delay(0)
        self.fec_async_decoder_0_0 = fec.async_decoder(dec_cc, True, False, MTU)
        self.fec_async_decoder_0 = fec.async_decoder(dec_cc, True, False, MTU)
        self.digital_symbol_sync_xx_0_0 = digital.symbol_sync_ff(digital.TED_GARDNER, bc_samp_per_symb, bc_ss_loopbw_range, bc_ss_damping_factor_range, bc_ss_ted_gain_range, 2, 1, digital.constellation_bpsk().base(), digital.IR_PFB_NO_MF, 32, ([]))
        self.digital_symbol_sync_xx_0 = digital.symbol_sync_ff(digital.TED_GARDNER, tm_samp_per_symb, tm_ss_loopbw_range, tm_ss_damping_factor_range, tm_ss_ted_gain_range, 2, 1, digital.constellation_bpsk().base(), digital.IR_PFB_NO_MF, 128, ([]))
        self.digital_binary_slicer_fb_0_0 = digital.binary_slicer_fb()
        self.digital_binary_slicer_fb_0 = digital.binary_slicer_fb()
        self.dc_blocker_xx_0_0 = filter.dc_blocker_ff(20000, True)
        self.dc_blocker_xx_0 = filter.dc_blocker_ff(65536, True)
        self.crypto_auth_dec_aes_gcm_0_0_0 = crypto.auth_dec_aes_gcm(([0xFE, 0xFF, 0xE9, 0x92, 0x86, 0x65, 0x73, 0x1C, 0x6D, 0x6A, 0x8F, 0x94, 0x67, 0x30, 0x83, 0x08]), 16, 96)
        self.crypto_auth_dec_aes_gcm_0_0 = crypto.auth_dec_aes_gcm(([0xFE, 0xFF, 0xE9, 0x92, 0x86, 0x65, 0x73, 0x1C, 0x6D, 0x6A, 0x8F, 0x94, 0x67, 0x30, 0x83, 0x08]), 16, 96)
        self.blocks_uchar_to_float_0_0 = blocks.uchar_to_float()
        self.blocks_uchar_to_float_0 = blocks.uchar_to_float()
        self.blocks_tag_gate_0_0 = blocks.tag_gate(gr.sizeof_float * 1, False)
        self.blocks_tag_gate_0_0.set_single_key("")
        self.blocks_tag_gate_0 = blocks.tag_gate(gr.sizeof_float * 1, False)
        self.blocks_tag_gate_0.set_single_key("")
        self.blocks_pdu_to_tagged_stream_0_0_0_0_0 = blocks.pdu_to_tagged_stream(blocks.float_t, 'frm_len')
        self.blocks_pdu_to_tagged_stream_0_0_0_0 = blocks.pdu_to_tagged_stream(blocks.float_t, 'frm_len')
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_1_0 = blocks.multiply_const_vff((0.1, ))
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_vff((0.066666667, ))
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_vff((2, ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((2, ))
        self.blocks_multiply_const_0 = blocks.multiply_const_vff((bc_gain_before_tr, ))
        self.blocks_multiply_const = blocks.multiply_const_vff((tm_gain_before_tr, ))
        self.blocks_float_to_uchar_0_0 = blocks.float_to_uchar()
        self.blocks_float_to_uchar_0 = blocks.float_to_uchar()
        self.blocks_file_sink_0_0 = blocks.file_sink(gr.sizeof_char*1, '/home/iust/Documents/zafar_prj/gr-iustsat/examples/ReceivedData/TelemetryReceivedData.bin', False)
        self.blocks_file_sink_0_0.set_unbuffered(True)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, '/home/iust/Documents/zafar_prj/gr-iustsat/examples/ReceivedData/BeaconReceivedData.bin', False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blocks_delay_0_0 = blocks.delay(gr.sizeof_float*1, 63)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_float*1, 63)
        self.blocks_add_const_vxx_0_0 = blocks.add_const_vff((-1, ))
        self.blocks_add_const_vxx_0 = blocks.add_const_vff((-1, ))
        self._bc_waterfall_per_tool_bar = Qt.QToolBar(self)
        self._bc_waterfall_per_tool_bar.addWidget(Qt.QLabel('Waterfall Plot Period'+": "))
        self._bc_waterfall_per_line_edit = Qt.QLineEdit(str(self.bc_waterfall_per))
        self._bc_waterfall_per_tool_bar.addWidget(self._bc_waterfall_per_line_edit)
        self._bc_waterfall_per_line_edit.returnPressed.connect(
        	lambda: self.set_bc_waterfall_per(eng_notation.str_to_num(str(self._bc_waterfall_per_line_edit.text().toAscii()))))
        self.bc_tab_control_grid_layout_0.addWidget(self._bc_waterfall_per_tool_bar, 3, 0, 1, 4)
        for r in range(3, 4):
            self.bc_tab_control_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 4):
            self.bc_tab_control_grid_layout_0.setColumnStretch(c, 1)
        self.band_pass_filter_0 = filter.fir_filter_ccc(1, firdes.complex_band_pass(
        	1, adrx_samp_rate, 850e3+frx_if, 1.15e6+frx_if, 100e3, firdes.WIN_HAMMING, 6.76))
        self.analog_sig_source_x_0 = analog.sig_source_c(adrx_samp_rate, analog.GR_COS_WAVE, -(1000000+(frx_if-bc_f_if)), 1, 0)
        self.analog_pll_freqdet_cf_0_0 = analog.pll_freqdet_cf(bc_pll_loopbw_range, 20000*6.28/(adrx_samp_rate/bc_dec1), 0*6.28/(adrx_samp_rate/bc_dec1))
        self.analog_pll_freqdet_cf_0 = analog.pll_freqdet_cf(tm_pll_loopbw_range, tm_channel_bw*6.28/(adrx_samp_rate/tm_dec1), -tm_channel_bw*6.28/(adrx_samp_rate/tm_dec1))



        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.crypto_auth_dec_aes_gcm_0_0, 'pdus'), (self.iustsat_pdu_to_message_0, 'in'))
        self.msg_connect((self.crypto_auth_dec_aes_gcm_0_0_0, 'pdus'), (self.iustsat_pdu_debug_0_0_0, 'pdu_in'))
        self.msg_connect((self.crypto_auth_dec_aes_gcm_0_0_0, 'pdus'), (self.iustsat_pdu_to_message_0_0, 'in'))
        self.msg_connect((self.fec_async_decoder_0, 'out'), (self.iustsat_zafar_telemetry_derand_0, 'in'))
        self.msg_connect((self.fec_async_decoder_0_0, 'out'), (self.iustsat_zafar_telemetry_derand_0_0, 'in'))
        self.msg_connect((self.iustsat_pdu_to_message_0, 'out'), (self.blocks_pdu_to_tagged_stream_0_0_0_0, 'pdus'))
        self.msg_connect((self.iustsat_pdu_to_message_0_0, 'out'), (self.blocks_pdu_to_tagged_stream_0_0_0_0_0, 'pdus'))
        self.msg_connect((self.iustsat_rs_to_decrypt_0_0, 'out'), (self.crypto_auth_dec_aes_gcm_0_0_0, 'pdus'))
        self.msg_connect((self.iustsat_vt_to_decrypt_0, 'out'), (self.crypto_auth_dec_aes_gcm_0_0, 'pdus'))
        self.msg_connect((self.iustsat_zafar_telemetry_derand_0, 'out'), (self.iustsat_vt_to_decrypt_0, 'in'))
        self.msg_connect((self.iustsat_zafar_telemetry_derand_0_0, 'out'), (self.satellites_decode_rs_general_0, 'in'))
        self.msg_connect((self.iustsat_zafar_telemetry_frame_extractor_1, 'out'), (self.fec_async_decoder_0, 'in'))
        self.msg_connect((self.iustsat_zafar_telemetry_frame_extractor_1_0, 'out'), (self.fec_async_decoder_0_0, 'in'))
        self.msg_connect((self.satellites_decode_rs_general_0, 'out'), (self.iustsat_rs_to_decrypt_0_0, 'in'))
        self.connect((self.analog_pll_freqdet_cf_0, 0), (self.dc_blocker_xx_0, 0))
        self.connect((self.analog_pll_freqdet_cf_0_0, 0), (self.dc_blocker_xx_0_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.band_pass_filter_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_add_const_vxx_0, 0), (self.fir_filter_xxx_0, 0))
        self.connect((self.blocks_add_const_vxx_0_0, 0), (self.fir_filter_xxx_0_0, 0))
        self.connect((self.blocks_delay_0, 0), (self.iustsat_synch_detect_tag_1, 0))
        self.connect((self.blocks_delay_0_0, 0), (self.iustsat_synch_detect_tag_1_0, 0))
        self.connect((self.blocks_float_to_uchar_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.blocks_float_to_uchar_0_0, 0), (self.blocks_file_sink_0_0, 0))
        self.connect((self.blocks_multiply_const, 0), (self.digital_symbol_sync_xx_0, 0))
        self.connect((self.blocks_multiply_const, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_multiply_const_0, 0), (self.root_raised_cosine_filter_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_add_const_vxx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.blocks_add_const_vxx_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.blocks_delay_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1_0, 0), (self.blocks_delay_0_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.low_pass_filter_0_0, 0))
        self.connect((self.blocks_pdu_to_tagged_stream_0_0_0_0, 0), (self.blocks_float_to_uchar_0, 0))
        self.connect((self.blocks_pdu_to_tagged_stream_0_0_0_0_0, 0), (self.blocks_float_to_uchar_0_0, 0))
        self.connect((self.blocks_tag_gate_0, 0), (self.blocks_multiply_const_vxx_1, 0))
        self.connect((self.blocks_tag_gate_0, 0), (self.digital_binary_slicer_fb_0, 0))
        self.connect((self.blocks_tag_gate_0_0, 0), (self.blocks_multiply_const_vxx_1_0, 0))
        self.connect((self.blocks_tag_gate_0_0, 0), (self.digital_binary_slicer_fb_0_0, 0))
        self.connect((self.blocks_uchar_to_float_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_uchar_to_float_0_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.dc_blocker_xx_0, 0), (self.blocks_multiply_const, 0))
        self.connect((self.dc_blocker_xx_0_0, 0), (self.blocks_multiply_const_0, 0))
        self.connect((self.digital_binary_slicer_fb_0, 0), (self.blocks_uchar_to_float_0, 0))
        self.connect((self.digital_binary_slicer_fb_0_0, 0), (self.blocks_uchar_to_float_0_0, 0))
        self.connect((self.digital_symbol_sync_xx_0, 0), (self.blocks_tag_gate_0, 0))
        self.connect((self.digital_symbol_sync_xx_0_0, 0), (self.blocks_tag_gate_0_0, 0))
        self.connect((self.fir_filter_xxx_0, 0), (self.iustsat_synch_detect_tag_1, 1))
        self.connect((self.fir_filter_xxx_0_0, 0), (self.iustsat_synch_detect_tag_1_0, 1))
        self.connect((self.iio_fmcomms2_source_0, 0), (self.band_pass_filter_0, 0))
        self.connect((self.iio_fmcomms2_source_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.iio_fmcomms2_source_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.iio_fmcomms2_source_0, 0), (self.qtgui_waterfall_sink_x_0, 0))
        self.connect((self.iustsat_synch_detect_tag_1, 0), (self.iustsat_tag_counter_0, 0))
        self.connect((self.iustsat_synch_detect_tag_1, 0), (self.iustsat_zafar_telemetry_frame_extractor_1_0, 0))
        self.connect((self.iustsat_synch_detect_tag_1, 0), (self.qtgui_time_sink_x_0_0_0_0_0, 0))
        self.connect((self.iustsat_synch_detect_tag_1_0, 0), (self.iustsat_tag_counter_0_0, 0))
        self.connect((self.iustsat_synch_detect_tag_1_0, 0), (self.iustsat_zafar_telemetry_frame_extractor_1, 0))
        self.connect((self.iustsat_synch_detect_tag_1_0, 0), (self.qtgui_time_sink_x_0_0_0_0_0_0, 0))
        self.connect((self.iustsat_tag_counter_0, 0), (self.qtgui_number_sink_0, 0))
        self.connect((self.iustsat_tag_counter_0, 1), (self.qtgui_number_sink_0, 1))
        self.connect((self.iustsat_tag_counter_0_0, 0), (self.qtgui_number_sink_0_0, 0))
        self.connect((self.iustsat_tag_counter_0_0, 1), (self.qtgui_number_sink_0_0, 1))
        self.connect((self.low_pass_filter_0, 0), (self.analog_pll_freqdet_cf_0, 0))
        self.connect((self.low_pass_filter_0_0, 0), (self.analog_pll_freqdet_cf_0_0, 0))
        self.connect((self.root_raised_cosine_filter_0, 0), (self.digital_symbol_sync_xx_0_0, 0))
        self.connect((self.root_raised_cosine_filter_0, 0), (self.qtgui_time_sink_x_0_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "tbhp")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_tm_symb_rate(self):
        return self.tm_symb_rate

    def set_tm_symb_rate(self, tm_symb_rate):
        self.tm_symb_rate = tm_symb_rate
        self.set_tm_channel_bw(self.tm_symb_rate*3+self.frx_if)
        self.set_adrx_samp_rate(self.tm_symb_rate*self.tm_dec1*self.tm_samp_per_symb)
        self.qtgui_time_sink_x_0_0_0_0_0.set_samp_rate(self.tm_symb_rate)

    def get_tm_samp_per_symb(self):
        return self.tm_samp_per_symb

    def set_tm_samp_per_symb(self, tm_samp_per_symb):
        self.tm_samp_per_symb = tm_samp_per_symb
        self.set_adrx_samp_rate(self.tm_symb_rate*self.tm_dec1*self.tm_samp_per_symb)

    def get_tm_dec1(self):
        return self.tm_dec1

    def set_tm_dec1(self, tm_dec1):
        self.tm_dec1 = tm_dec1
        self.set_adrx_samp_rate(self.tm_symb_rate*self.tm_dec1*self.tm_samp_per_symb)
        self.qtgui_time_sink_x_0.set_samp_rate(self.adrx_samp_rate/self.tm_dec1)
        self.analog_pll_freqdet_cf_0.set_max_freq(self.tm_channel_bw*6.28/(self.adrx_samp_rate/self.tm_dec1))
        self.analog_pll_freqdet_cf_0.set_min_freq(-self.tm_channel_bw*6.28/(self.adrx_samp_rate/self.tm_dec1))

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

    def get_frx_if(self):
        return self.frx_if

    def set_frx_if(self, frx_if):
        self.frx_if = frx_if
        self.set_tm_channel_bw(self.tm_symb_rate*3+self.frx_if)
        Qt.QMetaObject.invokeMethod(self._frx_if_line_edit, "setText", Qt.Q_ARG("QString", str(self.frx_if)))
        self.iio_fmcomms2_source_0.set_params(self.ad9361rx_lo_freq-self.frx_if, self.adrx_samp_rate, self.adrx_channel_bw*5, True, True, True, "fast_attack", 64.0, "manual", 64.0, "A_BALANCED", '', True)
        self.band_pass_filter_0.set_taps(firdes.complex_band_pass(1, self.adrx_samp_rate, 850e3+self.frx_if, 1.15e6+self.frx_if, 100e3, firdes.WIN_HAMMING, 6.76))
        self.analog_sig_source_x_0.set_frequency(-(1000000+(self.frx_if-self.bc_f_if)))

    def get_bc_symb_rate(self):
        return self.bc_symb_rate

    def set_bc_symb_rate(self, bc_symb_rate):
        self.bc_symb_rate = bc_symb_rate
        self.set_bc_channel_bw(self.bc_symb_rate*self.bc_samp_per_symb*3.5+self.bc_f_if)
        self.root_raised_cosine_filter_0.set_taps(firdes.root_raised_cosine(1, self.adrx_samp_rate/self.bc_dec1, self.bc_symb_rate, 0.7, 32))
        self.qtgui_time_sink_x_0_0_0_0_0_0.set_samp_rate(self.bc_symb_rate)

    def get_bc_samp_per_symb(self):
        return self.bc_samp_per_symb

    def set_bc_samp_per_symb(self, bc_samp_per_symb):
        self.bc_samp_per_symb = bc_samp_per_symb
        self.set_bc_channel_bw(self.bc_symb_rate*self.bc_samp_per_symb*3.5+self.bc_f_if)

    def get_bc_f_if(self):
        return self.bc_f_if

    def set_bc_f_if(self, bc_f_if):
        self.bc_f_if = bc_f_if
        Qt.QMetaObject.invokeMethod(self._bc_f_if_line_edit, "setText", Qt.Q_ARG("QString", str(self.bc_f_if)))
        self.set_bc_channel_bw(self.bc_symb_rate*self.bc_samp_per_symb*3.5+self.bc_f_if)
        self.analog_sig_source_x_0.set_frequency(-(1000000+(self.frx_if-self.bc_f_if)))

    def get_adrx_samp_rate(self):
        return self.adrx_samp_rate

    def set_adrx_samp_rate(self, adrx_samp_rate):
        self.adrx_samp_rate = adrx_samp_rate
        self.set_adrx_channel_bw(self.adrx_samp_rate/2)
        self.root_raised_cosine_filter_0.set_taps(firdes.root_raised_cosine(1, self.adrx_samp_rate/self.bc_dec1, self.bc_symb_rate, 0.7, 32))
        self.qtgui_waterfall_sink_x_0.set_frequency_range(0, self.adrx_samp_rate)
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.adrx_samp_rate/self.bc_dec1)
        self.qtgui_time_sink_x_0.set_samp_rate(self.adrx_samp_rate/self.tm_dec1)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.adrx_samp_rate)
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.adrx_samp_rate, self.bc_channel_bw, self.bc_channel_bw/self.bc_filt_sharp, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.adrx_samp_rate, self.tm_channel_bw, self.tm_channel_bw/20, firdes.WIN_HAMMING, 6.76))
        self.iio_fmcomms2_source_0.set_params(self.ad9361rx_lo_freq-self.frx_if, self.adrx_samp_rate, self.adrx_channel_bw*5, True, True, True, "fast_attack", 64.0, "manual", 64.0, "A_BALANCED", '', True)
        self.band_pass_filter_0.set_taps(firdes.complex_band_pass(1, self.adrx_samp_rate, 850e3+self.frx_if, 1.15e6+self.frx_if, 100e3, firdes.WIN_HAMMING, 6.76))
        self.analog_sig_source_x_0.set_sampling_freq(self.adrx_samp_rate)
        self.analog_pll_freqdet_cf_0_0.set_max_freq(20000*6.28/(self.adrx_samp_rate/self.bc_dec1))
        self.analog_pll_freqdet_cf_0_0.set_min_freq(0*6.28/(self.adrx_samp_rate/self.bc_dec1))
        self.analog_pll_freqdet_cf_0.set_max_freq(self.tm_channel_bw*6.28/(self.adrx_samp_rate/self.tm_dec1))
        self.analog_pll_freqdet_cf_0.set_min_freq(-self.tm_channel_bw*6.28/(self.adrx_samp_rate/self.tm_dec1))

    def get_MTU(self):
        return self.MTU

    def set_MTU(self, MTU):
        self.MTU = MTU

    def get_tm_waterfall_per(self):
        return self.tm_waterfall_per

    def set_tm_waterfall_per(self, tm_waterfall_per):
        self.tm_waterfall_per = tm_waterfall_per
        Qt.QMetaObject.invokeMethod(self._tm_waterfall_per_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.tm_waterfall_per)))
        self.qtgui_waterfall_sink_x_0.set_update_time(self.tm_waterfall_per)

    def get_tm_ss_ted_gain_range(self):
        return self.tm_ss_ted_gain_range

    def set_tm_ss_ted_gain_range(self, tm_ss_ted_gain_range):
        self.tm_ss_ted_gain_range = tm_ss_ted_gain_range
        self.digital_symbol_sync_xx_0.set_ted_gain(self.tm_ss_ted_gain_range)

    def get_tm_ss_loopbw_range(self):
        return self.tm_ss_loopbw_range

    def set_tm_ss_loopbw_range(self, tm_ss_loopbw_range):
        self.tm_ss_loopbw_range = tm_ss_loopbw_range
        self.digital_symbol_sync_xx_0.set_loop_bandwidth(self.tm_ss_loopbw_range)

    def get_tm_ss_damping_factor_range(self):
        return self.tm_ss_damping_factor_range

    def set_tm_ss_damping_factor_range(self, tm_ss_damping_factor_range):
        self.tm_ss_damping_factor_range = tm_ss_damping_factor_range
        self.digital_symbol_sync_xx_0.set_damping_factor(self.tm_ss_damping_factor_range)

    def get_tm_pll_loopbw_range(self):
        return self.tm_pll_loopbw_range

    def set_tm_pll_loopbw_range(self, tm_pll_loopbw_range):
        self.tm_pll_loopbw_range = tm_pll_loopbw_range
        self.analog_pll_freqdet_cf_0.set_loop_bandwidth(self.tm_pll_loopbw_range)

    def get_tm_gain_before_tr(self):
        return self.tm_gain_before_tr

    def set_tm_gain_before_tr(self, tm_gain_before_tr):
        self.tm_gain_before_tr = tm_gain_before_tr
        self.blocks_multiply_const.set_k((self.tm_gain_before_tr, ))

    def get_tm_channel_bw(self):
        return self.tm_channel_bw

    def set_tm_channel_bw(self, tm_channel_bw):
        self.tm_channel_bw = tm_channel_bw
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.adrx_samp_rate, self.tm_channel_bw, self.tm_channel_bw/20, firdes.WIN_HAMMING, 6.76))
        self.analog_pll_freqdet_cf_0.set_max_freq(self.tm_channel_bw*6.28/(self.adrx_samp_rate/self.tm_dec1))
        self.analog_pll_freqdet_cf_0.set_min_freq(-self.tm_channel_bw*6.28/(self.adrx_samp_rate/self.tm_dec1))

    def get_dec_cc(self):
        return self.dec_cc

    def set_dec_cc(self, dec_cc):
        self.dec_cc = dec_cc

    def get_bc_waterfall_per(self):
        return self.bc_waterfall_per

    def set_bc_waterfall_per(self, bc_waterfall_per):
        self.bc_waterfall_per = bc_waterfall_per
        Qt.QMetaObject.invokeMethod(self._bc_waterfall_per_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.bc_waterfall_per)))

    def get_bc_ss_ted_gain_range(self):
        return self.bc_ss_ted_gain_range

    def set_bc_ss_ted_gain_range(self, bc_ss_ted_gain_range):
        self.bc_ss_ted_gain_range = bc_ss_ted_gain_range
        self.digital_symbol_sync_xx_0_0.set_ted_gain(self.bc_ss_ted_gain_range)

    def get_bc_ss_loopbw_range(self):
        return self.bc_ss_loopbw_range

    def set_bc_ss_loopbw_range(self, bc_ss_loopbw_range):
        self.bc_ss_loopbw_range = bc_ss_loopbw_range
        self.digital_symbol_sync_xx_0_0.set_loop_bandwidth(self.bc_ss_loopbw_range)

    def get_bc_ss_damping_factor_range(self):
        return self.bc_ss_damping_factor_range

    def set_bc_ss_damping_factor_range(self, bc_ss_damping_factor_range):
        self.bc_ss_damping_factor_range = bc_ss_damping_factor_range
        self.digital_symbol_sync_xx_0_0.set_damping_factor(self.bc_ss_damping_factor_range)

    def get_bc_rrc_dec(self):
        return self.bc_rrc_dec

    def set_bc_rrc_dec(self, bc_rrc_dec):
        self.bc_rrc_dec = bc_rrc_dec

    def get_bc_pll_loopbw_range(self):
        return self.bc_pll_loopbw_range

    def set_bc_pll_loopbw_range(self, bc_pll_loopbw_range):
        self.bc_pll_loopbw_range = bc_pll_loopbw_range
        self.analog_pll_freqdet_cf_0_0.set_loop_bandwidth(self.bc_pll_loopbw_range)

    def get_bc_gain_before_tr(self):
        return self.bc_gain_before_tr

    def set_bc_gain_before_tr(self, bc_gain_before_tr):
        self.bc_gain_before_tr = bc_gain_before_tr
        self.blocks_multiply_const_0.set_k((self.bc_gain_before_tr, ))

    def get_bc_filt_sharp(self):
        return self.bc_filt_sharp

    def set_bc_filt_sharp(self, bc_filt_sharp):
        self.bc_filt_sharp = bc_filt_sharp
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.adrx_samp_rate, self.bc_channel_bw, self.bc_channel_bw/self.bc_filt_sharp, firdes.WIN_HAMMING, 6.76))

    def get_bc_dec1(self):
        return self.bc_dec1

    def set_bc_dec1(self, bc_dec1):
        self.bc_dec1 = bc_dec1
        self.root_raised_cosine_filter_0.set_taps(firdes.root_raised_cosine(1, self.adrx_samp_rate/self.bc_dec1, self.bc_symb_rate, 0.7, 32))
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.adrx_samp_rate/self.bc_dec1)
        self.analog_pll_freqdet_cf_0_0.set_max_freq(20000*6.28/(self.adrx_samp_rate/self.bc_dec1))
        self.analog_pll_freqdet_cf_0_0.set_min_freq(0*6.28/(self.adrx_samp_rate/self.bc_dec1))

    def get_bc_channel_bw(self):
        return self.bc_channel_bw

    def set_bc_channel_bw(self, bc_channel_bw):
        self.bc_channel_bw = bc_channel_bw
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.adrx_samp_rate, self.bc_channel_bw, self.bc_channel_bw/self.bc_filt_sharp, firdes.WIN_HAMMING, 6.76))

    def get_adrx_channel_bw(self):
        return self.adrx_channel_bw

    def set_adrx_channel_bw(self, adrx_channel_bw):
        self.adrx_channel_bw = adrx_channel_bw
        self.iio_fmcomms2_source_0.set_params(self.ad9361rx_lo_freq-self.frx_if, self.adrx_samp_rate, self.adrx_channel_bw*5, True, True, True, "fast_attack", 64.0, "manual", 64.0, "A_BALANCED", '', True)

    def get_ad9361rx_lo_freq(self):
        return self.ad9361rx_lo_freq

    def set_ad9361rx_lo_freq(self, ad9361rx_lo_freq):
        self.ad9361rx_lo_freq = ad9361rx_lo_freq
        Qt.QMetaObject.invokeMethod(self._ad9361rx_lo_freq_line_edit, "setText", Qt.Q_ARG("QString", str(self.ad9361rx_lo_freq)))
        self.iio_fmcomms2_source_0.set_params(self.ad9361rx_lo_freq-self.frx_if, self.adrx_samp_rate, self.adrx_channel_bw*5, True, True, True, "fast_attack", 64.0, "manual", 64.0, "A_BALANCED", '', True)


def main(top_block_cls=tbhp, options=None):

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
