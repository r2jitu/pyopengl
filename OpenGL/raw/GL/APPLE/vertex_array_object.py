'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_APPLE_vertex_array_object'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_APPLE_vertex_array_object',error_checker=_errors._error_checker)
GL_VERTEX_ARRAY_BINDING_APPLE=_C('GL_VERTEX_ARRAY_BINDING_APPLE',0x85B5)
@_f
@_p.types(None,_cs.GLuint)
def glBindVertexArrayAPPLE(array):pass
@_f
@_p.types(None,_cs.GLsizei,arrays.GLuintArray)
def glDeleteVertexArraysAPPLE(n,arrays):pass
@_f
@_p.types(None,_cs.GLsizei,arrays.GLuintArray)
def glGenVertexArraysAPPLE(n,arrays):pass
@_f
@_p.types(_cs.GLboolean,_cs.GLuint)
def glIsVertexArrayAPPLE(array):pass
