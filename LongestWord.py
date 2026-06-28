from itertools import count


a = "Python is very powerful programming language"
di = {}
st = '' 
count = 0
for i in a:
    if i == " ":

        di[st]=count
        st = ''
        count = 0
    else:
        count+=1
        st+=i
di[st]= count
val = float('-inf')
for x in di.values():
    if x >= val:
        val = x
for x,y in di.items():
    if y == val:
        print(x)

