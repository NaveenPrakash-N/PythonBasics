a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
alpha = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
sorted = ''

for i,j in zip(a,b):
    if i not in sorted:
        sorted += i
    if j not in sorted:
        sorted += j
print(list(sorted))

for i in alpha:
    for j in list(sorted):
        if i == j:
            print(i, end = '')