'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_EXT_index_material'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_EXT_index_material',error_checker=_errors._error_checker)
GL_INDEX_MATERIAL_EXT=_C('GL_INDEX_MATERIAL_EXT',0x81B8)
GL_INDEX_MATERIAL_FACE_EXT=_C('GL_INDEX_MATERIAL_FACE_EXT',0x81BA)
GL_INDEX_MATERIAL_PARAMETER_EXT=_C('GL_INDEX_MATERIAL_PARAMETER_EXT',0x81B9)
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum)
def glIndexMaterialEXT(face,mode):pass
