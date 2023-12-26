# main.py

# 아래 함수를 수정하시오.
def find_min_max(lst):
    min_v = 987654321  
    max_v = 0
    # min_v = max_v = lst[0]
    for num in lst:
        if min_v > num:
            min_v = num
        if max_v < num:
            max_v = num

    return (min_v, max_v)


def find_sum(lst):
    sum_v = 0
    cnt = 0
    for num in lst:
        sum_v = sum_v + num
        cnt += 1
    return sum_v / cnt

result = find_min_max([3, 1, 7, 2, 5])
result2 = find_sum([3, 1, 7, 2, 5])
print(result) # (1, 7)
print(result2) # 18