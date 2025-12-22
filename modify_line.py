"""
        :param: the first  word after the point always uppercase,
        others lowercase, always a dot at the end
        :return: string
        """
def correct_sentence(text) -> str:
    if not text:
        return "Please enter a sentence!"
    text = text.split(". ")
    text = ". ".join([p.capitalize() for p in text])
    if not text.endswith("."):
        text += "."
    return text

same_txt = input("Please enter some text: ")

print(correct_sentence(same_txt))