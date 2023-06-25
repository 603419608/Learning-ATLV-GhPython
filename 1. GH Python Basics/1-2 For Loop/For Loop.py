import rhinoscriptsyntax as rs

print("================= For loop =================")
#For loop
for i in range(10):
    print(i)

print("================= While loop =================")
#While loop
num = 0
a = []
while (num<10):
    a.append(rs.AddPoint(num,0,0))
    print num
    num += 1

print("================= continue =================")
#continue
for i in range(10):
    if(i%2==0):
        continue
    print i

print("================= break =================")
#break
for i in range(10):
    print i
    if(i%2==0):
        break