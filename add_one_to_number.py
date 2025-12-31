

def add_one(some_list):
    numeric = int("".join(str(d) for d in some_list)) + 1
    some_list = list(map(int, str(numeric)))
    return some_list

while True:
    try:
        operator = input("Please enter the numbers:  yes - exit: ")
        if operator == "yes":
            print("Exit: the program is over ", end='\n' "OK")
            break
        g = list(map(int, str(operator)))
        print(f"{g} == {add_one(g)}")
    except ValueError:
        print("Input error!")