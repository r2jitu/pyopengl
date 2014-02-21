'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_ARB_draw_indirect'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_ARB_draw_indirect',error_checker=_errors._error_checker)
GL_DRAW_INDIRECT_BUFFER=_C('GL_DRAW_INDIRECT_BUFFER',0x8F3F)
GL_DRAW_INDIRECT_BUFFER_BINDING=_C('GL_DRAW_INDIRECT_BUFFER_BINDING',0x8F43)
@_f
@_p.types(None,_cs.GLenum,ctypes.c_void_p)
def glDrawArraysIndirect(mode,indirect):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,ctypes.c_void_p)
def glDrawElementsIndirect(mode,type,indirect):pass
