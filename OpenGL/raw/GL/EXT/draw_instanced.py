'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_EXT_draw_instanced'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_EXT_draw_instanced',error_checker=_errors._error_checker)

@_f
@_p.types(None,_cs.GLenum,_cs.GLint,_cs.GLsizei,_cs.GLsizei)
def glDrawArraysInstancedEXT(mode,start,count,primcount):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLsizei,_cs.GLenum,ctypes.c_void_p,_cs.GLsizei)
def glDrawElementsInstancedEXT(mode,count,type,indices,primcount):pass
# Calculate length of indices from type:DrawElementsType
