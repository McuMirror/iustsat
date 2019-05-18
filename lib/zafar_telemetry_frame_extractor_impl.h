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

#ifndef INCLUDED_IUSTSAT_ZAFAR_TELEMETRY_FRAME_EXTRACTOR_IMPL_H
#define INCLUDED_IUSTSAT_ZAFAR_TELEMETRY_FRAME_EXTRACTOR_IMPL_H

#include <iustsat/zafar_telemetry_frame_extractor.h>


namespace gr {
  namespace iustsat {

    class zafar_telemetry_frame_extractor_impl : public zafar_telemetry_frame_extractor
    {
     private:
      unsigned d_currFrameLen;
      pmt::pmt_t           d_meta;
      pmt::pmt_t           d_vector;
      pmt::pmt_t           d_key;
      enum state_t {STATE_TAG_SEARCH, STATE_INIT_MESSAGE, STATE_BUFF_FRAME, STATE_MESSAGE_PUB};
      state_t d_state;
      unsigned d_frm_cnt;

     public:
      zafar_telemetry_frame_extractor_impl(const std::string &length_key);
      ~zafar_telemetry_frame_extractor_impl();

      // Where all the action really happens
      void forecast (int noutput_items, gr_vector_int &ninput_items_required);

      int general_work(int noutput_items,
           gr_vector_int &ninput_items,
           gr_vector_const_void_star &input_items,
           gr_vector_void_star &output_items);
    };

  } // namespace iustsat
} // namespace gr

#endif /* INCLUDED_IUSTSAT_ZAFAR_TELEMETRY_FRAME_EXTRACTOR_IMPL_H */
