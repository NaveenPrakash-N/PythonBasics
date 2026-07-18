s = "aaabbbbhaijjjm"
good = "abcdefghijklm"
goodCount = 0
for i in s:
    if i in good:
        goodCount += 1
print(f"{len(s) - goodCount}/{len(s)}")

a = [1 for i in s if i in good]
print(a)