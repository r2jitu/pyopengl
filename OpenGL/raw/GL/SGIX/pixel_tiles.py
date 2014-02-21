'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_SGIX_pixel_tiles'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_SGIX_pixel_tiles',error_checker=_errors._error_checker)
GL_PIXEL_TILE_BEST_ALIGNMENT_SGIX=_C('GL_PIXEL_TILE_BEST_ALIGNMENT_SGIX',0x813E)
GL_PIXEL_TILE_CACHE_INCREMENT_SGIX=_C('GL_PIXEL_TILE_CACHE_INCREMENT_SGIX',0x813F)
GL_PIXEL_TILE_CACHE_SIZE_SGIX=_C('GL_PIXEL_TILE_CACHE_SIZE_SGIX',0x8145)
GL_PIXEL_TILE_GRID_DEPTH_SGIX=_C('GL_PIXEL_TILE_GRID_DEPTH_SGIX',0x8144)
GL_PIXEL_TILE_GRID_HEIGHT_SGIX=_C('GL_PIXEL_TILE_GRID_HEIGHT_SGIX',0x8143)
GL_PIXEL_TILE_GRID_WIDTH_SGIX=_C('GL_PIXEL_TILE_GRID_WIDTH_SGIX',0x8142)
GL_PIXEL_TILE_HEIGHT_SGIX=_C('GL_PIXEL_TILE_HEIGHT_SGIX',0x8141)
GL_PIXEL_TILE_WIDTH_SGIX=_C('GL_PIXEL_TILE_WIDTH_SGIX',0x8140)

