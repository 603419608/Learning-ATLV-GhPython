#importing modules. (导入模块的3种方式)
import rhinoscriptsyntax as rs
from Rhino.Geometry import Point3d
ma = __import__("math")



text = "hello world"
print text

# comment (单行注释#)
a = rs.AddPoint(0,0,0)

"""
(多行注释""""""")
Creating a point using Rhinocommon.(使用Rhinocommon创建一个点)
"""
b = Point3d(10,10,10)


c = x + y