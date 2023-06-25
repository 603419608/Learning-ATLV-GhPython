import rhinoscriptsyntax as rs

a = [] # set an empty list(创建一个空列表存储生成的点)
for i in range(10):
    p = rs.AddPoint(i,0,0)
    a.append(p)

#List Comprehensions (列表解析)
b = [rs.AddPoint(0,0,i) for i in range(10)]