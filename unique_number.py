from collections import Counter
import re

def find_unique_value(some_list):
    some_list = re.findall(r'-?\d+\.?\d*', some_list)
    unique_list = Counter(some_list)
    unique_items = []
    for item, count in unique_list.items():
        if count == 1:
            unique_items.append(item)
    if len(unique_items) == 2 or len(unique_items) > 2:
        return None
    else:
        unique_one = "".join(unique_items)
        return unique_one


while True:
        operator = input("Please enter the numbers:  yes - exit: ")
        if operator == "yes":
            print("Exit: the program is over ", end='\n' "OK")
            break
        print(f"{find_unique_value(operator)}")