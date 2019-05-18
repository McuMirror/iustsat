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

#ifndef INCLUDED_IUSTSAT_TAG_COUNTER_IMPL_H
#define INCLUDED_IUSTSAT_TAG_COUNTER_IMPL_H

#include <iustsat/tag_counter.h>
#include "boost/date_time/posix_time/posix_time.hpp"

namespace gr {
  namespace iustsat {

    class tag_counter_impl : public tag_counter
    {
     private:
      int d_cnt;
      pmt::pmt_t d_key;
      //std::chrono::time_point<std::chrono::system_clock> d_start_time;
      unsigned d_frame_cnt;
      int d_rate;
      boost::posix_time::ptime d_startTime;
      unsigned d_cnt_temp;

     public:
      tag_counter_impl(const std::string &key);
      ~tag_counter_impl();

      // Where all the action really happens
      void forecast (int noutput_items, gr_vector_int &ninput_items_required);

      int general_work(int noutput_items,
           gr_vector_int &ninput_items,
           gr_vector_const_void_star &input_items,
           gr_vector_void_star &output_items);
    };

  } // namespace iustsat
} // namespace gr

#endif /* INCLUDED_IUSTSAT_TAG_COUNTER_IMPL_H */
