# ws_5_4.py

# 아래 함수를 수정하시오.
def capitalize_words(text):
    words = text.split()
    capitalized_words = []
    for word in words:
        capitalized_words.append(word.capitalize())
    return ' '.join(capitalized_words)


def capitalize_words2(text):
    return text.title()

result = capitalize_words("hello, world!")
print(result)
result = capitalize_words2("hello, world!")
print(result)
