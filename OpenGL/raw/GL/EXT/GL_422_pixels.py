'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_EXT_GL_422_pixels'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_EXT_GL_422_pixels',error_checker=_errors._error_checker)
GL_422_AVERAGE_EXT=_C('GL_422_AVERAGE_EXT',0x80CE)
GL_422_EXT=_C('GL_422_EXT',0x80CC)
GL_422_REV_AVERAGE_EXT=_C('GL_422_REV_AVERAGE_EXT',0x80CF)
GL_422_REV_EXT=_C('GL_422_REV_EXT',0x80CD)

