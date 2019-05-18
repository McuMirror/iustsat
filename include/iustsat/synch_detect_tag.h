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


#ifndef INCLUDED_IUSTSAT_SYNCH_DETECT_TAG_H
#define INCLUDED_IUSTSAT_SYNCH_DETECT_TAG_H

#include <iustsat/api.h>
#include <gnuradio/sync_block.h>

namespace gr {
  namespace iustsat {

    /*!
     * \brief <+description of block+>
     * \ingroup iustsat
     *
     */
    class IUSTSAT_API synch_detect_tag : virtual public gr::sync_block
    {
     public:
      typedef boost::shared_ptr<synch_detect_tag> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of iustsat::synch_detect_tag.
       *
       * To avoid accidental use of raw pointers, iustsat::synch_detect_tag's
       * constructor is in a private implementation
       * class. iustsat::synch_detect_tag::make is the public interface for
       * creating new instances.
       */
      static sptr make(float threshold, const std::string &length_key, unsigned length);
    };

  } // namespace iustsat
} // namespace gr

#endif /* INCLUDED_IUSTSAT_SYNCH_DETECT_TAG_H */
