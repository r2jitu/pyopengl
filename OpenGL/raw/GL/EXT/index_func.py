'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_EXT_index_func'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_EXT_index_func',error_checker=_errors._error_checker)
GL_INDEX_TEST_EXT=_C('GL_INDEX_TEST_EXT',0x81B5)
GL_INDEX_TEST_FUNC_EXT=_C('GL_INDEX_TEST_FUNC_EXT',0x81B6)
GL_INDEX_TEST_REF_EXT=_C('GL_INDEX_TEST_REF_EXT',0x81B7)
@_f
@_p.types(None,_cs.GLenum,_cs.GLclampf)
def glIndexFuncEXT(func,ref):pass
