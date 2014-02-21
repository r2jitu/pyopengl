'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GLX import _types as _cs
# End users want this...
from OpenGL.raw.GLX._types import *
from OpenGL.raw.GLX import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GLX_NV_video_capture'
def _f( function ):
    return _p.createFunction( function,_p.GLX,'GLX_NV_video_capture',error_checker=_errors._error_checker)
GLX_DEVICE_ID_NV=_C('GLX_DEVICE_ID_NV',0x20CD)
GLX_NUM_VIDEO_CAPTURE_SLOTS_NV=_C('GLX_NUM_VIDEO_CAPTURE_SLOTS_NV',0x20CF)
GLX_UNIQUE_ID_NV=_C('GLX_UNIQUE_ID_NV',0x20CE)
@_f
@_p.types(_cs.c_int,ctypes.POINTER(_cs.Display),_cs.c_uint,_cs.GLXVideoCaptureDeviceNV)
def glXBindVideoCaptureDeviceNV(dpy,video_capture_slot,device):pass
@_f
@_p.types(ctypes.POINTER(_cs.GLXVideoCaptureDeviceNV),ctypes.POINTER(_cs.Display),_cs.c_int,ctypes.POINTER(_cs.c_int))
def glXEnumerateVideoCaptureDevicesNV(dpy,screen,nelements):pass
@_f
@_p.types(None,ctypes.POINTER(_cs.Display),_cs.GLXVideoCaptureDeviceNV)
def glXLockVideoCaptureDeviceNV(dpy,device):pass
@_f
@_p.types(_cs.c_int,ctypes.POINTER(_cs.Display),_cs.GLXVideoCaptureDeviceNV,_cs.c_int,ctypes.POINTER(_cs.c_int))
def glXQueryVideoCaptureDeviceNV(dpy,device,attribute,value):pass
@_f
@_p.types(None,ctypes.POINTER(_cs.Display),_cs.GLXVideoCaptureDeviceNV)
def glXReleaseVideoCaptureDeviceNV(dpy,device):pass
