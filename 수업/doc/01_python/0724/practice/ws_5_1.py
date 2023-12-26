# ws_5_1.py

# 아래 함수를 수정하시오.
def reverse_string(text):
    return text[::-1]

def reverse_string2(text):
    return ''.join(list(reversed(text)))

# str -> list -> str
def reverse_string3(text):
    lst = list(text)
    lst.reverse()
    text = ''.join(lst)
    return text

def reverse_string4(text):
    lst = list(text)
    for i in range(len(lst) // 2):
        lst[i], lst[len(lst)-1-i] = lst[len(lst)-1-i], lst[i]
    return ''.join(lst)

result = reverse_string("Hello, World!")
print(result)
result2 = reverse_string2("Hello, World!")
print(result2)
result3 = reverse_string3("Hello, World!")
print(result3)
result4 = reverse_string4("Hello, World!")
print(result4)

