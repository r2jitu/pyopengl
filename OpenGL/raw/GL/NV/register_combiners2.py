'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_NV_register_combiners2'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_NV_register_combiners2',error_checker=_errors._error_checker)
GL_PER_STAGE_CONSTANTS_NV=_C('GL_PER_STAGE_CONSTANTS_NV',0x8535)
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLfloatArray)
def glCombinerStageParameterfvNV(stage,pname,params):pass
# Calculate length of params from pname:CombinerParameterNV
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLfloatArray)
def glGetCombinerStageParameterfvNV(stage,pname,params):pass
# Calculate length of params from pname:CombinerParameterNV
