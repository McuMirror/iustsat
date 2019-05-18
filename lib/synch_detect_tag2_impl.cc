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
#include "synch_detect_tag2_impl.h"

namespace gr {
  namespace iustsat {

    synch_detect_tag2::sptr
    synch_detect_tag2::make(float threshold, const std::string &length_key, unsigned length)
    {
      return gnuradio::get_initial_sptr
        (new synch_detect_tag2_impl(threshold, length_key, length));
    }

    /*
     * The private constructor
     */
    synch_detect_tag2_impl::synch_detect_tag2_impl(float threshold, const std::string &length_key, unsigned length)
      : gr::block("synch_detect_tag2",
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
    synch_detect_tag2_impl::~synch_detect_tag2_impl()
    {
    }

    void
    synch_detect_tag2_impl::forecast (int noutput_items, gr_vector_int &ninput_items_required)
    {
       // We need the same number of outputs as we need inputs
	     unsigned int input_required = noutput_items;

      	unsigned ninputs = ninput_items_required.size();
      	for(unsigned int i = 0; i < ninputs; i++)
       	    ninput_items_required[i] = input_required;
    }

    int
    synch_detect_tag2_impl::general_work (int noutput_items,
                       gr_vector_int &ninput_items,
                       gr_vector_const_void_star &input_items,
                       gr_vector_void_star &output_items)
    {
      const float *in_samp = (const float *) input_items[0];
      const float *in_mch = (const float *) input_items[1];
      float *out = (float *) output_items[0];

      //std::cout << noutput_items << std::endl;

      for (int i = 0;i < noutput_items;i++) {
        out[i] = in_samp[i];
        if (in_mch[i] >= d_threshold) {
          if (nitems_written(0)+i-63 > 0) {
            add_item_tag(0, nitems_written(0)+i-63, d_length_key, d_length);
            //std::cout << "tagged!" << std::endl;
          }

        }
      }

      // Tell runtime system how many input items we consumed on
      // each input stream.
      consume_each (noutput_items);

      // Tell runtime system how many output items we produced.
      return noutput_items;
    }

  } /* namespace iustsat */
} /* namespace gr */
