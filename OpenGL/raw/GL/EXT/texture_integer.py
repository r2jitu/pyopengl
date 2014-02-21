'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_EXT_texture_integer'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_EXT_texture_integer',error_checker=_errors._error_checker)
GL_ALPHA16I_EXT=_C('GL_ALPHA16I_EXT',0x8D8A)
GL_ALPHA16UI_EXT=_C('GL_ALPHA16UI_EXT',0x8D78)
GL_ALPHA32I_EXT=_C('GL_ALPHA32I_EXT',0x8D84)
GL_ALPHA32UI_EXT=_C('GL_ALPHA32UI_EXT',0x8D72)
GL_ALPHA8I_EXT=_C('GL_ALPHA8I_EXT',0x8D90)
GL_ALPHA8UI_EXT=_C('GL_ALPHA8UI_EXT',0x8D7E)
GL_ALPHA_INTEGER_EXT=_C('GL_ALPHA_INTEGER_EXT',0x8D97)
GL_BGRA_INTEGER_EXT=_C('GL_BGRA_INTEGER_EXT',0x8D9B)
GL_BGR_INTEGER_EXT=_C('GL_BGR_INTEGER_EXT',0x8D9A)
GL_BLUE_INTEGER_EXT=_C('GL_BLUE_INTEGER_EXT',0x8D96)
GL_GREEN_INTEGER_EXT=_C('GL_GREEN_INTEGER_EXT',0x8D95)
GL_INTENSITY16I_EXT=_C('GL_INTENSITY16I_EXT',0x8D8B)
GL_INTENSITY16UI_EXT=_C('GL_INTENSITY16UI_EXT',0x8D79)
GL_INTENSITY32I_EXT=_C('GL_INTENSITY32I_EXT',0x8D85)
GL_INTENSITY32UI_EXT=_C('GL_INTENSITY32UI_EXT',0x8D73)
GL_INTENSITY8I_EXT=_C('GL_INTENSITY8I_EXT',0x8D91)
GL_INTENSITY8UI_EXT=_C('GL_INTENSITY8UI_EXT',0x8D7F)
GL_LUMINANCE16I_EXT=_C('GL_LUMINANCE16I_EXT',0x8D8C)
GL_LUMINANCE16UI_EXT=_C('GL_LUMINANCE16UI_EXT',0x8D7A)
GL_LUMINANCE32I_EXT=_C('GL_LUMINANCE32I_EXT',0x8D86)
GL_LUMINANCE32UI_EXT=_C('GL_LUMINANCE32UI_EXT',0x8D74)
GL_LUMINANCE8I_EXT=_C('GL_LUMINANCE8I_EXT',0x8D92)
GL_LUMINANCE8UI_EXT=_C('GL_LUMINANCE8UI_EXT',0x8D80)
GL_LUMINANCE_ALPHA16I_EXT=_C('GL_LUMINANCE_ALPHA16I_EXT',0x8D8D)
GL_LUMINANCE_ALPHA16UI_EXT=_C('GL_LUMINANCE_ALPHA16UI_EXT',0x8D7B)
GL_LUMINANCE_ALPHA32I_EXT=_C('GL_LUMINANCE_ALPHA32I_EXT',0x8D87)
GL_LUMINANCE_ALPHA32UI_EXT=_C('GL_LUMINANCE_ALPHA32UI_EXT',0x8D75)
GL_LUMINANCE_ALPHA8I_EXT=_C('GL_LUMINANCE_ALPHA8I_EXT',0x8D93)
GL_LUMINANCE_ALPHA8UI_EXT=_C('GL_LUMINANCE_ALPHA8UI_EXT',0x8D81)
GL_LUMINANCE_ALPHA_INTEGER_EXT=_C('GL_LUMINANCE_ALPHA_INTEGER_EXT',0x8D9D)
GL_LUMINANCE_INTEGER_EXT=_C('GL_LUMINANCE_INTEGER_EXT',0x8D9C)
GL_RED_INTEGER_EXT=_C('GL_RED_INTEGER_EXT',0x8D94)
GL_RGB16I_EXT=_C('GL_RGB16I_EXT',0x8D89)
GL_RGB16UI_EXT=_C('GL_RGB16UI_EXT',0x8D77)
GL_RGB32I_EXT=_C('GL_RGB32I_EXT',0x8D83)
GL_RGB32UI_EXT=_C('GL_RGB32UI_EXT',0x8D71)
GL_RGB8I_EXT=_C('GL_RGB8I_EXT',0x8D8F)
GL_RGB8UI_EXT=_C('GL_RGB8UI_EXT',0x8D7D)
GL_RGBA16I_EXT=_C('GL_RGBA16I_EXT',0x8D88)
GL_RGBA16UI_EXT=_C('GL_RGBA16UI_EXT',0x8D76)
GL_RGBA32I_EXT=_C('GL_RGBA32I_EXT',0x8D82)
GL_RGBA32UI_EXT=_C('GL_RGBA32UI_EXT',0x8D70)
GL_RGBA8I_EXT=_C('GL_RGBA8I_EXT',0x8D8E)
GL_RGBA8UI_EXT=_C('GL_RGBA8UI_EXT',0x8D7C)
GL_RGBA_INTEGER_EXT=_C('GL_RGBA_INTEGER_EXT',0x8D99)
GL_RGBA_INTEGER_MODE_EXT=_C('GL_RGBA_INTEGER_MODE_EXT',0x8D9E)
GL_RGB_INTEGER_EXT=_C('GL_RGB_INTEGER_EXT',0x8D98)
@_f
@_p.types(None,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint)
def glClearColorIiEXT(red,green,blue,alpha):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint,_cs.GLuint,_cs.GLuint)
def glClearColorIuiEXT(red,green,blue,alpha):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glGetTexParameterIivEXT(target,pname,params):pass
# Calculate length of params from pname:GetTextureParameter
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLuintArray)
def glGetTexParameterIuivEXT(target,pname,params):pass
# Calculate length of params from pname:GetTextureParameter
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glTexParameterIivEXT(target,pname,params):pass
# Calculate length of params from pname:TextureParameterName
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLuintArray)
def glTexParameterIuivEXT(target,pname,params):pass
# Calculate length of params from pname:TextureParameterName
