'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.WGL import _types as _cs
# End users want this...
from OpenGL.raw.WGL._types import *
from OpenGL.raw.WGL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'WGL_NV_multisample_coverage'
def _f( function ):
    return _p.createFunction( function,_p.WGL,'WGL_NV_multisample_coverage',error_checker=_errors._error_checker)
WGL_COLOR_SAMPLES_NV=_C('WGL_COLOR_SAMPLES_NV',0x20B9)
WGL_COVERAGE_SAMPLES_NV=_C('WGL_COVERAGE_SAMPLES_NV',0x2042)

