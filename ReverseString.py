# a = "Naveen"
# b=""
# for i in range (len(a)-1,-1,-1):
#     b=b+a[i]
# print(b)



# advanced
a = "I Love Python"
lst = []
word=' '
op = ''
for i in a:
    if i == " ":
        lst.append(word)
        word = ' '
    else:
        word+=i
lst.append(word)

for j in lst:
    for i in range(len(j)-1,-1,-1):
        op+=j[i]
print(op)    