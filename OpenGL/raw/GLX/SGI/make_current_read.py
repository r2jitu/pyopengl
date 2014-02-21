'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GLX import _types as _cs
# End users want this...
from OpenGL.raw.GLX._types import *
from OpenGL.raw.GLX import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GLX_SGI_make_current_read'
def _f( function ):
    return _p.createFunction( function,_p.GLX,'GLX_SGI_make_current_read',error_checker=_errors._error_checker)

@_f
@_p.types(_cs.GLXDrawable,)
def glXGetCurrentReadDrawableSGI():pass
@_f
@_p.types(_cs.Bool,ctypes.POINTER(_cs.Display),_cs.GLXDrawable,_cs.GLXDrawable,_cs.GLXContext)
def glXMakeCurrentReadSGI(dpy,draw,read,ctx):pass
