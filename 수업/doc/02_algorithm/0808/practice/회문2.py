import sys; sys.stdin = open('회문2_input.txt')
def row_max(arr, N):
    M = N
    while M > 0:
        for i in range(N):
            for j in range(N-M+1):
                flag = 1
                for k in range(M//2):
                    if arr[i][j+k] != arr[i][j+M-1-k]:
                        flag = 0
                        break
                if flag:
                    return M
        M -= 1


def col_max(arr, N):
    M = N
    while M > 0:
        for i in range(N):
            for j in range(N-M+1):
                flag = 1
                for k in range(M//2):
                    if arr[j+k][i] != arr[j+M-1-k][i]:
                        flag = 0
                        break
                if flag:
                    return M
        M -= 1

N = 100
T = 10
for tc in range(1, T+1):
    no = int(input())
    #arr = [list(input()) for _ in range(N)]
    arr = [list(map(str, input())) for _ in range(N)]

    r_max = row_max(arr, N)
    c_max = col_max(arr, N)

    ans = 0
    if r_max > c_max:
        ans = r_max
    else:
        ans = c_max

    print(f'#{tc} {ans}')
