import sys; sys.stdin = open('sum_input.txt')

N = 100
T = 10
for tc in range(1, T+1):
    temp = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0
    # 행우선
    for i in range(N):
        total = 0
        for j in range(N):
            total += arr[i][j]
        if max_v < total:
            max_v = total
    # 열우선
    for j in range(N):
        total = 0
        for i in range(N):
            total += arr[i][j]
        if max_v < total:
            max_v = total
    # \
    total = 0
    for i in range(N):
        total += arr[i][i]
    if max_v < total:
        max_v = total

    # /
    total = 0
    for i in range(N):
        total += arr[i][N-1-i]

    if max_v < total:
        max_v = total

    print(f'#{tc} {max_v}')