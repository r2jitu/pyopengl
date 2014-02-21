'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.WGL import _types as _cs
# End users want this...
from OpenGL.raw.WGL._types import *
from OpenGL.raw.WGL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'WGL_EXT_pbuffer'
def _f( function ):
    return _p.createFunction( function,_p.WGL,'WGL_EXT_pbuffer',error_checker=_errors._error_checker)
WGL_DRAW_TO_PBUFFER_EXT=_C('WGL_DRAW_TO_PBUFFER_EXT',0x202D)
WGL_MAX_PBUFFER_HEIGHT_EXT=_C('WGL_MAX_PBUFFER_HEIGHT_EXT',0x2030)
WGL_MAX_PBUFFER_PIXELS_EXT=_C('WGL_MAX_PBUFFER_PIXELS_EXT',0x202E)
WGL_MAX_PBUFFER_WIDTH_EXT=_C('WGL_MAX_PBUFFER_WIDTH_EXT',0x202F)
WGL_OPTIMAL_PBUFFER_HEIGHT_EXT=_C('WGL_OPTIMAL_PBUFFER_HEIGHT_EXT',0x2032)
WGL_OPTIMAL_PBUFFER_WIDTH_EXT=_C('WGL_OPTIMAL_PBUFFER_WIDTH_EXT',0x2031)
WGL_PBUFFER_HEIGHT_EXT=_C('WGL_PBUFFER_HEIGHT_EXT',0x2035)
WGL_PBUFFER_LARGEST_EXT=_C('WGL_PBUFFER_LARGEST_EXT',0x2033)
WGL_PBUFFER_WIDTH_EXT=_C('WGL_PBUFFER_WIDTH_EXT',0x2034)
@_f
@_p.types(_cs.HPBUFFEREXT,_cs.HDC,_cs.c_int,_cs.c_int,_cs.c_int,ctypes.POINTER(_cs.c_int))
def wglCreatePbufferEXT(hDC,iPixelFormat,iWidth,iHeight,piAttribList):pass
@_f
@_p.types(_cs.BOOL,_cs.HPBUFFEREXT)
def wglDestroyPbufferEXT(hPbuffer):pass
@_f
@_p.types(_cs.HDC,_cs.HPBUFFEREXT)
def wglGetPbufferDCEXT(hPbuffer):pass
@_f
@_p.types(_cs.BOOL,_cs.HPBUFFEREXT,_cs.c_int,ctypes.POINTER(_cs.c_int))
def wglQueryPbufferEXT(hPbuffer,iAttribute,piValue):pass
@_f
@_p.types(_cs.c_int,_cs.HPBUFFEREXT,_cs.HDC)
def wglReleasePbufferDCEXT(hPbuffer,hDC):pass
