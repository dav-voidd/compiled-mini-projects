#Word Frequency Counter
import string
from collections import Counter



def translate(text):
    translator = str.maketrans('', '', string.punctuation)
    new_text = text.translate(translator)
    split_raw = new_text.split()
    count_raw = Counter(split_raw)
    return count_raw



user_input = input("Raw String of Text: ")
counted_input = translate(user_input)


for i in counted_input:
    print(f"{i}: {counted_input.get(i)}")





