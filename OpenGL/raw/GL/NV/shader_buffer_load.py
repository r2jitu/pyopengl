'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_NV_shader_buffer_load'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_NV_shader_buffer_load',error_checker=_errors._error_checker)
GL_BUFFER_GPU_ADDRESS_NV=_C('GL_BUFFER_GPU_ADDRESS_NV',0x8F1D)
GL_GPU_ADDRESS_NV=_C('GL_GPU_ADDRESS_NV',0x8F34)
GL_MAX_SHADER_BUFFER_ADDRESS_NV=_C('GL_MAX_SHADER_BUFFER_ADDRESS_NV',0x8F35)
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLuint64Array)
def glGetBufferParameterui64vNV(target,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLuint64Array)
def glGetIntegerui64vNV(value,result):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLuint64Array)
def glGetNamedBufferParameterui64vNV(buffer,pname,params):pass
# Calculate length of params from pname:VertexBufferObjectParameter
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,arrays.GLuint64Array)
def glGetUniformui64vNV(program,location,params):pass
@_f
@_p.types(_cs.GLboolean,_cs.GLenum)
def glIsBufferResidentNV(target):pass
@_f
@_p.types(_cs.GLboolean,_cs.GLuint)
def glIsNamedBufferResidentNV(buffer):pass
@_f
@_p.types(None,_cs.GLenum)
def glMakeBufferNonResidentNV(target):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum)
def glMakeBufferResidentNV(target,access):pass
@_f
@_p.types(None,_cs.GLuint)
def glMakeNamedBufferNonResidentNV(buffer):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum)
def glMakeNamedBufferResidentNV(buffer,access):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLuint64EXT)
def glProgramUniformui64NV(program,location,value):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLsizei,arrays.GLuint64Array)
def glProgramUniformui64vNV(program,location,count,value):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLuint64EXT)
def glUniformui64NV(location,value):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLsizei,arrays.GLuint64Array)
def glUniformui64vNV(location,count,value):pass
