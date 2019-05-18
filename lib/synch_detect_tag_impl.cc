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
#include "synch_detect_tag_impl.h"

namespace gr {
  namespace iustsat {

    synch_detect_tag::sptr
    synch_detect_tag::make(float threshold, const std::string &length_key, unsigned length)
    {
      return gnuradio::get_initial_sptr
        (new synch_detect_tag_impl(threshold, length_key, length));
    }

    /*
     * The private constructor
     */
    synch_detect_tag_impl::synch_detect_tag_impl(float threshold, const std::string &length_key, unsigned length)
      : gr::sync_block("synch_detect_tag",
              gr::io_signature::make(2, 2, sizeof(float)),
              gr::io_signature::make(1, 1, sizeof(float)))
    {
      d_threshold = threshold;
      d_length_key = pmt::string_to_symbol(length_key);
      d_length = pmt::from_long(length);
    }

    /*
     * Our virtual destructor.
     */
    synch_detect_tag_impl::~synch_detect_tag_impl()
    {
    }

    int
    synch_detect_tag_impl::work(int noutput_items,
        gr_vector_const_void_star &input_items,
        gr_vector_void_star &output_items)
    {
      const float *in_samp = (const float *) input_items[0];
      const float *in_mch = (const float *) input_items[1];
      float *out = (float *) output_items[0];


      for (int i = 0;i < noutput_items;i++) {
        out[i] = in_samp[i];
        if (in_mch[i] >= d_threshold) {
            add_item_tag(0, nitems_written(0)+i, d_length_key, d_length);
        }
      }

      // Tell runtime system how many output items we produced.
      return noutput_items;
    }

  } /* namespace iustsat */
} /* namespace gr */
