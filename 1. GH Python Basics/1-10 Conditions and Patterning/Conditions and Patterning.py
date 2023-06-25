import Rhino.Geometry as rg
import math
import math

pts = []
for i in range(100):
    for j in range(100):
        x = i*0.5
        y = j*0.5
        if( i%20<4 or j%20<4 ):
            z = 0
        elif( i%20+j%20 > 20):
            z = ((20 - i%20) * (j%20))*0.03
            z += math.cos(i*0.1) * math.sin(j*0.1)*2+2
        elif( i%20>=5 and j%20<10 ):
            z = ((i%20)*(i%20)/20 + (j%20)/2)*0.3
        else:
            z = ((i%20)*0.2 + (j%20)*0.3)
        pts.append(rg.Point3d(x,y,z))