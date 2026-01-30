
string_number = (input("Enter a whole number: "))
final_number = int(string_number)

while final_number > 9:
    current_product = 1
    for digit in str(final_number):
        current_product *= int(digit)
    final_number = current_product
print(f"{string_number} -> {final_number}")