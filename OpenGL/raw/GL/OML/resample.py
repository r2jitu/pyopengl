'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_OML_resample'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_OML_resample',error_checker=_errors._error_checker)
GL_PACK_RESAMPLE_OML=_C('GL_PACK_RESAMPLE_OML',0x8984)
GL_RESAMPLE_AVERAGE_OML=_C('GL_RESAMPLE_AVERAGE_OML',0x8988)
GL_RESAMPLE_DECIMATE_OML=_C('GL_RESAMPLE_DECIMATE_OML',0x8989)
GL_RESAMPLE_REPLICATE_OML=_C('GL_RESAMPLE_REPLICATE_OML',0x8986)
GL_RESAMPLE_ZERO_FILL_OML=_C('GL_RESAMPLE_ZERO_FILL_OML',0x8987)
GL_UNPACK_RESAMPLE_OML=_C('GL_UNPACK_RESAMPLE_OML',0x8985)

