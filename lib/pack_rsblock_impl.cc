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
#include "pack_rsblock_impl.h"

namespace gr {
  namespace iustsat {

    pack_rsblock::sptr
    pack_rsblock::make(const std::string &pkt_len_key)
    {
      return gnuradio::get_initial_sptr
        (new pack_rsblock_impl(pkt_len_key));
    }

    /*
     * The private constructor
     */
    pack_rsblock_impl::pack_rsblock_impl(const std::string &pkt_len_key)
      : gr::block("pack_rsblock",
              gr::io_signature::make(0, 0, 0),
              gr::io_signature::make(0, 0, 0))
    {
      message_port_register_in(pmt::mp("in"));
      message_port_register_out(pmt::mp("out"));

      set_msg_handler(
        pmt::mp("in"),
        boost::bind(&pack_rsblock_impl::msg_handler, this, _1)
      );

      d_len_tag_key = pmt::string_to_symbol(pkt_len_key);
      d_block_counter = 0;
    }

    /*
     * Our virtual destructor.
     */
    pack_rsblock_impl::~pack_rsblock_impl()
    {
    }

    void
    pack_rsblock_impl::forecast (int noutput_items, gr_vector_int &ninput_items_required)
    {
      unsigned ninputs = ninput_items_required.size ();
      for(unsigned i = 0; i < ninputs; i++)
        ninput_items_required[i] = noutput_items;
    }

    int
    pack_rsblock_impl::general_work (int noutput_items,
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

    void pack_rsblock_impl::msg_handler(pmt::pmt_t msg) {
      //check PDU
      if (!pmt::is_pair(msg)) {
        throw std::runtime_error("pack_rsblock_impl received non PDU input");
      }
      pmt::pmt_t meta = pmt::car(msg);
      pmt::pmt_t data = pmt::cdr(msg);

      if (pmt::is_null(meta)) {
        meta = pmt::make_dict();
      } else if (!pmt::is_dict(meta)) {
        throw std::runtime_error("pack_rsblock_impl received non PDU input");
      }

      for (int i = 0;i < 223;i++) {
        d_block_buff[d_block_counter*223 + i] = pmt::u8vector_ref(data, i);
      }

      if (++d_block_counter >= 5) {
        d_block_counter = 0;
        meta = pmt::make_dict();
        meta = dict_add(meta, d_len_tag_key, pmt::from_long(223*5));

        pmt::pmt_t vector = pmt::PMT_NIL;
        vector = pmt::make_u8vector(223*5, 0);

        for (int i = 0;i < 223*5;i++) {
          pmt::u8vector_set(vector, i, d_block_buff[i]);
        }

        pmt::pmt_t msg = pmt::cons(meta, vector);
        message_port_pub(pmt::mp("out"), msg);
      }
    }

  } /* namespace iustsat */
} /* namespace gr */

