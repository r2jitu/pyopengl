'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_EXT_texture_rg'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_EXT_texture_rg',error_checker=_errors._error_checker)
GL_R8_EXT=_C('GL_R8_EXT',0x8229)
GL_RED_EXT=_C('GL_RED_EXT',0x1903)
GL_RG8_EXT=_C('GL_RG8_EXT',0x822B)
GL_RG_EXT=_C('GL_RG_EXT',0x8227)

