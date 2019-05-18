INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_IUSTSAT iustsat)

FIND_PATH(
    IUSTSAT_INCLUDE_DIRS
    NAMES iustsat/api.h
    HINTS $ENV{IUSTSAT_DIR}/include
        ${PC_IUSTSAT_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    IUSTSAT_LIBRARIES
    NAMES gnuradio-iustsat
    HINTS $ENV{IUSTSAT_DIR}/lib
        ${PC_IUSTSAT_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(IUSTSAT DEFAULT_MSG IUSTSAT_LIBRARIES IUSTSAT_INCLUDE_DIRS)
MARK_AS_ADVANCED(IUSTSAT_LIBRARIES IUSTSAT_INCLUDE_DIRS)

