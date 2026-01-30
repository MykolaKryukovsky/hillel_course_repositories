import re

two_letters = input('Will enter two letters with a hyphen: ')
two_letters = re.sub(r'[^a-zA-Zа-яА-Я]', '', two_letters)
two_letters = list(two_letters)
start_letter = ord(two_letters[0])
end_letter = ord(two_letters[-1])


if start_letter > end_letter:
    for i in range(start_letter, ord('z') + 1):
        letter_chr_low = chr(i)
        print(letter_chr_low, end="")
    for b in range(ord('A'), end_letter + 1):
        letter_chr_up = chr(b)
        print(letter_chr_up, end="")
for letter in range(start_letter, end_letter + 1):
    letter_chr = chr(letter)
    letter_chr = re.sub(r'[^a-zA-Zа-яА-Я]', '', letter_chr)
    print(f'{letter_chr}', end="")