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
#include "zafar_telemetry_frame_extractor_impl.h"
#include <gnuradio/tags.h>
#include <stdio.h>
#include <pmt/pmt.h>


namespace gr {
  namespace iustsat {

    zafar_telemetry_frame_extractor::sptr
    zafar_telemetry_frame_extractor::make(const std::string &length_key)
    {
      return gnuradio::get_initial_sptr
        (new zafar_telemetry_frame_extractor_impl(length_key));
    }

    /*
     * The private constructor
     */
    zafar_telemetry_frame_extractor_impl::zafar_telemetry_frame_extractor_impl(const std::string &length_key)
      : gr::block("zafar_telemetry_frame_extractor",
              gr::io_signature::make(1, 1, sizeof(float)),
              gr::io_signature::make(0, 0, 0))
    {
      set_tag_propagation_policy(TPP_DONT);
      message_port_register_out(pmt::mp("out"));
      d_meta = pmt::PMT_NIL;
      d_vector = pmt::PMT_NIL;
      d_key = pmt::string_to_symbol(length_key);
      d_currFrameLen = 0;
      d_state = STATE_TAG_SEARCH;
      d_frm_cnt = 0;
    }

    /*
     * Our virtual destructor.
     */
    zafar_telemetry_frame_extractor_impl::~zafar_telemetry_frame_extractor_impl()
    {
    }

    void
    zafar_telemetry_frame_extractor_impl::forecast (int noutput_items, gr_vector_int &ninput_items_required)
    {
      unsigned ninputs = ninput_items_required.size();
      for(unsigned i = 0; i < ninputs; i++)
        ninput_items_required[i] = noutput_items;
    }

    int
    zafar_telemetry_frame_extractor_impl::general_work (int noutput_items,
                       gr_vector_int &ninput_items,
                       gr_vector_const_void_star &input_items,
                       gr_vector_void_star &output_items)
    {
      const float *in = (const float *) input_items[0];
      std::vector<gr::tag_t> tags;
      uint64_t nitem = nitems_read(0);
      int count = 0;
      int i = 0;


      while (count < noutput_items) {
        switch (d_state) {
          case STATE_TAG_SEARCH:
            //printf("STATE_TAG_SEARCH\n");
            get_tags_in_range(tags, 0, nitem, nitem + ninput_items[0], d_key);

            if (tags.size()) {
              d_state = STATE_INIT_MESSAGE;
              break;
            }
            count = noutput_items;
            break;
          case STATE_INIT_MESSAGE:
            //printf("STATE_INIT_MESSAGE\n");
            count = tags[i].offset - nitem;
            d_currFrameLen = pmt::to_long(tags[i].value);
            d_vector = pmt::make_f32vector(d_currFrameLen, 0);
            d_meta = pmt::make_dict();
            d_meta = dict_add(d_meta, tags[i].key, tags[i].value);
            d_state = STATE_BUFF_FRAME;
            break;
          case STATE_BUFF_FRAME:
            //printf("STATE_BUFF_FRAME\n");
            while (count < noutput_items) {
              pmt::f32vector_set(d_vector, d_frm_cnt, in[count++]);
              if (++d_frm_cnt >= d_currFrameLen) {
                d_frm_cnt = 0;
                d_state = STATE_MESSAGE_PUB;
                break;
              }
            }
            break;
          case STATE_MESSAGE_PUB:
            //printf("STATE_MESSAGE_PUB\n");
            pmt::pmt_t msg = pmt::cons(d_meta, d_vector);
            message_port_pub(pmt::mp("out"), msg);

            if (tags.size()){
              if (++i < tags.size()) {
                d_state = STATE_INIT_MESSAGE;
              } else {
                count = noutput_items;
                d_state = STATE_TAG_SEARCH;
              }
            } else {
              d_state = STATE_TAG_SEARCH;
            }
            break;
        }
      }

      // Tell runtime system how many input items we consumed on
      // each input stream.
      consume_each (noutput_items);

      // Tell runtime system how many output items we produced.
      return 0;
    }

  } /* namespace iustsat */
} /* namespace gr */
