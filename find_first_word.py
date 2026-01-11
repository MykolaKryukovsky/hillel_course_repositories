import string

def first_word(text):
    """ First word search """
    """
    :param text: string
    :return: string
    """
    text_list = text
    for punc in string.punctuation.replace("'", ""):
        text_list = text_list.replace(punc, " ")
    first_word = text_list.split()

    return f"{first_word[0]}"

assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')