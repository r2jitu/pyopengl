'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_SGIX_fog_offset'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_SGIX_fog_offset',error_checker=_errors._error_checker)
GL_FOG_OFFSET_SGIX=_C('GL_FOG_OFFSET_SGIX',0x8198)
GL_FOG_OFFSET_VALUE_SGIX=_C('GL_FOG_OFFSET_VALUE_SGIX',0x8199)

