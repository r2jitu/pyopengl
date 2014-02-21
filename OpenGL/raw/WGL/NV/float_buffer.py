'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.WGL import _types as _cs
# End users want this...
from OpenGL.raw.WGL._types import *
from OpenGL.raw.WGL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'WGL_NV_float_buffer'
def _f( function ):
    return _p.createFunction( function,_p.WGL,'WGL_NV_float_buffer',error_checker=_errors._error_checker)
WGL_BIND_TO_TEXTURE_RECTANGLE_FLOAT_RGBA_NV=_C('WGL_BIND_TO_TEXTURE_RECTANGLE_FLOAT_RGBA_NV',0x20B4)
WGL_BIND_TO_TEXTURE_RECTANGLE_FLOAT_RGB_NV=_C('WGL_BIND_TO_TEXTURE_RECTANGLE_FLOAT_RGB_NV',0x20B3)
WGL_BIND_TO_TEXTURE_RECTANGLE_FLOAT_RG_NV=_C('WGL_BIND_TO_TEXTURE_RECTANGLE_FLOAT_RG_NV',0x20B2)
WGL_BIND_TO_TEXTURE_RECTANGLE_FLOAT_R_NV=_C('WGL_BIND_TO_TEXTURE_RECTANGLE_FLOAT_R_NV',0x20B1)
WGL_FLOAT_COMPONENTS_NV=_C('WGL_FLOAT_COMPONENTS_NV',0x20B0)
WGL_TEXTURE_FLOAT_RGBA_NV=_C('WGL_TEXTURE_FLOAT_RGBA_NV',0x20B8)
WGL_TEXTURE_FLOAT_RGB_NV=_C('WGL_TEXTURE_FLOAT_RGB_NV',0x20B7)
WGL_TEXTURE_FLOAT_RG_NV=_C('WGL_TEXTURE_FLOAT_RG_NV',0x20B6)
WGL_TEXTURE_FLOAT_R_NV=_C('WGL_TEXTURE_FLOAT_R_NV',0x20B5)

