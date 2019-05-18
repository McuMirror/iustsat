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
#include "pdu_debug_impl.h"
#include <iostream>
#include <stdio.h>

namespace gr {
  namespace iustsat {

    pdu_debug::sptr
    pdu_debug::make(const std::string &meta_tag_key)
    {
      return gnuradio::get_initial_sptr
        (new pdu_debug_impl(meta_tag_key));
    }

    /*
     * The private constructor
     */
    pdu_debug_impl::pdu_debug_impl(const std::string &meta_tag_key)
      : gr::block("pdu_debug",
              gr::io_signature::make(0, 0, 0),
              gr::io_signature::make(0, 0, 0))
    {
      message_port_register_in(pmt::mp("pdu_in"));

      set_msg_handler(
        pmt::mp("pdu_in"),
        boost::bind(&pdu_debug_impl::msg_handler, this, _1)
      );


      d_meta_tag_key = pmt::string_to_symbol(meta_tag_key);
    }

    /*
     * Our virtual destructor.
     */
    pdu_debug_impl::~pdu_debug_impl()
    {
    }

    void
    pdu_debug_impl::forecast (int noutput_items, gr_vector_int &ninput_items_required)
    {
      unsigned ninputs = ninput_items_required.size ();
      for(unsigned i = 0; i < ninputs; i++)
        ninput_items_required[i] = noutput_items;
    }

    int
    pdu_debug_impl::general_work (int noutput_items,
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

    void pdu_debug_impl::msg_handler(pmt::pmt_t msg) {
      //check PDU
      if (!pmt::is_pair(msg)) {
        throw std::runtime_error("pdu_debug received non PDU input");
      }
      pmt::pmt_t meta = pmt::car(msg);
      pmt::pmt_t data_pmt = pmt::cdr(msg);

      if (!pmt::is_dict(meta)) {
        throw std::runtime_error("pdu_debug received non dictionary in meta data");
      }

      std::cout << "******** PDU DEBUG PRINT **********\n";
      std::cout << "******** META PRINT ***************\n";
      pmt::pmt_t meta_data_pmt = pmt::dict_ref(meta, d_meta_tag_key, pmt::PMT_F);
      if (meta_data_pmt != pmt::PMT_F) {
        pmt::print(d_meta_tag_key);
        if (pmt::equal(meta_data_pmt, pmt::PMT_F) || pmt::equal(meta_data_pmt, pmt::PMT_T)) {
          if (pmt::equal(meta_data_pmt, pmt::PMT_T)) {
            printf("True\n");
          } else {
            printf("False\n");
          }
        } else {
          size_t meta_data_len = pmt::length(meta_data_pmt);
          const unsigned char *meta_data = u8vector_elements(meta_data_pmt, meta_data_len);
          for(size_t i=0;i<meta_data_len;i+=16){
            printf("%04x: ", ((unsigned int)i));
            for(size_t j=i;j<std::min(i+16,meta_data_len);j++){
              printf("%02x ",meta_data[j] );
            }
            std::cout << std::endl;
          }
        }
      }



      std::cout << "******** DATA PRINT ***************\n";
      size_t data_len = pmt::length(data_pmt);
      const unsigned char *data = (const unsigned char *) uniform_vector_elements(data_pmt, data_len);
      for(size_t i=0;i<data_len;i+=16){
        printf("%04x: ", ((unsigned int)i));
        for(size_t j=i;j<std::min(i+16,data_len);j++){
          printf("%02x ",data[j] );
        }
        std::cout << std::endl;
      }

      std::cout << "***********************************\n";
    }


  } /* namespace iustsat */
} /* namespace gr */
