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


#ifndef INCLUDED_IUSTSAT_ZAFAR_TELEMETRY_DERAND_H
#define INCLUDED_IUSTSAT_ZAFAR_TELEMETRY_DERAND_H

#include <iustsat/api.h>
#include <gnuradio/block.h>

namespace gr {
  namespace iustsat {

    /*!
     * \brief <+description of block+>
     * \ingroup iustsat
     *
     */
    class IUSTSAT_API zafar_telemetry_derand : virtual public gr::block
    {
     public:
      typedef boost::shared_ptr<zafar_telemetry_derand> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of iustsat::zafar_telemetry_derand.
       *
       * To avoid accidental use of raw pointers, iustsat::zafar_telemetry_derand's
       * constructor is in a private implementation
       * class. iustsat::zafar_telemetry_derand::make is the public interface for
       * creating new instances.
       */
      static sptr make(const std::string &pkt_len_key);
    };

  } // namespace iustsat
} // namespace gr

#endif /* INCLUDED_IUSTSAT_ZAFAR_TELEMETRY_DERAND_H */
