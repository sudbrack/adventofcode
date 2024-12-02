import json

with open('1/data.json', 'r') as file:
    data = json.load(file)

list1 = sorted(item[0] for item in data)
list2 = sorted(item[1] for item in data)

# print(list1)
# print(list2)

result = 0
for i in range(len(list1)):
    diff = abs(list1[i] - list2[i])
    result += diff
print(result)