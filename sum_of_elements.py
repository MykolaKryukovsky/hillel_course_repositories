
list5 = [0, 1, 7, 2, 4, 8]
even_indexes = []
last_element = list5[-1]
print(list5,"->",end=' ')
for index, element in enumerate(list5):
    if index % 2 == 0:
        even_indexes.append(element)
sum_even_indexes = sum(even_indexes)
result = sum_even_indexes * last_element
print(f"({even_indexes[0]} + {even_indexes[1]} + {even_indexes[2]}) * {sum_even_indexes} = {result}")


list6 = [1, 3, 5]
sum_even_indexes1 = 0
last_element1 = list6[-1]
print(list6,"->",end=' ')
for i in range(0, len(list6), 2):
        sum_even_indexes1 += list6[i]
print(sum_even_indexes1 * last_element1)


list7 = [6]
print(list7,"->",end=' ')
last_element2 = list7[-1]
print(last_element2 * (sum(list7[i] for i in range(0, len(list7), 2))))


list8 = [0]
print(list8,"->",end=' ')
last_element3 = list8[-1]
print(last_element3 * (sum(list8[::2])))
