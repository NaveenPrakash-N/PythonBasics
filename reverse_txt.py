text = "Reverse this message!"
op = ''
reversed = text[::-1]
for i in range(len(reversed)):
    if reversed[i].isalpha():
        if i == 0:
            op += reversed[i].upper()
        elif reversed[i-1] == ' ':
            op += reversed[i].upper()
        else:
            op += reversed[i].lower()
    else:
            op += reversed[i]  
print(op)
