import sys; sys.stdin = open('부분집합의합_input.txt')
arr = list(range(1, 13))
n = len(arr)
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())

    ans = 0
    for i in range(1<<n):
        sum = cnt = 0
        for j in range(n):
            if i & (1 << j):  # i의 비트열을 확인
                cnt += 1
                sum += arr[j]
        if cnt == N and sum == K:
            ans += 1
    print(f'#{tc} {ans}')