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
#include "rs_to_decrypt_impl.h"
#include <stdio.h>

namespace gr {
  namespace iustsat {

    rs_to_decrypt::sptr
    rs_to_decrypt::make(const std::string &iv_key, std::vector<uint8_t> iv, const std::string &aad_key, const std::string &tag_key)
    {
      return gnuradio::get_initial_sptr
        (new rs_to_decrypt_impl(iv_key, iv, aad_key, tag_key));
    }

    /*
     * The private constructor
     */
    rs_to_decrypt_impl::rs_to_decrypt_impl(const std::string &iv_key, std::vector<uint8_t> iv, const std::string &aad_key, const std::string &tag_key)
      : gr::block("rs_to_decrypt",
              gr::io_signature::make(0, 0, 0),
              gr::io_signature::make(0, 0, 0))
    {
      message_port_register_in(pmt::mp("in"));
      message_port_register_out(pmt::mp("out"));

      set_msg_handler(
        pmt::mp("in"),
        boost::bind(&rs_to_decrypt_impl::msg_handler, this, _1)
      );

      d_aad_key = pmt::mp(aad_key);
      d_tag_key = pmt::mp(tag_key);
      d_iv_key = pmt::mp(iv_key);
      d_iv = pmt::init_u8vector(12, iv);
    }

    /*
     * Our virtual destructor.
     */
    rs_to_decrypt_impl::~rs_to_decrypt_impl()
    {
    }

    void
    rs_to_decrypt_impl::forecast (int noutput_items, gr_vector_int &ninput_items_required)
    {
      unsigned ninputs = ninput_items_required.size ();
      for(unsigned i = 0; i < ninputs; i++)
        ninput_items_required[i] = noutput_items;
    }

    int
    rs_to_decrypt_impl::general_work (int noutput_items,
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

    void rs_to_decrypt_impl::msg_handler(pmt::pmt_t msg) {
      //check PDU
      if (!pmt::is_pair(msg)) {
        throw std::runtime_error("rs_to_decrypt received non PDU input");
      }
      pmt::pmt_t data = pmt::cdr(msg);
      int len = pmt::length(data);

      
      unsigned char *data_temp = new unsigned char[len];
      for (int i = 0;i < len;i++) {
        data_temp[i] = (unsigned char)pmt::u8vector_ref(data, (len-1)-i);
      }
      data = pmt::init_u8vector(len, data_temp);

      unsigned char *data2 = new unsigned char[len-20];
      for (int i = 0;i < (len-20);i++) {
        data2[i] = pmt::u8vector_ref(data, i);
      }

      unsigned char aad[16];
      for (int i = 0;i < 16;i++) {
        if (i < 4) {
          aad[i] = pmt::u8vector_ref(data, i+(len-20));
        } else {
          aad[i] = 0;
        }
      }

      unsigned char tag[16];
      for (int i = 0;i < 16;i++) {
        tag[i] = pmt::u8vector_ref(data, i+(len-16));
      }



      pmt::pmt_t meta = pmt::make_dict();
      meta = dict_add(meta, d_aad_key, pmt::init_u8vector(16, aad));
      meta = dict_add(meta, d_tag_key, pmt::init_u8vector(16, tag));
      meta = dict_add(meta, d_iv_key, d_iv);
      pmt::pmt_t data_pmt = pmt::init_u8vector(len-20, data2);

      pmt::pmt_t msg2 = pmt::cons(meta, data_pmt);
      message_port_pub(pmt::mp("out"), msg2);
      delete [] data2;
    }

  } /* namespace iustsat */
} /* namespace gr */
