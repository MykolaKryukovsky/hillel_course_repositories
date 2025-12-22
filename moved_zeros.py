
list1 = [0, 1, 0, 12, 3]
print(list1,"->",end=' ')
for i in range(len(list1) - 1, -1, -1):
    if list1[i] == 0:
        list1.append(list1.pop(i))
print(list1)


list2 = [1, 0, 13, 0, 0, 0, 5]
print(list2,"->",end=' ')
list2 = sorted(list2, key=lambda x: (x != 0), reverse=True)
print(list2)


list3 = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
print(list3,"->",end=' ')
non_zeros = [x for x in list3 if x != 0]
zeros = [x for x in list3 if x == 0]
list3 = non_zeros + zeros
print(list3)


list4 = []
print(list4,"->",end=' ')
list4.sort(key=bool, reverse=True)
print(list4)
