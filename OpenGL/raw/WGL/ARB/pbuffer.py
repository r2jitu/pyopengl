'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.WGL import _types as _cs
# End users want this...
from OpenGL.raw.WGL._types import *
from OpenGL.raw.WGL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'WGL_ARB_pbuffer'
def _f( function ):
    return _p.createFunction( function,_p.WGL,'WGL_ARB_pbuffer',error_checker=_errors._error_checker)
WGL_DRAW_TO_PBUFFER_ARB=_C('WGL_DRAW_TO_PBUFFER_ARB',0x202D)
WGL_MAX_PBUFFER_HEIGHT_ARB=_C('WGL_MAX_PBUFFER_HEIGHT_ARB',0x2030)
WGL_MAX_PBUFFER_PIXELS_ARB=_C('WGL_MAX_PBUFFER_PIXELS_ARB',0x202E)
WGL_MAX_PBUFFER_WIDTH_ARB=_C('WGL_MAX_PBUFFER_WIDTH_ARB',0x202F)
WGL_PBUFFER_HEIGHT_ARB=_C('WGL_PBUFFER_HEIGHT_ARB',0x2035)
WGL_PBUFFER_LARGEST_ARB=_C('WGL_PBUFFER_LARGEST_ARB',0x2033)
WGL_PBUFFER_LOST_ARB=_C('WGL_PBUFFER_LOST_ARB',0x2036)
WGL_PBUFFER_WIDTH_ARB=_C('WGL_PBUFFER_WIDTH_ARB',0x2034)
@_f
@_p.types(_cs.HPBUFFERARB,_cs.HDC,_cs.c_int,_cs.c_int,_cs.c_int,ctypes.POINTER(_cs.c_int))
def wglCreatePbufferARB(hDC,iPixelFormat,iWidth,iHeight,piAttribList):pass
@_f
@_p.types(_cs.BOOL,_cs.HPBUFFERARB)
def wglDestroyPbufferARB(hPbuffer):pass
@_f
@_p.types(_cs.HDC,_cs.HPBUFFERARB)
def wglGetPbufferDCARB(hPbuffer):pass
@_f
@_p.types(_cs.BOOL,_cs.HPBUFFERARB,_cs.c_int,ctypes.POINTER(_cs.c_int))
def wglQueryPbufferARB(hPbuffer,iAttribute,piValue):pass
@_f
@_p.types(_cs.c_int,_cs.HPBUFFERARB,_cs.HDC)
def wglReleasePbufferDCARB(hPbuffer,hDC):pass
