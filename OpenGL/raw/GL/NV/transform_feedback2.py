'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_NV_transform_feedback2'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_NV_transform_feedback2',error_checker=_errors._error_checker)
GL_TRANSFORM_FEEDBACK_BINDING_NV=_C('GL_TRANSFORM_FEEDBACK_BINDING_NV',0x8E25)
GL_TRANSFORM_FEEDBACK_BUFFER_ACTIVE_NV=_C('GL_TRANSFORM_FEEDBACK_BUFFER_ACTIVE_NV',0x8E24)
GL_TRANSFORM_FEEDBACK_BUFFER_PAUSED_NV=_C('GL_TRANSFORM_FEEDBACK_BUFFER_PAUSED_NV',0x8E23)
GL_TRANSFORM_FEEDBACK_NV=_C('GL_TRANSFORM_FEEDBACK_NV',0x8E22)
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint)
def glBindTransformFeedbackNV(target,id):pass
@_f
@_p.types(None,_cs.GLsizei,arrays.GLuintArray)
def glDeleteTransformFeedbacksNV(n,ids):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint)
def glDrawTransformFeedbackNV(mode,id):pass
@_f
@_p.types(None,_cs.GLsizei,arrays.GLuintArray)
def glGenTransformFeedbacksNV(n,ids):pass
@_f
@_p.types(_cs.GLboolean,_cs.GLuint)
def glIsTransformFeedbackNV(id):pass
@_f
@_p.types(None,)
def glPauseTransformFeedbackNV():pass
@_f
@_p.types(None,)
def glResumeTransformFeedbackNV():pass
