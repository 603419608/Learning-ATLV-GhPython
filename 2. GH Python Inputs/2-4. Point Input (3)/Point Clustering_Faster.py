import Rhino.Geometry as rg
import scriptcontext as sc


a = []

#初始化字典
for i in xrange(len(pts)):sc.sticky[i] = []

sq_dis = threshold*threshold

# 计算所有点之间的距离，并记录靠近的点
for i, pt in enumerate(pts):
    for j, pt2 in enumerate(pts[i+1:], i+1):
        if pt.DistanceToSquared(pt2) < sq_dis:
            sc.sticky[i].append(pt2)
            sc.sticky[j].append(pt)
    
    # 构建连接线
    close_pts = sc.sticky[i]
    count = len(close_pts)
    if count > 2:
        zpt = rg.Point3d(pt.X, pt.Y, 0.5 * (count - 2))
        lines = [rg.Line(zpt, cpt) for cpt in close_pts]
        a.extend(lines)