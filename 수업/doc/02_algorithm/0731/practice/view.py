import sys; sys.stdin = open('view_input.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    ans = 0
    for i in range(2, N-2):
        # i-2, i-1, i+1, i+2 최대값
        max_v = 0
        for j in range(5):
            if j != 2:
                if max_v < arr[i-2+j]:
                    max_v = arr[i-2+j]
        # 좌우2개의 최대값이 기준값보다 작은 경우 조망권 확보
        if arr[i] > max_v:
            ans += arr[i] - max_v
    print(f'#{tc} {ans}')