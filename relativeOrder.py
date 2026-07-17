alice = [8, 5, 4, 3]
bob   = [9, 8, 1, 5, 3]

alicelst = []
boblst = []
for i in alice:
    if i in bob:
        alicelst.append(i)
for i in bob:
    if i in alice:
        boblst.append(i)
if alicelst == boblst:
    print(True)
else:
    print(False)