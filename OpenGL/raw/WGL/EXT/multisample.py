'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.WGL import _types as _cs
# End users want this...
from OpenGL.raw.WGL._types import *
from OpenGL.raw.WGL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'WGL_EXT_multisample'
def _f( function ):
    return _p.createFunction( function,_p.WGL,'WGL_EXT_multisample',error_checker=_errors._error_checker)
WGL_SAMPLES_EXT=_C('WGL_SAMPLES_EXT',0x2042)
WGL_SAMPLE_BUFFERS_EXT=_C('WGL_SAMPLE_BUFFERS_EXT',0x2041)

