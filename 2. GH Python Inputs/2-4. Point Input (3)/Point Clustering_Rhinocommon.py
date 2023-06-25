
import Rhino.Geometry as rg


a = []
for pt in pts:
    closePts = []
    for pt2 in pts:
        dist = pt.DistanceTo(pt2)
        if(dist > 0 and dist < threshold): # exclude itself by > 0
            closePts.append(pt2)
    
    count = len(closePts)
    if(count >= 3):
        for cpt in closePts:
            zpt = rg.Point3d(pt.X, pt.Y, 0.5*(count-2))
            line = rg.Line(zpt, cpt)
            a.append(line)