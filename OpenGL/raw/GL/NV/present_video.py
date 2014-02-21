'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_NV_present_video'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_NV_present_video',error_checker=_errors._error_checker)
GL_CURRENT_TIME_NV=_C('GL_CURRENT_TIME_NV',0x8E28)
GL_FIELDS_NV=_C('GL_FIELDS_NV',0x8E27)
GL_FRAME_NV=_C('GL_FRAME_NV',0x8E26)
GL_NUM_FILL_STREAMS_NV=_C('GL_NUM_FILL_STREAMS_NV',0x8E29)
GL_PRESENT_DURATION_NV=_C('GL_PRESENT_DURATION_NV',0x8E2B)
GL_PRESENT_TIME_NV=_C('GL_PRESENT_TIME_NV',0x8E2A)
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLint64Array)
def glGetVideoi64vNV(video_slot,pname,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLintArray)
def glGetVideoivNV(video_slot,pname,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLuint64Array)
def glGetVideoui64vNV(video_slot,pname,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLuintArray)
def glGetVideouivNV(video_slot,pname,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint64EXT,_cs.GLuint,_cs.GLuint,_cs.GLenum,_cs.GLenum,_cs.GLuint,_cs.GLenum,_cs.GLuint,_cs.GLenum,_cs.GLuint,_cs.GLenum,_cs.GLuint)
def glPresentFrameDualFillNV(video_slot,minPresentTime,beginPresentTimeId,presentDurationId,type,target0,fill0,target1,fill1,target2,fill2,target3,fill3):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint64EXT,_cs.GLuint,_cs.GLuint,_cs.GLenum,_cs.GLenum,_cs.GLuint,_cs.GLuint,_cs.GLenum,_cs.GLuint,_cs.GLuint)
def glPresentFrameKeyedNV(video_slot,minPresentTime,beginPresentTimeId,presentDurationId,type,target0,fill0,key0,target1,fill1,key1):pass
