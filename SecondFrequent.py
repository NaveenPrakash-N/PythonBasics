a = 'banana'
b = {}
c = []
for i in a:
    if i not in b:
        b[i]=1
    else:
        b[i]+=1
for x,y in b.items():
    c.append(y)
print(c)

# c.sort(reverse=True)
def second(c):
    d = c[0]
    for i in c:
        if i > d:
            d = i
    c.remove(d)
    d = c[0]
    for i in c:
        if i > d:
            d = i
    return d

g=second(c)


for x,y in b.items():
    if y == g:
        print(x)
