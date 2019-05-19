/* -*- c++ -*- */

#define IUSTSAT_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "iustsat_swig_doc.i"

%{
#include "iustsat/zafar_telemetry_rx.h"
#include "iustsat/zafar_telemetry_frame_extractor.h"
#include "iustsat/zafar_telemetry_derand.h"
#include "iustsat/synch_detect_tag.h"
#include "iustsat/synch_detect_tag2.h"
#include "iustsat/test.h"
#include "iustsat/pdu_debug.h"
#include "iustsat/pdu_debug_2.h"
#include "iustsat/tag_counter.h"
#include "iustsat/rs_to_decrypt.h"
#include "iustsat/frame_analysis.h"
#include "iustsat/pdu_to_message.h"
#include "iustsat/zafar_telemetry_deinterleave.h"
#include "iustsat/pack_rsblock.h"
#include "iustsat/vt_to_decrypt.h"
%}


%include "iustsat/zafar_telemetry_rx.h"
GR_SWIG_BLOCK_MAGIC2(iustsat, zafar_telemetry_rx);
%include "iustsat/zafar_telemetry_frame_extractor.h"
GR_SWIG_BLOCK_MAGIC2(iustsat, zafar_telemetry_frame_extractor);
%include "iustsat/zafar_telemetry_derand.h"
GR_SWIG_BLOCK_MAGIC2(iustsat, zafar_telemetry_derand);

%include "iustsat/synch_detect_tag.h"
GR_SWIG_BLOCK_MAGIC2(iustsat, synch_detect_tag);
%include "iustsat/synch_detect_tag2.h"
GR_SWIG_BLOCK_MAGIC2(iustsat, synch_detect_tag2);

%include "iustsat/test.h"
GR_SWIG_BLOCK_MAGIC2(iustsat, test);
%include "iustsat/pdu_debug.h"
GR_SWIG_BLOCK_MAGIC2(iustsat, pdu_debug);
%include "iustsat/pdu_debug_2.h"
GR_SWIG_BLOCK_MAGIC2(iustsat, pdu_debug_2);
%include "iustsat/tag_counter.h"
GR_SWIG_BLOCK_MAGIC2(iustsat, tag_counter);
%include "iustsat/rs_to_decrypt.h"
GR_SWIG_BLOCK_MAGIC2(iustsat, rs_to_decrypt);
%include "iustsat/frame_analysis.h"
GR_SWIG_BLOCK_MAGIC2(iustsat, frame_analysis);
%include "iustsat/pdu_to_message.h"
GR_SWIG_BLOCK_MAGIC2(iustsat, pdu_to_message);
%include "iustsat/zafar_telemetry_deinterleave.h"
GR_SWIG_BLOCK_MAGIC2(iustsat, zafar_telemetry_deinterleave);
%include "iustsat/pack_rsblock.h"
GR_SWIG_BLOCK_MAGIC2(iustsat, pack_rsblock);

%include "iustsat/vt_to_decrypt.h"
GR_SWIG_BLOCK_MAGIC2(iustsat, vt_to_decrypt);
