'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GLX import _types as _cs
# End users want this...
from OpenGL.raw.GLX._types import *
from OpenGL.raw.GLX import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GLX_EXT_swap_control'
def _f( function ):
    return _p.createFunction( function,_p.GLX,'GLX_EXT_swap_control',error_checker=_errors._error_checker)
GLX_MAX_SWAP_INTERVAL_EXT=_C('GLX_MAX_SWAP_INTERVAL_EXT',0x20F2)
GLX_SWAP_INTERVAL_EXT=_C('GLX_SWAP_INTERVAL_EXT',0x20F1)
@_f
@_p.types(None,ctypes.POINTER(_cs.Display),_cs.GLXDrawable,_cs.c_int)
def glXSwapIntervalEXT(dpy,drawable,interval):pass
