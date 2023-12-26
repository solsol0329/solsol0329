import sys; sys.stdin = open('전기카트_input.txt')
def calc(cursum) :
    global ans
    # total = 0
    # for i in range(N):
    #     total += dist[p[i]][p[i+1]]
    # ans = min(ans, total)
    cursum += dist[p[N-1]][p[N]]  # 0-1-2 까지만 포함 2-0까지 추가
    ans = min(ans, cursum)

def perm(n, k, cursum):
    if ans < cursum: return   # 가지치기

    if n == k:
        calc(cursum)
    else:
        for i in range(n):
            if v[i] == 0:
                v[i] = 1
                p[k] = A[i]
                perm(n, k+1, cursum + dist[p[k-1]][p[k]])
                v[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    dist = [list(map(int, input().split())) for _ in range(N)]

    A = list(range(N))
    p = [0] * N + [0]     # 0 1 2 0 으로 저장(출발, 도착 고정)
    v = [0] * N
    v[0] = 1              # 0번은 제외

    ans = 987654321
    perm(N, 1, 0)
    print(f'#{tc} {ans}')