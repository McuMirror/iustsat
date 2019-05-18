/* -*- c++ -*- */
/*
 * Copyright 2019 IUST.
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
#include "zafar_telemetry_rx_impl.h"
#include <pmt/pmt.h>
#include <gnuradio/tags.h>
#include <iostream>

using namespace std;

namespace gr {
  namespace iustsat {

    zafar_telemetry_rx::sptr
    zafar_telemetry_rx::make()
    {
      return gnuradio::get_initial_sptr
        (new zafar_telemetry_rx_impl());
    }

    /*
     * The private constructor
     */
    zafar_telemetry_rx_impl::zafar_telemetry_rx_impl()
      : gr::block("zafar_telemetry_rx",
        gr::io_signature::make(1, 1, sizeof(float)),
        gr::io_signature::make(1, 1, sizeof(float)))
    {}

    /*
     * Our virtual destructor.
     */
    zafar_telemetry_rx_impl::~zafar_telemetry_rx_impl()
    {
    }

    void
    zafar_telemetry_rx_impl::forecast (int noutput_items, gr_vector_int &ninput_items_required)
    {
      unsigned ninputs = ninput_items_required.size ();
      for(unsigned i = 0; i < ninputs; i++)
        ninput_items_required[i] = noutput_items;
    }

    int
    zafar_telemetry_rx_impl::general_work (int noutput_items,
                       gr_vector_int &ninput_items,
                       gr_vector_const_void_star &input_items,
                       gr_vector_void_star &output_items)
    {
      const float *in = (const float *) input_items[0];
      float *out = (float *) output_items[0];

      pmt::pmt_t key = pmt::intern("key");
      pmt::pmt_t value = pmt::from_double(1000);

      gr::tag_t tag;

      tag.key = pmt::intern("key2");
      tag.value = pmt::from_double(1001);

      for (int i = 0;i < noutput_items;i++) {
        out[i] = in[i];
        if (!((nitems_written(0) + i) % 1000)) {
          //add_item_tag(0, nitems_written(0) + i, key, value);
          tag.offset = nitems_written(0) + i;
          add_item_tag(0, (const tag_t)tag);
        }
      }



      // Do <+signal processing+>
      // Tell runtime system how many input items we consumed on
      // each input stream.
      consume_each (noutput_items);

      // Tell runtime system how many output items we produced.
      return noutput_items;
    }

  } /* namespace iustsat */
} /* namespace gr */
