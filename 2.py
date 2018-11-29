list1 = ["A","B"]
list2 = ["a","b","c"]
list3 = []
for i in  range(len(list1)):
    for j in range(len(list2)):
        list3.append([list1[i],list2[j]])

print(list3)