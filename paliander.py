import re


def  is_palindrome(text):
    no_punctuation_marks = re.sub(r'[^a-zа-я0-9]', '', text.lower())
    reversed_no_marks = "".join(reversed(no_punctuation_marks))
    return no_punctuation_marks == reversed_no_marks

while True:
        operator = input("Please enter the numbers:  yes - exit: ")
        if operator == "yes":
            print("Exit: the program is over ", end='\n' "OK")
            break
        print(f"{operator} == {is_palindrome(operator)}")