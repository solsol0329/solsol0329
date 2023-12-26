# ws_5_2.py

# 아래 함수를 수정하시오.
def remove_duplicates(lst):
    new_lst = []
    for num in lst:
        if num not in new_lst:  # 1 2 3 4 5
            new_lst.append(num)
    return new_lst

def remove_duplicates2(lst):
    return list(set(lst))

def remove_duplicates3(lst):
    # 카운팅 배열을 0으로 초기화
    counts = [0] * (5+1)
    # 카운팅 
    for num in lst:
        counts[num] += 1  # 리스트의 인덱스 값을 기준으로 값을 증가

    # counts에서 값이 0아닌 인덱스만 lst에 추가
    lst = []
    for i in range(len(counts)):
        if counts[i]:
            lst.append(i)
    return lst

result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
print(result)
result = remove_duplicates2([1, 2, 2, 3, 4, 4, 5])
print(result)
result = remove_duplicates3([1, 2, 2, 3, 4, 4, 5])
print(result)
