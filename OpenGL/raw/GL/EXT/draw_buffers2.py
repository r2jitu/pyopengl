'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_EXT_draw_buffers2'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_EXT_draw_buffers2',error_checker=_errors._error_checker)

@_f
@_p.types(None,_cs.GLuint,_cs.GLboolean,_cs.GLboolean,_cs.GLboolean,_cs.GLboolean)
def glColorMaskIndexedEXT(index,r,g,b,a):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint)
def glDisableIndexedEXT(target,index):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint)
def glEnableIndexedEXT(target,index):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,arrays.GLbooleanArray)
def glGetBooleanIndexedvEXT(target,index,data):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,arrays.GLintArray)
def glGetIntegerIndexedvEXT(target,index,data):pass
@_f
@_p.types(_cs.GLboolean,_cs.GLenum,_cs.GLuint)
def glIsEnabledIndexedEXT(target,index):pass
