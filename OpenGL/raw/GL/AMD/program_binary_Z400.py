'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_AMD_program_binary_Z400'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_AMD_program_binary_Z400',error_checker=_errors._error_checker)
GL_Z400_BINARY_AMD=_C('GL_Z400_BINARY_AMD',0x8740)

