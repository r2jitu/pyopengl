'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.EGL import _types as _cs
# End users want this...
from OpenGL.raw.EGL._types import *
from OpenGL.raw.EGL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'EGL_EXT_swap_buffers_with_damage'
def _f( function ):
    return _p.createFunction( function,_p.EGL,'EGL_EXT_swap_buffers_with_damage',error_checker=_errors._error_checker)

@_f
@_p.types(_cs.EGLBoolean,_cs.EGLDisplay,_cs.EGLSurface,arrays.GLintArray,_cs.EGLint)
def eglSwapBuffersWithDamageEXT(dpy,surface,rects,n_rects):pass
