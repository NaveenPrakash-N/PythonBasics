n = 1234
storage = ''
while n > 0:
    storage += str(n % 2)
    n = n // 2
print(storage[::-1])

print(len([i for i in storage[::-1] if i == '1']))