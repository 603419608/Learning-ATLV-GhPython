import Rhino.Geometry as rg
import math

pts = []
for i in range(u_count):
    for j in range(v_count):
        p = rg.Point3d(i, j, math.sin(i*u) * math.sin(j*u) * z)
        pts.append(p)
#Creating a grid of points using list comprehension.
#pts2 = [rg.Point3d(i, j, math.sin(i*u) * math.sin(j*u) * z)  for i in range(u_count) for j in range(v_count)]
srf = rg.NurbsSurface.CreateFromPoints(pts,u_count,v_count,3,3)