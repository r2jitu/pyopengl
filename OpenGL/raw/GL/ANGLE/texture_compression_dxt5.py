'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_ANGLE_texture_compression_dxt5'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_ANGLE_texture_compression_dxt5',error_checker=_errors._error_checker)
GL_COMPRESSED_RGBA_S3TC_DXT5_ANGLE=_C('GL_COMPRESSED_RGBA_S3TC_DXT5_ANGLE',0x83F3)

