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
#include <stdio.h>
#include "tag_counter_impl.h"

namespace gr {
  namespace iustsat {

    tag_counter::sptr
    tag_counter::make(const std::string &key)
    {
      return gnuradio::get_initial_sptr
        (new tag_counter_impl(key));
    }

    /*
     * The private constructor
     */
    tag_counter_impl::tag_counter_impl(const std::string &key)
      : gr::block("tag_counter",
              gr::io_signature::make(1, 1, sizeof(float)),
              gr::io_signature::make(2, 2, sizeof(float)))
    {
      d_cnt = 0;
      d_key = pmt::intern(key);
      d_frame_cnt = 0;
      d_rate = 0;
      d_startTime = boost::posix_time::microsec_clock::local_time();
      d_cnt_temp = 0;
    }

    /*
     * Our virtual destructor.
     */
    tag_counter_impl::~tag_counter_impl()
    {
    }

    void
    tag_counter_impl::forecast (int noutput_items, gr_vector_int &ninput_items_required)
    {
      unsigned ninputs = ninput_items_required.size ();
      for(unsigned i = 0; i < ninputs; i++)
        ninput_items_required[i] = noutput_items;
    }

    int
    tag_counter_impl::general_work (int noutput_items,
                       gr_vector_int &ninput_items,
                       gr_vector_const_void_star &input_items,
                       gr_vector_void_star &output_items)
    {
      const float *in = (const float *) input_items[0];
      float *out = (float *) output_items[0];
      float *out_rate = (float *) output_items[1];
      std::vector<gr::tag_t> tags;
      uint64_t nitem = nitems_read(0);
      int j = 0;

      get_tags_in_range(tags, 0, nitem, nitem+ninput_items[0], d_key);

      for(int i = 0;i < noutput_items;i++) {
        if (j < tags.size()) {
          if (tags[j].key != pmt::PMT_NIL && (nitem+i) >= tags[j].offset) {
            d_cnt++;
            j++;
          }
        }

        out[i] = d_cnt;
        out_rate[i] = d_rate;
      }

      boost::posix_time::ptime t2 = boost::posix_time::microsec_clock::local_time();
      boost::posix_time::time_duration diff = t2 - d_startTime;
      if (diff.total_milliseconds() > 1000) {
        d_rate = (d_cnt - d_cnt_temp)*259*8*2/(diff.total_milliseconds()/1000);
        d_startTime = boost::posix_time::microsec_clock::local_time();
        d_cnt_temp = d_cnt;
      }

      // Tell runtime system how many input items we consumed on
      // each input stream.
      consume_each (noutput_items);

      // Tell runtime system how many output items we produced.
      return noutput_items;
    }

  } /* namespace iustsat */
} /* namespace gr */
