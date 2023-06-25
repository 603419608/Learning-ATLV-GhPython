import rhinoscriptsyntax as rs

a = []
for i in range(10):
    if(i < 5):
        p = rs.AddPoint(i,0,0)
    elif(i < 8):
        p = rs.AddPoint(i,0,6)
    else:
        p = rs.AddPoint(i,0,2)
    a.append(p)

pl = rs.AddPolyline(a)