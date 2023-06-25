import Rhino.Geometry as rg
import math

pts = []
for i in range(u_count):
    for j in range(v_count):
        x = i*0.5
        y = j*0.5
        if( i<20 and j<20 ):
            z = 2
        elif( i>=20 and i<40 and j>=60 and j<80):
            z = 1
        elif( i==50 or j==50):
            z = 2
        elif( i>=60 and i<80 and j>=20 and j<80):
            z = math.cos(j*0.2)+2
        elif( not i>60 and j>=25 and j<35):
            z = 8 - i*0.1
        elif( not (i<90 and j<90) ):
             z = math.sin(i*0.2) * math.cos(j*0.2)+2
        else:
            z = math.cos(i*0.1) * math.sin(j*0.1)
        pts.append(rg.Point3d(x,y,z))

srf = rg.NurbsSurface.CreateFromPoints(pts,u_count,v_count,3,3)