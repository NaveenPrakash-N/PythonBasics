def nonrep(a):
    b= {}
    for i in a:
        if i not in b:
            b[i]=1
        else:
            b[i]+=1
    for x,y in b.items():
        if y == 1:
            return x
print(nonrep("aabbcdde"))