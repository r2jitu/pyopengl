'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_EXT_vertex_weighting'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_EXT_vertex_weighting',error_checker=_errors._error_checker)
GL_CURRENT_VERTEX_WEIGHT_EXT=_C('GL_CURRENT_VERTEX_WEIGHT_EXT',0x850B)
GL_MODELVIEW0_EXT=_C('GL_MODELVIEW0_EXT',0x1700)
GL_MODELVIEW0_MATRIX_EXT=_C('GL_MODELVIEW0_MATRIX_EXT',0x0BA6)
GL_MODELVIEW0_STACK_DEPTH_EXT=_C('GL_MODELVIEW0_STACK_DEPTH_EXT',0x0BA3)
GL_MODELVIEW1_EXT=_C('GL_MODELVIEW1_EXT',0x850A)
GL_MODELVIEW1_MATRIX_EXT=_C('GL_MODELVIEW1_MATRIX_EXT',0x8506)
GL_MODELVIEW1_STACK_DEPTH_EXT=_C('GL_MODELVIEW1_STACK_DEPTH_EXT',0x8502)
GL_VERTEX_WEIGHTING_EXT=_C('GL_VERTEX_WEIGHTING_EXT',0x8509)
GL_VERTEX_WEIGHT_ARRAY_EXT=_C('GL_VERTEX_WEIGHT_ARRAY_EXT',0x850C)
GL_VERTEX_WEIGHT_ARRAY_POINTER_EXT=_C('GL_VERTEX_WEIGHT_ARRAY_POINTER_EXT',0x8510)
GL_VERTEX_WEIGHT_ARRAY_SIZE_EXT=_C('GL_VERTEX_WEIGHT_ARRAY_SIZE_EXT',0x850D)
GL_VERTEX_WEIGHT_ARRAY_STRIDE_EXT=_C('GL_VERTEX_WEIGHT_ARRAY_STRIDE_EXT',0x850F)
GL_VERTEX_WEIGHT_ARRAY_TYPE_EXT=_C('GL_VERTEX_WEIGHT_ARRAY_TYPE_EXT',0x850E)
@_f
@_p.types(None,_cs.GLint,_cs.GLenum,_cs.GLsizei,ctypes.c_void_p)
def glVertexWeightPointerEXT(size,type,stride,pointer):pass
# Calculate length of pointer from type:VertexWeightPointerTypeEXT
@_f
@_p.types(None,_cs.GLfloat)
def glVertexWeightfEXT(weight):pass
@_f
@_p.types(None,arrays.GLfloatArray)
def glVertexWeightfvEXT(weight):pass
