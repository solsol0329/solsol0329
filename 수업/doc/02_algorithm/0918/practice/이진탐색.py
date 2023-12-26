import sys; sys.stdin = open('이진탐색_input.txt')

def binary_search(a, key):
    low, high = 0, len(a) - 1
    dir = -1    # 방향 미정, 왼쪽 0, 오른쪽 1
    while low <= high:
        mid = (low+high) // 2
        if key == a[mid]:   # 찾았을 때
            return 1
        elif key < a[mid]:  # 왼쪽(0)
            if dir == 0 :
                return 0
            else:
                high = mid - 1
                dir = 0
        else:               # 오른쪽(1)
            if dir == 1:
                return 0
            else:
                low = mid + 1
                dir = 1
    return 0

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    cnt = 0
    for i in range(M):
        cnt += binary_search(A, B[i])
    print(f'#{tc} {cnt}')
