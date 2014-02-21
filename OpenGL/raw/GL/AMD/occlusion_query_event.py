'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_AMD_occlusion_query_event'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_AMD_occlusion_query_event',error_checker=_errors._error_checker)
GL_OCCLUSION_QUERY_EVENT_MASK_AMD=_C('GL_OCCLUSION_QUERY_EVENT_MASK_AMD',0x874F)
GL_QUERY_ALL_EVENT_BITS_AMD=_C('GL_QUERY_ALL_EVENT_BITS_AMD',0xFFFFFFFF)
GL_QUERY_DEPTH_BOUNDS_FAIL_EVENT_BIT_AMD=_C('GL_QUERY_DEPTH_BOUNDS_FAIL_EVENT_BIT_AMD',0x00000008)
GL_QUERY_DEPTH_FAIL_EVENT_BIT_AMD=_C('GL_QUERY_DEPTH_FAIL_EVENT_BIT_AMD',0x00000002)
GL_QUERY_DEPTH_PASS_EVENT_BIT_AMD=_C('GL_QUERY_DEPTH_PASS_EVENT_BIT_AMD',0x00000001)
GL_QUERY_STENCIL_FAIL_EVENT_BIT_AMD=_C('GL_QUERY_STENCIL_FAIL_EVENT_BIT_AMD',0x00000004)
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,_cs.GLenum,_cs.GLuint)
def glQueryObjectParameteruiAMD(target,id,pname,param):pass
