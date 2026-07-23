walk = ['n','n','n','s','n','s','n','s','n','s']

if walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w') and len(walk) == 10:
    print(True)
else:
    print(False)