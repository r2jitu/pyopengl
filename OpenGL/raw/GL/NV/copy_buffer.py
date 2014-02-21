'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_NV_copy_buffer'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_NV_copy_buffer',error_checker=_errors._error_checker)
GL_COPY_READ_BUFFER_NV=_C('GL_COPY_READ_BUFFER_NV',0x8F36)
GL_COPY_WRITE_BUFFER_NV=_C('GL_COPY_WRITE_BUFFER_NV',0x8F37)
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLintptr,_cs.GLintptr,_cs.GLsizeiptr)
def glCopyBufferSubDataNV(readTarget,writeTarget,readOffset,writeOffset,size):pass
