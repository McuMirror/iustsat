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

#ifndef INCLUDED_IUSTSAT_SYNCH_DETECT_TAG2_IMPL_H
#define INCLUDED_IUSTSAT_SYNCH_DETECT_TAG2_IMPL_H

#include <iustsat/synch_detect_tag2.h>

namespace gr {
  namespace iustsat {

    class synch_detect_tag2_impl : public synch_detect_tag2
    {
     private:
       unsigned d_threshold;
       pmt::pmt_t d_length_key;
       pmt::pmt_t d_length;

     public:
      synch_detect_tag2_impl(float threshold, const std::string &length_key, unsigned length);
      ~synch_detect_tag2_impl();

      // Where all the action really happens
      void forecast (int noutput_items, gr_vector_int &ninput_items_required);

      int general_work(int noutput_items,
           gr_vector_int &ninput_items,
           gr_vector_const_void_star &input_items,
           gr_vector_void_star &output_items);
    };

  } // namespace iustsat
} // namespace gr

#endif /* INCLUDED_IUSTSAT_SYNCH_DETECT_TAG2_IMPL_H */
