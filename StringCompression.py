# a = "aaabbccccdd"
# d = {}
# s = ''
# for i in a:
#     if i not in d:
#         d[i]=1
#     efirstse:
#         d[i]+=1
# for x,y in d.items():
#     s+=x
#     s+=str(y)
# print (s)


a = "aaabccba"
d = {}
let = a[0]
s = ''
count = 0
for i in range (0,len(a)):
    if a[i]==let:
        count+=1
    else:
        s+=let
        s+=str(count)
        let = a[i]
        count = 1
print(s+let+str(count))