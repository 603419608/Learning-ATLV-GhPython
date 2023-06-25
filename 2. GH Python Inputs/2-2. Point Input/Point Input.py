import rhinoscriptsyntax as rs
import math

a = []
b = []
c = []
for pt in pts:
    if(pt.X % 3 < 0.5):
        a.append(pt)
    elif( math.sqrt(abs(pt.Y)) %0.5 < 0.1):
        b.append(pt)
        """
        The math.sqrt function does not accept negative numbers,
        so it needs to be preceded by the abs function to take the absolute value.
        math.sqrt函数不能输入负数，所以需要加一个abs函数取绝对值.
        """
    else:
        c.append(pt)