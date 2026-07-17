text = "The sunset sets at twelve o' clock."
alphabet = [
    "a", "b", "c", "d", "e", "f", "g",
    "h", "i", "j", "k", "l", "m", "n",
    "o", "p", "q", "r", "s", "t", "u",
    "v", "w", "x", "y", "z"
    ]
op = ''
for letter in text:
    count = 0
    for alpha in alphabet:
        count += 1
        if letter.lower() == alpha:
            op += str(count) + ' '
            
print(op)

            