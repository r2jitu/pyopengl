'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_SGIX_polynomial_ffd'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_SGIX_polynomial_ffd',error_checker=_errors._error_checker)
GL_DEFORMATIONS_MASK_SGIX=_C('GL_DEFORMATIONS_MASK_SGIX',0x8196)
GL_GEOMETRY_DEFORMATION_BIT_SGIX=_C('GL_GEOMETRY_DEFORMATION_BIT_SGIX',0x00000002)
GL_GEOMETRY_DEFORMATION_SGIX=_C('GL_GEOMETRY_DEFORMATION_SGIX',0x8194)
GL_MAX_DEFORMATION_ORDER_SGIX=_C('GL_MAX_DEFORMATION_ORDER_SGIX',0x8197)
GL_TEXTURE_DEFORMATION_BIT_SGIX=_C('GL_TEXTURE_DEFORMATION_BIT_SGIX',0x00000001)
GL_TEXTURE_DEFORMATION_SGIX=_C('GL_TEXTURE_DEFORMATION_SGIX',0x8195)
@_f
@_p.types(None,_cs.GLbitfield)
def glDeformSGIX(mask):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLdouble,_cs.GLdouble,_cs.GLint,_cs.GLint,_cs.GLdouble,_cs.GLdouble,_cs.GLint,_cs.GLint,_cs.GLdouble,_cs.GLdouble,_cs.GLint,_cs.GLint,arrays.GLdoubleArray)
def glDeformationMap3dSGIX(target,u1,u2,ustride,uorder,v1,v2,vstride,vorder,w1,w2,wstride,worder,points):pass
# Calculate length of points from target:FfdTargetSGIX, uorder:CheckedInt32, vorder:CheckedInt32, worder:CheckedInt32
@_f
@_p.types(None,_cs.GLenum,_cs.GLfloat,_cs.GLfloat,_cs.GLint,_cs.GLint,_cs.GLfloat,_cs.GLfloat,_cs.GLint,_cs.GLint,_cs.GLfloat,_cs.GLfloat,_cs.GLint,_cs.GLint,arrays.GLfloatArray)
def glDeformationMap3fSGIX(target,u1,u2,ustride,uorder,v1,v2,vstride,vorder,w1,w2,wstride,worder,points):pass
# Calculate length of points from target:FfdTargetSGIX, uorder:CheckedInt32, vorder:CheckedInt32, worder:CheckedInt32
@_f
@_p.types(None,_cs.GLbitfield)
def glLoadIdentityDeformationMapSGIX(mask):pass
