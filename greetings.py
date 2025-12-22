def say_hi(name, age) -> str:
    return f"Hi, {name}! You are {age} years old, you look good!"

user_name = input("What is your name? : ")
user_age = int(input("And your age? : "))

print(say_hi(user_name, user_age))

