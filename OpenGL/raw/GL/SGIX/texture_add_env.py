'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_SGIX_texture_add_env'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_SGIX_texture_add_env',error_checker=_errors._error_checker)
GL_TEXTURE_ENV_BIAS_SGIX=_C('GL_TEXTURE_ENV_BIAS_SGIX',0x80BE)

