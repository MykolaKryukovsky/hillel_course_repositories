
while True:
    try:
        operator = input("Please enter the operator: +, -, *, /, yes - exit: ")
        if operator == "yes":
            print("Exit calculator")
            break
        namber1 = float(input("Please enter the first number: "))
        namber2 = float(input("Please enter the second number: "))
        if operator == "+":
            print(namber1 + namber2)
        elif operator == "-":
            print(namber1 - namber2)
        elif operator == "*":
            print(namber1 * namber2)
        elif operator == "/":
            if namber2 == 0:
                print("Illegal division by zero operation")
            else:
                print(namber1 / namber2)
        else:
            print("An invalid operator was entered")
    except ValueError:
        print("Number input error!")
