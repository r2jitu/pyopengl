'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GLX import _types as _cs
# End users want this...
from OpenGL.raw.GLX._types import *
from OpenGL.raw.GLX import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GLX_ARB_get_proc_address'
def _f( function ):
    return _p.createFunction( function,_p.GLX,'GLX_ARB_get_proc_address',error_checker=_errors._error_checker)

@_f
@_p.types(_cs.__GLXextFuncPtr,arrays.GLubyteArray)
def glXGetProcAddressARB(procName):pass
