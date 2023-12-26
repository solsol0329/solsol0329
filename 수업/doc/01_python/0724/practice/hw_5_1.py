# main.py

# 아래 함수를 수정하시오.
def count_character(text, char):
    cnt = 0
    for c in text:
        if c == char:
            cnt += 1
    return cnt

def count_character2(text, char):
    return text.count(char)

# 아래 코드는 절대 수정하지 마시오.
result = count_character("Hello, World!", "o")
print(result) # 2
result = count_character2("Hello, World!", "o")
print(result) # 2
