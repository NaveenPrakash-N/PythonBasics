st = "The quick brown fox jumps over the lazy dog."
alpha = "abcdefghijklmnopqrstuvwxyz"
pana = ''
for i in st:
    if i.lower() not in pana and i.lower() in alpha:
        pana += i.lower()
if len(pana) == len(alpha):
    print("The string is a pangram.")
