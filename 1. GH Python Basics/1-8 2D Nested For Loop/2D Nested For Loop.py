import Rhino.Geometry as rg
import math

pts = []
for i in range(100):
    for j in range(50):
        x = i*0.5
        y = j*0.5
        z = math.sin(i*0.1)*1;
        if(j%20 < 10):
            z *= (j%20)*0.2;
        else:
            z *= (20 - j%20)*0.2;
        pts.append(rg.Point3d(x,y,z))

#Create a NurbsSurface
srf = rg.NurbsSurface.CreateFromPoints(pts,100,50,3,3)