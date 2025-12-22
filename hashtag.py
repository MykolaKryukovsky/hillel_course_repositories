import re

hashtag_unchanged = input("Enter the name of the hashtag: ")

cleaned_hashtag = re.sub(r'[^\w\s]', '', hashtag_unchanged)
changed_hashtag = cleaned_hashtag.title().split()
clean_hashtag = f'#{''.join(changed_hashtag)}'

if len(clean_hashtag) > 140:
    clean_hashtag = clean_hashtag[:140]

print(clean_hashtag)