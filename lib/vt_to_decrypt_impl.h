/* -*- c++ -*- */
/* 
 * Copyright 2019 Armin Ghani (IUST).
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

#ifndef INCLUDED_IUSTSAT_VT_TO_DECRYPT_IMPL_H
#define INCLUDED_IUSTSAT_VT_TO_DECRYPT_IMPL_H

#include <iustsat/vt_to_decrypt.h>

namespace gr {
  namespace iustsat {

    class vt_to_decrypt_impl : public vt_to_decrypt
    {
     private:
      pmt::pmt_t d_aad_key;
      pmt::pmt_t d_tag_key;
      pmt::pmt_t d_iv_key;
      pmt::pmt_t d_iv;

     public:
      vt_to_decrypt_impl(const std::string &iv_key, std::vector<uint8_t> iv, const std::string &aad_key, const std::string &tag_key);
      ~vt_to_decrypt_impl();

      // Where all the action really happens
      void forecast (int noutput_items, gr_vector_int &ninput_items_required);

      int general_work(int noutput_items,
           gr_vector_int &ninput_items,
           gr_vector_const_void_star &input_items,
           gr_vector_void_star &output_items);

      void msg_handler(pmt::pmt_t msg);
    };

  } // namespace iustsat
} // namespace gr

#endif /* INCLUDED_IUSTSAT_VT_TO_DECRYPT_IMPL_H */

