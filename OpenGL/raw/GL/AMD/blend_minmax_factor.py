'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_AMD_blend_minmax_factor'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_AMD_blend_minmax_factor',error_checker=_errors._error_checker)
GL_FACTOR_MAX_AMD=_C('GL_FACTOR_MAX_AMD',0x901D)
GL_FACTOR_MIN_AMD=_C('GL_FACTOR_MIN_AMD',0x901C)

