import sys;sys.stdin = open('배열최소합_input.txt')
def perm(n, k, sum):
    global ans
    if ans < sum : return
    #######################
    if n == k:
        # print(p, end=' ')
        # sum = 0
        # for i in range(n):
        #     sum += arr[i][p[i]]
        # print(sum)
        if ans > sum: ans = sum

    else:
        for i in range(k, n):
            p[k], p[i] = p[i], p[k]
            perm(n, k+1, sum + arr[k][p[k]])
            p[k], p[i] = p[i], p[k]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    p = list(range(N))
    ans = 987654321
    perm(N, 0, 0)
    print(f'#{tc} {ans}')