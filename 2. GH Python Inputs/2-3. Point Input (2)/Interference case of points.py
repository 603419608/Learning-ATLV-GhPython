import Rhino.Geometry as rg
import sys

center_pts = []
dists = []
for cell in cells:
    #Finding the center point of a polyline(查找中心点)
    center = cell.CenterPoint()
    center_pts.append(center)
    
    #Calculating the distance from the nearest interference point to the center point.
    #(求中心点到最近干扰点的距离)
    min_distance =sys.float_info.max
    for pt in pts:
        distance = pt.DistanceToSquared(center)
        if distance < min_distance :
            min_distance = distance
    dists.append(min_distance)

#Mapping the nearest distance to a range of 0.2 to 0.85(把最近距离映射到0.2 to 0.85之间)
domain = rg.Interval(0.85,0.2)
dists_domain = rg.Interval(min(dists),max(dists))
circles = [rg.Circle(pt,domain.ParameterAt(dists_domain.NormalizedParameterAt(dists[i]))) for i,pt in enumerate(center_pts)]