import sys; sys.stdin = open('flatten_input.txt')
def min_max(arr, N):
    min_idx = max_idx = 0
    for i in range(1, N):
        if arr[max_idx] < arr[i]:
            max_idx = i
        if arr[min_idx] > arr[i]:
            min_idx = i

    return max_idx, min_idx

T = 10
for tc in range(1, T+1):
    dump_count = int(input())
    N = 100
    arr = list(map(int, input().split()))

    for _ in range(dump_count):
        max_idx, min_idx = min_max(arr, N)
        arr[max_idx] -= 1
        arr[min_idx] += 1

    # 반드시 최종덤프후에 최고점과 최저점의 높이차를 반환
    max_idx, min_idx = min_max(arr, N)
    print(f'#{tc} {arr[max_idx] - arr[min_idx]}')