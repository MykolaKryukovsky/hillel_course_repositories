import sys

print("Enter the number of seconds you want to convert to a readable time format")
seconds = int(input("But not more than (8640000): "))
days = 0
hours = 0
minutes = 0
remaining_seconds = 0
dict_days = {"день": "день", "дні": "дні", "днів": "днів"}

if seconds > 8640000:
    print("A critical error has occurred! Completion of work!!!")
    print(f"The number exceeds the allowed value: {seconds} > 8640000!!!")
    sys.exit(1)

if seconds == 0:
    print(f"{seconds} -> {days} {dict_days["днів"]}, {str(hours).zfill(2)}:"
          f"{str(minutes).zfill(2)}:{str(remaining_seconds).zfill(2)}")

if seconds > 0:
    days = seconds // 86400
    remaining_seconds = seconds % 86400
    hours = remaining_seconds // 3600
    remaining_seconds = remaining_seconds % 3600
    minutes = remaining_seconds // 60
    remaining_seconds = remaining_seconds % 60
    print(f"{seconds} -> {days}", end=" ")
    if 5 <= days % 100 <= 19 or days == 100 or days == 0 or days == 99:
        print(f"{dict_days["днів"]}, {str(hours).zfill(2)}:", end="")
    elif days % 10 in [2, 3, 4,]:
        print(f"{dict_days["дні"]}, {str(hours).zfill(2)}:", end="")
    elif days % 10 == 1:
        print(f"{dict_days["день"]}, {str(hours).zfill(2)}:", end="")
    print(f"{str(minutes).zfill(2)}:{str(remaining_seconds).zfill(2)}")