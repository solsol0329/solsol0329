import sys; sys.stdin = open('회문_input.txt')
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(str, input())) for _ in range(N)]
    # arr = [input() for _ in range(N)]

    print(f'#{tc}', end=' ')
    # 행방향
    for i in range(N):
        for j in range(N-M+1):
            flag = 1
            for k in range(M//2):
                if arr[i][j+k] != arr[i][j+M-1-k]:
                    flag = 0
                    break
            if flag == 1:
                for k in range(M):
                    print(arr[i][j+k], end='')
                print()

    # 열방향
    for i in range(N):
        for j in range(N - M + 1):
            flag = 1
            for k in range(M // 2):
                if arr[j + k][i] != arr[j + M - 1 - k][i]:
                    flag = 0
                    break
            if flag == 1:
                for k in range(M):
                    print(arr[j + k][i], end='')
                print()