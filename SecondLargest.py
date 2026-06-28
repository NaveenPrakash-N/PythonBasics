a = [2,9,8]
b=[]

large = 0
second = 0

for i in a:
    if i not in b:
        b.append(i)


for i in b:
    if i >= large:
        second = large
        large = i
    elif i >= second:
        second = i
print(large,second)