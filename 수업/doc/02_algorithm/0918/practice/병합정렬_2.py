import sys; sys.stdin = open('병합정렬_input.txt', 'r')


def merge_sort(arr):
    global cnt
    if len(arr) == 1:  # 리스트 원소가 하나 남을 때
        return arr
    else:
        m = len(arr) // 2
        left = arr[:m]  # 리스트 왼쪽 절반
        right = arr[m:]  # 오른쪽 절반
        left = merge_sort(left)  # 정렬된 리스트 리턴
        right = merge_sort(right)  # 정렬된 리스트 리턴

        left_idx = 0
        right_idx = 0
        i = 0
        while left_idx < len(left) and right_idx < len(right):  # 좌우 리스트에서 비교 대상이 남은 경우
            if left[left_idx] <= right[right_idx]:
                arr[i] = left[left_idx]
                left_idx += 1
            else:
                arr[i] = right[right_idx]
                right_idx += 1
            i += 1

        if left_idx < len(left):  # 왼쪽 리스트가 남은 경우
            arr[i:] = left[left_idx:]

        if right_idx < len(right):  # 오른쪽 리스트가 남은 경우
            arr[i:] = right[right_idx:]

        #########################################################
        if left[-1] > right[-1]:  # 왼쪽 마지막 원소가 큰 경우(문제)
            cnt += 1
        #########################################################

        return arr  # 왼쪽 오른쪽을 합쳐 정렬된 리스트 반환


T = int(input())
for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    arr = merge_sort(arr)
    print('#{} {} {}'.format(tc + 1, arr[N // 2], cnt))


























