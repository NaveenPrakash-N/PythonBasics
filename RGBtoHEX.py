def rgb(r, g, b):
    value = [r,g,b]
    op = ''
    for i in value:
        if i < 0:
            op += '00'
        elif i > 255:
            op += 'ff'
        else:
            if len(hex(i)) == 3:
                op += hex(i)[0]
                op += hex(i)[2]
            else:
                op += hex(i)[2:]
    return ''.join([i.upper() if i.isalpha() else i for i in op])

print(rgb(148, 0, 211 ))