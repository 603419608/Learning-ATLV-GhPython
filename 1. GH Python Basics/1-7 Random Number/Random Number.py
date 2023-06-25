import Rhino.Geometry as rg
import random
import math

a = []
for i in range(500):
    x = math.cos(i*0.2) * i*0.1
    y = math.sin(i*0.2) * i*0.08
    if(i<200):
        z = 0
    else:
        z = random.random() * (i-200)* 0.02
    a.append(rg.Point3d(x,y,z))