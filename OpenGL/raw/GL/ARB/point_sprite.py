'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_ARB_point_sprite'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_ARB_point_sprite',error_checker=_errors._error_checker)
GL_COORD_REPLACE_ARB=_C('GL_COORD_REPLACE_ARB',0x8862)
GL_POINT_SPRITE_ARB=_C('GL_POINT_SPRITE_ARB',0x8861)

