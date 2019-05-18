#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Tcp Sink Test
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
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import pmt
import sys
from gnuradio import qtgui


class tcp_sink_test(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Tcp Sink Test")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Tcp Sink Test")
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

        self.settings = Qt.QSettings("GNU Radio", "tcp_sink_test")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.meta_dict = meta_dict = pmt.make_dict()
        self.meta = meta = pmt.dict_add(meta_dict, pmt.intern("packet_len"), pmt.from_double(10))
        self.samp_rate = samp_rate = 32000
        self.data_pdu = data_pdu = pmt.cons(meta, pmt.make_s8vector(10, 0x30))

        ##################################################
        # Blocks
        ##################################################
        self.blocks_socket_pdu_0 = blocks.socket_pdu("TCP_CLIENT", '192.168.1.1', '56000', 10000, False)
        self.blocks_message_strobe_0 = blocks.message_strobe(data_pdu, 1000)



        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_message_strobe_0, 'strobe'), (self.blocks_socket_pdu_0, 'pdus'))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "tcp_sink_test")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_meta_dict(self):
        return self.meta_dict

    def set_meta_dict(self, meta_dict):
        self.meta_dict = meta_dict
        self.set_meta(pmt.dict_add(self.meta_dict, pmt.intern("packet_len"), pmt.from_double(10)))

    def get_meta(self):
        return self.meta

    def set_meta(self, meta):
        self.meta = meta
        self.set_data_pdu(pmt.cons(self.meta, pmt.make_s8vector(10, 0x30)))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

    def get_data_pdu(self):
        return self.data_pdu

    def set_data_pdu(self, data_pdu):
        self.data_pdu = data_pdu
        self.blocks_message_strobe_0.set_msg(self.data_pdu)


def main(top_block_cls=tcp_sink_test, options=None):

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
