# ws_5_5.py

# 아래 함수를 수정하시오.
def even_elements(lst):
    result = []
    for num in lst:
        if num % 2 == 0:
            result.append(num)
    return result


def even_elements2(lst):
    result = []
    while lst:
        item = lst.pop(0)
        if item %  2 == 0:
            result.extend([item])
    return result


def even_elements3(lst):
    result = []
    l = len(lst)
    for i in range(l):
        item = lst.pop()
        if item %  2 == 0:
            result.extend([item])
    result.reverse()
    return result


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)
result = even_elements2(my_list)
print(result)
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements3(my_list)
print(result)
