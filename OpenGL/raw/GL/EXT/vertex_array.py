'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_EXT_vertex_array'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_EXT_vertex_array',error_checker=_errors._error_checker)
GL_COLOR_ARRAY_COUNT_EXT=_C('GL_COLOR_ARRAY_COUNT_EXT',0x8084)
GL_COLOR_ARRAY_EXT=_C('GL_COLOR_ARRAY_EXT',0x8076)
GL_COLOR_ARRAY_POINTER_EXT=_C('GL_COLOR_ARRAY_POINTER_EXT',0x8090)
GL_COLOR_ARRAY_SIZE_EXT=_C('GL_COLOR_ARRAY_SIZE_EXT',0x8081)
GL_COLOR_ARRAY_STRIDE_EXT=_C('GL_COLOR_ARRAY_STRIDE_EXT',0x8083)
GL_COLOR_ARRAY_TYPE_EXT=_C('GL_COLOR_ARRAY_TYPE_EXT',0x8082)
GL_EDGE_FLAG_ARRAY_COUNT_EXT=_C('GL_EDGE_FLAG_ARRAY_COUNT_EXT',0x808D)
GL_EDGE_FLAG_ARRAY_EXT=_C('GL_EDGE_FLAG_ARRAY_EXT',0x8079)
GL_EDGE_FLAG_ARRAY_POINTER_EXT=_C('GL_EDGE_FLAG_ARRAY_POINTER_EXT',0x8093)
GL_EDGE_FLAG_ARRAY_STRIDE_EXT=_C('GL_EDGE_FLAG_ARRAY_STRIDE_EXT',0x808C)
GL_INDEX_ARRAY_COUNT_EXT=_C('GL_INDEX_ARRAY_COUNT_EXT',0x8087)
GL_INDEX_ARRAY_EXT=_C('GL_INDEX_ARRAY_EXT',0x8077)
GL_INDEX_ARRAY_POINTER_EXT=_C('GL_INDEX_ARRAY_POINTER_EXT',0x8091)
GL_INDEX_ARRAY_STRIDE_EXT=_C('GL_INDEX_ARRAY_STRIDE_EXT',0x8086)
GL_INDEX_ARRAY_TYPE_EXT=_C('GL_INDEX_ARRAY_TYPE_EXT',0x8085)
GL_NORMAL_ARRAY_COUNT_EXT=_C('GL_NORMAL_ARRAY_COUNT_EXT',0x8080)
GL_NORMAL_ARRAY_EXT=_C('GL_NORMAL_ARRAY_EXT',0x8075)
GL_NORMAL_ARRAY_POINTER_EXT=_C('GL_NORMAL_ARRAY_POINTER_EXT',0x808F)
GL_NORMAL_ARRAY_STRIDE_EXT=_C('GL_NORMAL_ARRAY_STRIDE_EXT',0x807F)
GL_NORMAL_ARRAY_TYPE_EXT=_C('GL_NORMAL_ARRAY_TYPE_EXT',0x807E)
GL_TEXTURE_COORD_ARRAY_COUNT_EXT=_C('GL_TEXTURE_COORD_ARRAY_COUNT_EXT',0x808B)
GL_TEXTURE_COORD_ARRAY_EXT=_C('GL_TEXTURE_COORD_ARRAY_EXT',0x8078)
GL_TEXTURE_COORD_ARRAY_POINTER_EXT=_C('GL_TEXTURE_COORD_ARRAY_POINTER_EXT',0x8092)
GL_TEXTURE_COORD_ARRAY_SIZE_EXT=_C('GL_TEXTURE_COORD_ARRAY_SIZE_EXT',0x8088)
GL_TEXTURE_COORD_ARRAY_STRIDE_EXT=_C('GL_TEXTURE_COORD_ARRAY_STRIDE_EXT',0x808A)
GL_TEXTURE_COORD_ARRAY_TYPE_EXT=_C('GL_TEXTURE_COORD_ARRAY_TYPE_EXT',0x8089)
GL_VERTEX_ARRAY_COUNT_EXT=_C('GL_VERTEX_ARRAY_COUNT_EXT',0x807D)
GL_VERTEX_ARRAY_EXT=_C('GL_VERTEX_ARRAY_EXT',0x8074)
GL_VERTEX_ARRAY_POINTER_EXT=_C('GL_VERTEX_ARRAY_POINTER_EXT',0x808E)
GL_VERTEX_ARRAY_SIZE_EXT=_C('GL_VERTEX_ARRAY_SIZE_EXT',0x807A)
GL_VERTEX_ARRAY_STRIDE_EXT=_C('GL_VERTEX_ARRAY_STRIDE_EXT',0x807C)
GL_VERTEX_ARRAY_TYPE_EXT=_C('GL_VERTEX_ARRAY_TYPE_EXT',0x807B)
@_f
@_p.types(None,_cs.GLint)
def glArrayElementEXT(i):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLenum,_cs.GLsizei,_cs.GLsizei,ctypes.c_void_p)
def glColorPointerEXT(size,type,stride,count,pointer):pass
# Calculate length of pointer from type:ColorPointerType
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,_cs.GLsizei)
def glDrawArraysEXT(mode,first,count):pass
@_f
@_p.types(None,_cs.GLsizei,_cs.GLsizei,arrays.GLbooleanArray)
def glEdgeFlagPointerEXT(stride,count,pointer):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLvoidpArray)
def glGetPointervEXT(pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLsizei,_cs.GLsizei,ctypes.c_void_p)
def glIndexPointerEXT(type,stride,count,pointer):pass
# Calculate length of pointer from type:IndexPointerType
@_f
@_p.types(None,_cs.GLenum,_cs.GLsizei,_cs.GLsizei,ctypes.c_void_p)
def glNormalPointerEXT(type,stride,count,pointer):pass
# Calculate length of pointer from type:NormalPointerType
@_f
@_p.types(None,_cs.GLint,_cs.GLenum,_cs.GLsizei,_cs.GLsizei,ctypes.c_void_p)
def glTexCoordPointerEXT(size,type,stride,count,pointer):pass
# Calculate length of pointer from type:TexCoordPointerType
@_f
@_p.types(None,_cs.GLint,_cs.GLenum,_cs.GLsizei,_cs.GLsizei,ctypes.c_void_p)
def glVertexPointerEXT(size,type,stride,count,pointer):pass
# Calculate length of pointer from type:VertexPointerType
