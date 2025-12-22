
def second_index(text, some_str):
  first_index_some_str = text.find(some_str)
  if first_index_some_str != -1:
      second_index_some_str = text.find(some_str, first_index_some_str + 1)
      if second_index_some_str != -1:
         return second_index_some_str
      else:
          return None
  else:
      return None

user_text = input("Enter some text : ")
user_some_str = input("Enter a character to search for the index : ")
print(second_index(user_text, user_some_str))

