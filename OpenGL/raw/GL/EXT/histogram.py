'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_EXT_histogram'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_EXT_histogram',error_checker=_errors._error_checker)
GL_HISTOGRAM_ALPHA_SIZE_EXT=_C('GL_HISTOGRAM_ALPHA_SIZE_EXT',0x802B)
GL_HISTOGRAM_BLUE_SIZE_EXT=_C('GL_HISTOGRAM_BLUE_SIZE_EXT',0x802A)
GL_HISTOGRAM_EXT=_C('GL_HISTOGRAM_EXT',0x8024)
GL_HISTOGRAM_FORMAT_EXT=_C('GL_HISTOGRAM_FORMAT_EXT',0x8027)
GL_HISTOGRAM_GREEN_SIZE_EXT=_C('GL_HISTOGRAM_GREEN_SIZE_EXT',0x8029)
GL_HISTOGRAM_LUMINANCE_SIZE_EXT=_C('GL_HISTOGRAM_LUMINANCE_SIZE_EXT',0x802C)
GL_HISTOGRAM_RED_SIZE_EXT=_C('GL_HISTOGRAM_RED_SIZE_EXT',0x8028)
GL_HISTOGRAM_SINK_EXT=_C('GL_HISTOGRAM_SINK_EXT',0x802D)
GL_HISTOGRAM_WIDTH_EXT=_C('GL_HISTOGRAM_WIDTH_EXT',0x8026)
GL_MINMAX_EXT=_C('GL_MINMAX_EXT',0x802E)
GL_MINMAX_FORMAT_EXT=_C('GL_MINMAX_FORMAT_EXT',0x802F)
GL_MINMAX_SINK_EXT=_C('GL_MINMAX_SINK_EXT',0x8030)
GL_PROXY_HISTOGRAM_EXT=_C('GL_PROXY_HISTOGRAM_EXT',0x8025)
GL_TABLE_TOO_LARGE_EXT=_C('GL_TABLE_TOO_LARGE_EXT',0x8031)
@_f
@_p.types(None,_cs.GLenum,_cs.GLboolean,_cs.GLenum,_cs.GLenum,ctypes.c_void_p)
def glGetHistogramEXT(target,reset,format,type,values):pass
# Calculate length of values from target:HistogramTargetEXT, format:PixelFormat, type:PixelType
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLfloatArray)
def glGetHistogramParameterfvEXT(target,pname,params):pass
# Calculate length of params from pname:GetHistogramParameterPNameEXT
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glGetHistogramParameterivEXT(target,pname,params):pass
# Calculate length of params from pname:GetHistogramParameterPNameEXT
@_f
@_p.types(None,_cs.GLenum,_cs.GLboolean,_cs.GLenum,_cs.GLenum,ctypes.c_void_p)
def glGetMinmaxEXT(target,reset,format,type,values):pass
# Calculate length of values from target:MinmaxTargetEXT, format:PixelFormat, type:PixelType
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLfloatArray)
def glGetMinmaxParameterfvEXT(target,pname,params):pass
# Calculate length of params from pname:GetMinmaxParameterPNameEXT
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glGetMinmaxParameterivEXT(target,pname,params):pass
# Calculate length of params from pname:GetMinmaxParameterPNameEXT
@_f
@_p.types(None,_cs.GLenum,_cs.GLsizei,_cs.GLenum,_cs.GLboolean)
def glHistogramEXT(target,width,internalformat,sink):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLboolean)
def glMinmaxEXT(target,internalformat,sink):pass
@_f
@_p.types(None,_cs.GLenum)
def glResetHistogramEXT(target):pass
@_f
@_p.types(None,_cs.GLenum)
def glResetMinmaxEXT(target):pass
