'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_OES_fixed_point'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_OES_fixed_point',error_checker=_errors._error_checker)
GL_FIXED_OES=_C('GL_FIXED_OES',0x140C)
@_f
@_p.types(None,_cs.GLenum,_cs.GLfixed)
def glAccumxOES(op,value):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLfixed)
def glAlphaFuncxOES(func,ref):pass
@_f
@_p.types(None,_cs.GLsizei,_cs.GLsizei,_cs.GLfixed,_cs.GLfixed,_cs.GLfixed,_cs.GLfixed,arrays.GLubyteArray)
def glBitmapxOES(width,height,xorig,yorig,xmove,ymove,bitmap):pass
@_f
@_p.types(None,_cs.GLfixed,_cs.GLfixed,_cs.GLfixed,_cs.GLfixed)
def glBlendColorxOES(red,green,blue,alpha):pass
@_f
@_p.types(None,_cs.GLfixed,_cs.GLfixed,_cs.GLfixed,_cs.GLfixed)
def glClearAccumxOES(red,green,blue,alpha):pass
@_f
@_p.types(None,_cs.GLfixed,_cs.GLfixed,_cs.GLfixed,_cs.GLfixed)
def glClearColorxOES(red,green,blue,alpha):pass
@_f
@_p.types(None,_cs.GLfixed)
def glClearDepthxOES(depth):pass
@_f
@_p.types(None,_cs.GLenum,ctypes.POINTER(_cs.GLfixed))
def glClipPlanexOES(plane,equation):pass
@_f
@_p.types(None,_cs.GLfixed,_cs.GLfixed,_cs.GLfixed)
def glColor3xOES(red,green,blue):pass
@_f
@_p.types(None,ctypes.POINTER(_cs.GLfixed))
def glColor3xvOES(components):pass
@_f
@_p.types(None,_cs.GLfixed,_cs.GLfixed,_cs.GLfixed,_cs.GLfixed)
def glColor4xOES(red,green,blue,alpha):pass
@_f
@_p.types(None,ctypes.POINTER(_cs.GLfixed))
def glColor4xvOES(components):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLfixed)
def glConvolutionParameterxOES(target,pname,param):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,ctypes.POINTER(_cs.GLfixed))
def glConvolutionParameterxvOES(target,pname,params):pass
@_f
@_p.types(None,_cs.GLfixed,_cs.GLfixed)
def glDepthRangexOES(n,f):pass
@_f
@_p.types(None,_cs.GLfixed)
def glEvalCoord1xOES(u):pass
@_f
@_p.types(None,ctypes.POINTER(_cs.GLfixed))
def glEvalCoord1xvOES(coords):pass
@_f
@_p.types(None,_cs.GLfixed,_cs.GLfixed)
def glEvalCoord2xOES(u,v):pass
@_f
@_p.types(None,ctypes.POINTER(_cs.GLfixed))
def glEvalCoord2xvOES(coords):pass
@_f
@_p.types(None,_cs.GLsizei,_cs.GLenum,ctypes.POINTER(_cs.GLfixed))
def glFeedbackBufferxOES(n,type,buffer):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLfixed)
def glFogxOES(pname,param):pass
@_f
@_p.types(None,_cs.GLenum,ctypes.POINTER(_cs.GLfixed))
def glFogxvOES(pname,param):pass
@_f
@_p.types(None,_cs.GLfixed,_cs.GLfixed,_cs.GLfixed,_cs.GLfixed,_cs.GLfixed,_cs.GLfixed)
def glFrustumxOES(l,r,b,t,n,f):pass
@_f
@_p.types(None,_cs.GLenum,ctypes.POINTER(_cs.GLfixed))
def glGetClipPlanexOES(plane,equation):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,ctypes.POINTER(_cs.GLfixed))
def glGetConvolutionParameterxvOES(target,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,ctypes.POINTER(_cs.GLfixed))
def glGetFixedvOES(pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,ctypes.POINTER(_cs.GLfixed))
def glGetHistogramParameterxvOES(target,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,ctypes.POINTER(_cs.GLfixed))
def glGetLightxOES(light,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,ctypes.POINTER(_cs.GLfixed))
def glGetLightxvOES(light,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,ctypes.POINTER(_cs.GLfixed))
def glGetMapxvOES(target,query,v):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLfixed)
def glGetMaterialxOES(face,pname,param):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,ctypes.POINTER(_cs.GLfixed))
def glGetMaterialxvOES(face,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,ctypes.POINTER(_cs.GLfixed))
def glGetPixelMapxv(map,size,values):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,ctypes.POINTER(_cs.GLfixed))
def glGetTexEnvxvOES(target,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,ctypes.POINTER(_cs.GLfixed))
def glGetTexGenxvOES(coord,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,_cs.GLenum,ctypes.POINTER(_cs.GLfixed))
def glGetTexLevelParameterxvOES(target,level,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,ctypes.POINTER(_cs.GLfixed))
def glGetTexParameterxvOES(target,pname,params):pass
@_f
@_p.types(None,_cs.GLfixed)
def glIndexxOES(component):pass
@_f
@_p.types(None,ctypes.POINTER(_cs.GLfixed))
def glIndexxvOES(component):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLfixed)
def glLightModelxOES(pname,param):pass
@_f
@_p.types(None,_cs.GLenum,ctypes.POINTER(_cs.GLfixed))
def glLightModelxvOES(pname,param):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLfixed)
def glLightxOES(light,pname,param):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,ctypes.POINTER(_cs.GLfixed))
def glLightxvOES(light,pname,params):pass
@_f
@_p.types(None,_cs.GLfixed)
def glLineWidthxOES(width):pass
@_f
@_p.types(None,ctypes.POINTER(_cs.GLfixed))
def glLoadMatrixxOES(m):pass
@_f
@_p.types(None,ctypes.POINTER(_cs.GLfixed))
def glLoadTransposeMatrixxOES(m):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLfixed,_cs.GLfixed,_cs.GLint,_cs.GLint,_cs.GLfixed)
def glMap1xOES(target,u1,u2,stride,order,points):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLfixed,_cs.GLfixed,_cs.GLint,_cs.GLint,_cs.GLfixed,_cs.GLfixed,_cs.GLint,_cs.GLint,_cs.GLfixed)
def glMap2xOES(target,u1,u2,ustride,uorder,v1,v2,vstride,vorder,points):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLfixed,_cs.GLfixed)
def glMapGrid1xOES(n,u1,u2):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLfixed,_cs.GLfixed,_cs.GLfixed,_cs.GLfixed)
def glMapGrid2xOES(n,u1,u2,v1,v2):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLfixed)
def glMaterialxOES(face,pname,param):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,ctypes.POINTER(_cs.GLfixed))
def glMaterialxvOES(face,pname,param):pass
@_f
@_p.types(None,ctypes.POINTER(_cs.GLfixed))
def glMultMatrixxOES(m):pass
@_f
@_p.types(None,ctypes.POINTER(_cs.GLfixed))
def glMultTransposeMatrixxOES(m):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLfixed)
def glMultiTexCoord1xOES(texture,s):pass
@_f
@_p.types(None,_cs.GLenum,ctypes.POINTER(_cs.GLfixed))
def glMultiTexCoord1xvOES(texture,coords):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLfixed,_cs.GLfixed)
def glMultiTexCoord2xOES(texture,s,t):pass
@_f
@_p.types(None,_cs.GLenum,ctypes.POINTER(_cs.GLfixed))
def glMultiTexCoord2xvOES(texture,coords):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLfixed,_cs.GLfixed,_cs.GLfixed)
def glMultiTexCoord3xOES(texture,s,t,r):pass
@_f
@_p.types(None,_cs.GLenum,ctypes.POINTER(_cs.GLfixed))
def glMultiTexCoord3xvOES(texture,coords):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLfixed,_cs.GLfixed,_cs.GLfixed,_cs.GLfixed)
def glMultiTexCoord4xOES(texture,s,t,r,q):pass
@_f
@_p.types(None,_cs.GLenum,ctypes.POINTER(_cs.GLfixed))
def glMultiTexCoord4xvOES(texture,coords):pass
@_f
@_p.types(None,_cs.GLfixed,_cs.GLfixed,_cs.GLfixed)
def glNormal3xOES(nx,ny,nz):pass
@_f
@_p.types(None,ctypes.POINTER(_cs.GLfixed))
def glNormal3xvOES(coords):pass
@_f
@_p.types(None,_cs.GLfixed,_cs.GLfixed,_cs.GLfixed,_cs.GLfixed,_cs.GLfixed,_cs.GLfixed)
def glOrthoxOES(l,r,b,t,n,f):pass
@_f
@_p.types(None,_cs.GLfixed)
def glPassThroughxOES(token):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,ctypes.POINTER(_cs.GLfixed))
def glPixelMapx(map,size,values):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLfixed)
def glPixelStorex(pname,param):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLfixed)
def glPixelTransferxOES(pname,param):pass
@_f
@_p.types(None,_cs.GLfixed,_cs.GLfixed)
def glPixelZoomxOES(xfactor,yfactor):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLfixed)
def glPointParameterxOES(pname,param):pass
@_f
@_p.types(None,_cs.GLenum,ctypes.POINTER(_cs.GLfixed))
def glPointParameterxvOES(pname,params):pass
@_f
@_p.types(None,_cs.GLfixed)
def glPointSizexOES(size):pass
@_f
@_p.types(None,_cs.GLfixed,_cs.GLfixed)
def glPolygonOffsetxOES(factor,units):pass
@_f
@_p.types(None,_cs.GLsizei,arrays.GLuintArray,ctypes.POINTER(_cs.GLfixed))
def glPrioritizeTexturesxOES(n,textures,priorities):pass
@_f
@_p.types(None,_cs.GLfixed,_cs.GLfixed)
def glRasterPos2xOES(x,y):pass
@_f
@_p.types(None,ctypes.POINTER(_cs.GLfixed))
def glRasterPos2xvOES(coords):pass
@_f
@_p.types(None,_cs.GLfixed,_cs.GLfixed,_cs.GLfixed)
def glRasterPos3xOES(x,y,z):pass
@_f
@_p.types(None,ctypes.POINTER(_cs.GLfixed))
def glRasterPos3xvOES(coords):pass
@_f
@_p.types(None,_cs.GLfixed,_cs.GLfixed,_cs.GLfixed,_cs.GLfixed)
def glRasterPos4xOES(x,y,z,w):pass
@_f
@_p.types(None,ctypes.POINTER(_cs.GLfixed))
def glRasterPos4xvOES(coords):pass
@_f
@_p.types(None,_cs.GLfixed,_cs.GLfixed,_cs.GLfixed,_cs.GLfixed)
def glRectxOES(x1,y1,x2,y2):pass
@_f
@_p.types(None,ctypes.POINTER(_cs.GLfixed),ctypes.POINTER(_cs.GLfixed))
def glRectxvOES(v1,v2):pass
@_f
@_p.types(None,_cs.GLfixed,_cs.GLfixed,_cs.GLfixed,_cs.GLfixed)
def glRotatexOES(angle,x,y,z):pass
@_f
@_p.types(None,_cs.GLfixed,_cs.GLboolean)
def glSampleCoverageOES(value,invert):pass
@_f
@_p.types(None,_cs.GLclampx,_cs.GLboolean)
def glSampleCoveragexOES(value,invert):pass
@_f
@_p.types(None,_cs.GLfixed,_cs.GLfixed,_cs.GLfixed)
def glScalexOES(x,y,z):pass
@_f
@_p.types(None,_cs.GLfixed)
def glTexCoord1xOES(s):pass
@_f
@_p.types(None,ctypes.POINTER(_cs.GLfixed))
def glTexCoord1xvOES(coords):pass
@_f
@_p.types(None,_cs.GLfixed,_cs.GLfixed)
def glTexCoord2xOES(s,t):pass
@_f
@_p.types(None,ctypes.POINTER(_cs.GLfixed))
def glTexCoord2xvOES(coords):pass
@_f
@_p.types(None,_cs.GLfixed,_cs.GLfixed,_cs.GLfixed)
def glTexCoord3xOES(s,t,r):pass
@_f
@_p.types(None,ctypes.POINTER(_cs.GLfixed))
def glTexCoord3xvOES(coords):pass
@_f
@_p.types(None,_cs.GLfixed,_cs.GLfixed,_cs.GLfixed,_cs.GLfixed)
def glTexCoord4xOES(s,t,r,q):pass
@_f
@_p.types(None,ctypes.POINTER(_cs.GLfixed))
def glTexCoord4xvOES(coords):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLfixed)
def glTexEnvxOES(target,pname,param):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,ctypes.POINTER(_cs.GLfixed))
def glTexEnvxvOES(target,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLfixed)
def glTexGenxOES(coord,pname,param):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,ctypes.POINTER(_cs.GLfixed))
def glTexGenxvOES(coord,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLfixed)
def glTexParameterxOES(target,pname,param):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,ctypes.POINTER(_cs.GLfixed))
def glTexParameterxvOES(target,pname,params):pass
@_f
@_p.types(None,_cs.GLfixed,_cs.GLfixed,_cs.GLfixed)
def glTranslatexOES(x,y,z):pass
@_f
@_p.types(None,_cs.GLfixed)
def glVertex2xOES(x):pass
@_f
@_p.types(None,ctypes.POINTER(_cs.GLfixed))
def glVertex2xvOES(coords):pass
@_f
@_p.types(None,_cs.GLfixed,_cs.GLfixed)
def glVertex3xOES(x,y):pass
@_f
@_p.types(None,ctypes.POINTER(_cs.GLfixed))
def glVertex3xvOES(coords):pass
@_f
@_p.types(None,_cs.GLfixed,_cs.GLfixed,_cs.GLfixed)
def glVertex4xOES(x,y,z):pass
@_f
@_p.types(None,ctypes.POINTER(_cs.GLfixed))
def glVertex4xvOES(coords):pass
