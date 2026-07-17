a1 = "xyaabbbccccdefww"
a2 = "xxxxyyyyabklmopq"
alpha = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
sorted = ''

for i in a1:
    if i not in sorted:
        sorted += i
for j in a2:
    if j not in sorted:
        sorted += j
for i in alpha:
    for j in list(sorted):
        if i == j:
            print(i, end = '')