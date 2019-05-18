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
#include "zafar_telemetry_deinterleave_impl.h"
#include <stdio.h>

namespace gr {
  namespace iustsat {

    zafar_telemetry_deinterleave::sptr
    zafar_telemetry_deinterleave::make(const std::string &pkt_len_key)
    {
      return gnuradio::get_initial_sptr
        (new zafar_telemetry_deinterleave_impl(pkt_len_key));
    }

    /*
     * The private constructor
     */
    zafar_telemetry_deinterleave_impl::zafar_telemetry_deinterleave_impl(const std::string &pkt_len_key)
      : gr::block("zafar_telemetry_deinterleave",
              gr::io_signature::make(0, 0, 0),
              gr::io_signature::make(0, 0, 0))
    {
      message_port_register_in(pmt::mp("in"));
      message_port_register_out(pmt::mp("out"));

      set_msg_handler(
        pmt::mp("in"),
        boost::bind(&zafar_telemetry_deinterleave_impl::msg_handler, this, _1)
      );

      d_len_tag_key = pmt::string_to_symbol(pkt_len_key);
    }

    /*
     * Our virtual destructor.
     */
    zafar_telemetry_deinterleave_impl::~zafar_telemetry_deinterleave_impl()
    {
    }

    void
    zafar_telemetry_deinterleave_impl::forecast (int noutput_items, gr_vector_int &ninput_items_required)
    {
      unsigned ninputs = ninput_items_required.size ();
      for(unsigned i = 0; i < ninputs; i++)
        ninput_items_required[i] = noutput_items;
    }

    int
    zafar_telemetry_deinterleave_impl::general_work (int noutput_items,
                       gr_vector_int &ninput_items,
                       gr_vector_const_void_star &input_items,
                       gr_vector_void_star &output_items)
    {
      // Do <+signal processing+>
      // Tell runtime system how many input items we consumed on
      // each input stream.
      consume_each (noutput_items);

      // Tell runtime system how many output items we produced.
      return noutput_items;
    }

    void zafar_telemetry_deinterleave_impl::msg_handler(pmt::pmt_t msg) {
      //check PDU
      if (!pmt::is_pair(msg)) {
        throw std::runtime_error("zafar_telemetry_deinterleave_impl received non PDU input");
      }
      pmt::pmt_t meta = pmt::car(msg);
      pmt::pmt_t data = pmt::cdr(msg);

      if (pmt::is_null(meta)) {
        meta = pmt::make_dict();
      } else if (!pmt::is_dict(meta)) {
        throw std::runtime_error("zafar_telemetry_deinterleave_impl received non PDU input");
      }

      pmt::pmt_t pkt_len = pmt::dict_ref(meta, d_len_tag_key, pmt::PMT_F);
      int len = pmt::to_long(pkt_len);
      if (len % 255) {
        throw std::runtime_error("zafar_telemetry_deinterleave_impl not a valid packet length");
      }
      len /= 5; // 5: interleaving depth

      meta = pmt::make_dict();
      meta = dict_add(meta, d_len_tag_key, pmt::from_long(len));
      pmt::pmt_t vector1 = pmt::PMT_NIL;
      pmt::pmt_t vector2 = pmt::PMT_NIL;
      pmt::pmt_t vector3 = pmt::PMT_NIL;
      pmt::pmt_t vector4 = pmt::PMT_NIL;
      pmt::pmt_t vector5 = pmt::PMT_NIL;
      vector1 = pmt::make_u8vector(len, 0);
      vector2 = pmt::make_u8vector(len, 0);
      vector3 = pmt::make_u8vector(len, 0);
      vector4 = pmt::make_u8vector(len, 0);
      vector5 = pmt::make_u8vector(len, 0);

      
      for (int i = 0;i < len;i++) {
        pmt::u8vector_set(vector1, i, pmt::u8vector_ref(data, 0*255+i));
      }
      pmt::pmt_t msg1 = pmt::cons(meta, vector1);
      message_port_pub(pmt::mp("out"), msg1);

      for (int i = 0;i < len;i++) {
        pmt::u8vector_set(vector2, i, pmt::u8vector_ref(data, 1*255+i));
      }
      pmt::pmt_t msg2 = pmt::cons(meta, vector2);
      message_port_pub(pmt::mp("out"), msg2);

      for (int i = 0;i < len;i++) {
        pmt::u8vector_set(vector3, i, pmt::u8vector_ref(data, 2*255+i));
      }
      pmt::pmt_t msg3 = pmt::cons(meta, vector3);
      message_port_pub(pmt::mp("out"), msg3);

      for (int i = 0;i < len;i++) {
        pmt::u8vector_set(vector4, i, pmt::u8vector_ref(data, 3*255+i));
      }
      pmt::pmt_t msg4 = pmt::cons(meta, vector4);
      message_port_pub(pmt::mp("out"), msg4);

      for (int i = 0;i < len;i++) {
        pmt::u8vector_set(vector5, i, pmt::u8vector_ref(data, 4*255+i));
      }
      pmt::pmt_t msg5 = pmt::cons(meta, vector5);
      message_port_pub(pmt::mp("out"), msg5);
    }
  } /* namespace iustsat */
} /* namespace gr */

