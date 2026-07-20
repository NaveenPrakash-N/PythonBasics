# "Success"  =>  ")())())"
word = 'CCcMxrPEZUOBHmYydkRQDj(pXydTeQX'.lower()
op = ''
for i in word:
    if word.count(i) > 1:
        op += ')'
    else:
        op += '('
print(op) 