'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_OES_matrix_get'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_OES_matrix_get',error_checker=_errors._error_checker)
GL_MODELVIEW_MATRIX_FLOAT_AS_INT_BITS_OES=_C('GL_MODELVIEW_MATRIX_FLOAT_AS_INT_BITS_OES',0x898D)
GL_PROJECTION_MATRIX_FLOAT_AS_INT_BITS_OES=_C('GL_PROJECTION_MATRIX_FLOAT_AS_INT_BITS_OES',0x898E)
GL_TEXTURE_MATRIX_FLOAT_AS_INT_BITS_OES=_C('GL_TEXTURE_MATRIX_FLOAT_AS_INT_BITS_OES',0x898F)

