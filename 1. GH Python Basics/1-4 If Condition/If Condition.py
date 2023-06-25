import rhinoscriptsyntax as rs

a = []
for i in range(10):
    if(i%2 == 0):
        p = rs.AddPoint(i,0,0)
    else:
        p = rs.AddPoint(i,0,5)
    a.append(p)

pl = rs.AddPolyline(a)