'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_ARB_pixel_buffer_object'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_ARB_pixel_buffer_object',error_checker=_errors._error_checker)
GL_PIXEL_PACK_BUFFER_ARB=_C('GL_PIXEL_PACK_BUFFER_ARB',0x88EB)
GL_PIXEL_PACK_BUFFER_BINDING_ARB=_C('GL_PIXEL_PACK_BUFFER_BINDING_ARB',0x88ED)
GL_PIXEL_UNPACK_BUFFER_ARB=_C('GL_PIXEL_UNPACK_BUFFER_ARB',0x88EC)
GL_PIXEL_UNPACK_BUFFER_BINDING_ARB=_C('GL_PIXEL_UNPACK_BUFFER_BINDING_ARB',0x88EF)

