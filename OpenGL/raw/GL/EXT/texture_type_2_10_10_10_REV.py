'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_EXT_texture_type_2_10_10_10_REV'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_EXT_texture_type_2_10_10_10_REV',error_checker=_errors._error_checker)
GL_UNSIGNED_INT_2_10_10_10_REV_EXT=_C('GL_UNSIGNED_INT_2_10_10_10_REV_EXT',0x8368)

