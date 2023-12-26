import sys; sys.stdin = open('동철이의일분배_input.txt')
def perm(n, k, curmax):
    global ans
    if ans >= curmax: return

    if n == k :
        if ans < curmax: ans = curmax
        return
    else:
        for i in range(n):
            if visited[i] == 0:
                visited[i] = 1
                P[k] = A[i]
                perm(n, k+1, curmax * (arr[k][P[k]] * 0.01))   # arr[k][i]
                visited[i] = 0



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    A = list(range(N))  # 순열의 입력
    P = [0] * N         # 순열의 결과
    ans = 0
    perm(N, 0, 1)
    print(f'#{tc} {ans * 100:.6f}')
    # print("#%d %.6f" % (tc, ans * 100))