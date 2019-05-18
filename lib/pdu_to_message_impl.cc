/* -*- c++ -*- */
/*
 * Copyright 2019 IUST (Armin Ghani).
 *
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 *
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <gnuradio/io_signature.h>
#include "pdu_to_message_impl.h"

namespace gr {
  namespace iustsat {

    pdu_to_message::sptr
    pdu_to_message::make(const std::string &len_tag_key)
    {
      return gnuradio::get_initial_sptr
        (new pdu_to_message_impl(len_tag_key));
    }

    /*
     * The private constructor
     */
    pdu_to_message_impl::pdu_to_message_impl(const std::string &len_tag_key)
      : gr::block("pdu_to_message",
              gr::io_signature::make(0, 0, 0),
              gr::io_signature::make(0, 0, 0))
    {
      message_port_register_in(pmt::mp("in"));
      message_port_register_out(pmt::mp("out"));

      set_msg_handler(
        pmt::mp("in"),
        boost::bind(&pdu_to_message_impl::msg_handler, this, _1)
      );

      d_len_tag_key = pmt::intern(len_tag_key);
    }

    /*
     * Our virtual destructor.
     */
    pdu_to_message_impl::~pdu_to_message_impl()
    {
    }

    void
    pdu_to_message_impl::forecast (int noutput_items, gr_vector_int &ninput_items_required)
    {
      unsigned ninputs = ninput_items_required.size ();
      for(unsigned i = 0; i < ninputs; i++)
        ninput_items_required[i] = noutput_items;
    }

    int
    pdu_to_message_impl::general_work (int noutput_items,
                       gr_vector_int &ninput_items,
                       gr_vector_const_void_star &input_items,
                       gr_vector_void_star &output_items)
    {

      // Tell runtime system how many input items we consumed on
      // each input stream.
      consume_each (noutput_items);

      // Tell runtime system how many output items we produced.
      return noutput_items;
    }

    void pdu_to_message_impl::msg_handler(pmt::pmt_t msg) {
      //check PDU
      if (!pmt::is_pair(msg)) {
        throw std::runtime_error("zafar_telemetry_derand received non PDU input");
      }
      pmt::pmt_t data = pmt::cdr(msg);
      int len = pmt::length(data);

      float *u8data = new float [len];
      for (int i = 0;i < len;i++) {
        u8data[i] = (float)pmt::u8vector_ref(data, i);
      }

      data = pmt::init_f32vector(len, u8data);
      pmt::pmt_t meta = pmt::make_dict();
      meta = dict_add(meta, d_len_tag_key, pmt::from_long(len*4));
      msg = pmt::cons(meta, data);
      message_port_pub(pmt::mp("out"), msg);
    }

  } /* namespace iustsat */
} /* namespace gr */
