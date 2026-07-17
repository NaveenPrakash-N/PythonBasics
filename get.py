import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos")
response.raise_for_status()  
data = response.json()


# for i in data:
#     print(i['title'])  



# for i in data:
#     if i['completed'] == True:
#         print(i)


# comp=0
# incomp = 0
# for i in data:
#     if i['completed'] == True:
#         comp+=1
#     else:
#         incomp+=1
# print("Completed tasks:", comp)
# print("Incomplete tasks:", incomp)



# for i in data:
#     if i['userId'] == 5:
#         print(i)


count = 0
longtitle = ""
for i in data:
    if len(i['title']) > count:
        count = len(i['title'])
        longtitle = i['title']
print("Longest title:", longtitle)