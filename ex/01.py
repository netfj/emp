x = {'leg':2,'mouse':1}

class Person():
    leg = -1
    mouse = -1

for k,v in x.items():
    print(k,v)

p = Person()

print(p.leg,p.mouse)

bl = (dir(p))
for i in bl:
    print(i)
    print(type(i))
