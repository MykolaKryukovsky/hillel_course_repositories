from itertools import count


def popular_words(text, words) -> dict:
    """
    This function returns the popularity words
    :param text: string
    :param words: list
    :return: dict
    """
    text_list_lower = text.lower().split()
    dictionary_searched_words = dict.fromkeys([s.lower() for s in words], 0)
    for word in dictionary_searched_words:
        repetition_counter = text_list_lower.count(word)
        dictionary_searched_words[word] = repetition_counter

    return dictionary_searched_words


words_text = 'When I was One I had just begun When I was Two I was nearly new '
search_words = ['i', 'was', 'three', 'near']

print(f"{popular_words(words_text,search_words)}")