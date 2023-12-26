import sys; sys.stdin = open('병합정렬_input.txt')
from collections import deque

def merge(left, right):
    left = deque(left)
    right = deque(right)
    result = []
    # 두리스트 중에 하나가 남으면
    while left and right:
    # 둘 다 남았을 때
        if left[0] < right[0]:
            result.append(left.popleft())
        else:
            result.append(right.popleft())
    # 왼쪽만 남았을 때
    if left:
        # result.append(left.popleft())
        result += left  # extend
    # 오른쪽만 남았을 때
    if right:
        # result.append(right.popleft())
        result.extend(right)
    return result


def merge_sort(a):
    global cnt
    if len(a) == 1:
        return a
    # 문제를 절반으로 나누어 각각 별도의 정렬 진행
    else:
        mid = len(a)//2
        left = merge_sort(a[:mid])
        right = merge_sort(a[mid:])
        if left[-1] > right[-1]:
            cnt += 1
        return merge(left, right)



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    arr = merge_sort(arr)  # 비파괴형
    print(f'#{tc} {arr[N//2]} {cnt}')