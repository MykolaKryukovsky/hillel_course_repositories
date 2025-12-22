import keyword
import string

variable_name = input(f"Please enter the name of the variable: ")

incompatible_symbol = string.punctuation.replace('_', '') + string.whitespace
for char in variable_name:
    if variable_name.count('_') > 1:
        print(f"{False}")
        break
    elif char.isupper() or char in incompatible_symbol:
        print(f"{False}")
        break
    elif not variable_name or variable_name[0].isdigit():
        print(f"{False}")
        break
    elif keyword.iskeyword(variable_name):
         print(f"{False}")
         break
else:
    print(f"{True}")