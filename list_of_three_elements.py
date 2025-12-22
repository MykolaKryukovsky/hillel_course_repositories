
import random

array_random_numbers = []
three_numbers_selected = []
while len(array_random_numbers) < 10:
    array_random_numbers.append(random.randint(1,10))
print(array_random_numbers, "->",end=' ')
for index, element in enumerate(array_random_numbers):
    if index == 0 or index == 2 or index == len(array_random_numbers)-2 :
        three_numbers_selected.append(element)
print(three_numbers_selected)


array_random_numbers1 = []
three_numbers_selected1 = []

for i in range(4):
    array_random_numbers1.append(random.randint(1,10))
for index, element in enumerate(array_random_numbers1):
    if index == 0 or index == 2:
       three_numbers_selected1.append(element)
a = array_random_numbers1[-2]
three_numbers_selected1.append(a)
print(array_random_numbers1, "->", end=' ')
print(three_numbers_selected1)


array_random_numbers2 = [random.choice([i for i in range(10)]) for j in range(3)]
three_numbers_selected2 = []
for index, element in enumerate(array_random_numbers2):
    if index == 0 or index == 2:
        three_numbers_selected2.append(element)
a1 = array_random_numbers2[-2]
three_numbers_selected2.append(a1)
print(array_random_numbers2, "->", three_numbers_selected2)
