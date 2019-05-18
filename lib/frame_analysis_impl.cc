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
#include "frame_analysis_impl.h"
#include <stdio.h>

namespace gr {
  namespace iustsat {

    frame_analysis::sptr
    frame_analysis::make(const std::string &len_tag_key)
    {
      return gnuradio::get_initial_sptr
        (new frame_analysis_impl(len_tag_key));
    }

    /*
     * The private constructor
     */
    frame_analysis_impl::frame_analysis_impl(const std::string &len_tag_key)
      : gr::block("frame_analysis",
              gr::io_signature::make(0, 0, 0),
              gr::io_signature::make(0, 0, 0))
    {
      message_port_register_in(pmt::mp("in"));
      message_port_register_out(pmt::mp("out"));

      set_msg_handler(
        pmt::mp("in"),
        boost::bind(&frame_analysis_impl::msg_handler, this, _1)
      );

      d_len_tag_key = pmt::intern(len_tag_key);
      d_frame_cnt = 0;
    }

    /*
     * Our virtual destructor.
     */
    frame_analysis_impl::~frame_analysis_impl()
    {
    }

    void
    frame_analysis_impl::forecast (int noutput_items, gr_vector_int &ninput_items_required)
    {
      unsigned ninputs = ninput_items_required.size ();
      for(unsigned i = 0; i < ninputs; i++)
        ninput_items_required[i] = noutput_items;
    }

    int
    frame_analysis_impl::general_work (int noutput_items,
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

    void frame_analysis_impl::msg_handler(pmt::pmt_t msg) {
      d_frame_cnt++;
      //pmt::pmt_t data2 = pmt::cdr(msg);
      //printf("data len: %d\n", (int)length(data2));
      pmt::pmt_t meta = pmt::make_dict();
      meta = dict_add(meta, d_len_tag_key, pmt::from_long(4));
      pmt::pmt_t data = pmt::make_f32vector(1, d_frame_cnt);
      pmt::pmt_t msg2 = pmt::cons(meta, data);
      message_port_pub(pmt::mp("out"), msg2);
    }

  } /* namespace iustsat */
} /* namespace gr */
