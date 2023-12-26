import sys; sys.stdin = open('파리퇴치_input.txt')
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0
    for r in range(N-M+1):
        for c in range(N-M+1):
            sum_v = 0  # 파리채에 죽은 파리수
            for i in range(M):
                for j in range(M):
                    sum_v += arr[r+i][c+j]
            if max_v < sum_v:
                max_v = sum_v
    print(f'#{tc} {max_v}')