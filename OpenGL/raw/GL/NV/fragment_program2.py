'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_NV_fragment_program2'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_NV_fragment_program2',error_checker=_errors._error_checker)
GL_MAX_PROGRAM_CALL_DEPTH_NV=_C('GL_MAX_PROGRAM_CALL_DEPTH_NV',0x88F5)
GL_MAX_PROGRAM_EXEC_INSTRUCTIONS_NV=_C('GL_MAX_PROGRAM_EXEC_INSTRUCTIONS_NV',0x88F4)
GL_MAX_PROGRAM_IF_DEPTH_NV=_C('GL_MAX_PROGRAM_IF_DEPTH_NV',0x88F6)
GL_MAX_PROGRAM_LOOP_COUNT_NV=_C('GL_MAX_PROGRAM_LOOP_COUNT_NV',0x88F8)
GL_MAX_PROGRAM_LOOP_DEPTH_NV=_C('GL_MAX_PROGRAM_LOOP_DEPTH_NV',0x88F7)

