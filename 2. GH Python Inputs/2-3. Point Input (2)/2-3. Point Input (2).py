import rhinoscriptsyntax as rs
import Rhino.Geometry as rg     

a = []
b = []
for pt in pts:
    if( pt.Y % 10 > 0 and pt.Y % 10 < 2):
        rect = rs.AddRectangle(rg.Plane.WorldXY, 1.5, 0.4)
        rs.MoveObject(rect, pt)
        rs.MoveObject(rect, rg.Vector3d(-0.75,-0.2,0))
        a.append(rect)
    else:
        dist = rs.Distance(pt, attr)
        circle = rs.AddCircle(pt, 0.02*dist)
        b.append(circle)
