a = "banana"
dic = {}
for i in a:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
print(dic)

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.keys()
# print(x)