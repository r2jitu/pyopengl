'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_EXT_separate_specular_color'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_EXT_separate_specular_color',error_checker=_errors._error_checker)
GL_LIGHT_MODEL_COLOR_CONTROL_EXT=_C('GL_LIGHT_MODEL_COLOR_CONTROL_EXT',0x81F8)
GL_SEPARATE_SPECULAR_COLOR_EXT=_C('GL_SEPARATE_SPECULAR_COLOR_EXT',0x81FA)
GL_SINGLE_COLOR_EXT=_C('GL_SINGLE_COLOR_EXT',0x81F9)

