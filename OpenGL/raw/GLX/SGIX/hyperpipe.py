'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GLX import _types as _cs
# End users want this...
from OpenGL.raw.GLX._types import *
from OpenGL.raw.GLX import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GLX_SGIX_hyperpipe'
def _f( function ):
    return _p.createFunction( function,_p.GLX,'GLX_SGIX_hyperpipe',error_checker=_errors._error_checker)
GLX_BAD_HYPERPIPE_CONFIG_SGIX=_C('GLX_BAD_HYPERPIPE_CONFIG_SGIX',91)
GLX_BAD_HYPERPIPE_SGIX=_C('GLX_BAD_HYPERPIPE_SGIX',92)
GLX_HYPERPIPE_DISPLAY_PIPE_SGIX=_C('GLX_HYPERPIPE_DISPLAY_PIPE_SGIX',0x00000001)
GLX_HYPERPIPE_ID_SGIX=_C('GLX_HYPERPIPE_ID_SGIX',0x8030)
GLX_HYPERPIPE_PIPE_NAME_LENGTH_SGIX=_C('GLX_HYPERPIPE_PIPE_NAME_LENGTH_SGIX',80)
GLX_HYPERPIPE_PIXEL_AVERAGE_SGIX=_C('GLX_HYPERPIPE_PIXEL_AVERAGE_SGIX',0x00000004)
GLX_HYPERPIPE_RENDER_PIPE_SGIX=_C('GLX_HYPERPIPE_RENDER_PIPE_SGIX',0x00000002)
GLX_HYPERPIPE_STEREO_SGIX=_C('GLX_HYPERPIPE_STEREO_SGIX',0x00000003)
GLX_PIPE_RECT_LIMITS_SGIX=_C('GLX_PIPE_RECT_LIMITS_SGIX',0x00000002)
GLX_PIPE_RECT_SGIX=_C('GLX_PIPE_RECT_SGIX',0x00000001)
@_f
@_p.types(_cs.c_int,ctypes.POINTER(_cs.Display),_cs.c_int)
def glXBindHyperpipeSGIX(dpy,hpId):pass
@_f
@_p.types(_cs.c_int,ctypes.POINTER(_cs.Display),_cs.c_int)
def glXDestroyHyperpipeConfigSGIX(dpy,hpId):pass
@_f
@_p.types(_cs.c_int,ctypes.POINTER(_cs.Display),_cs.c_int,_cs.c_int,_cs.c_int,ctypes.c_void_p)
def glXHyperpipeAttribSGIX(dpy,timeSlice,attrib,size,attribList):pass
@_f
@_p.types(_cs.c_int,ctypes.POINTER(_cs.Display),_cs.c_int,_cs.c_int,ctypes.POINTER(_cs.GLXHyperpipeConfigSGIX),ctypes.POINTER(_cs.c_int))
def glXHyperpipeConfigSGIX(dpy,networkId,npipes,cfg,hpId):pass
@_f
@_p.types(_cs.c_int,ctypes.POINTER(_cs.Display),_cs.c_int,_cs.c_int,_cs.c_int,ctypes.c_void_p)
def glXQueryHyperpipeAttribSGIX(dpy,timeSlice,attrib,size,returnAttribList):pass
@_f
@_p.types(_cs.c_int,ctypes.POINTER(_cs.Display),_cs.c_int,_cs.c_int,_cs.c_int,ctypes.c_void_p,ctypes.c_void_p)
def glXQueryHyperpipeBestAttribSGIX(dpy,timeSlice,attrib,size,attribList,returnAttribList):pass
@_f
@_p.types(ctypes.POINTER(_cs.GLXHyperpipeConfigSGIX),ctypes.POINTER(_cs.Display),_cs.c_int,ctypes.POINTER(_cs.c_int))
def glXQueryHyperpipeConfigSGIX(dpy,hpId,npipes):pass
@_f
@_p.types(ctypes.POINTER(_cs.GLXHyperpipeNetworkSGIX),ctypes.POINTER(_cs.Display),ctypes.POINTER(_cs.c_int))
def glXQueryHyperpipeNetworkSGIX(dpy,npipes):pass
