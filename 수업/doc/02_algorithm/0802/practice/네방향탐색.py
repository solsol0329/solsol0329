import sys; sys.stdin = open('네방향탐색_input.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    sum_total = 0       # 전체합
    for i in range(N):
        for j in range(N): # 이중for문 2차원 순회
            sum_sub = 0 # 각원소의 4방향 차의 합
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0<=ni<N and 0<=nj<N: # 인덱스체크
                    # 절대값 구하기
                    rst = arr[i][j] - arr[ni][nj]
                    if rst < 0: rst = -rst
                    sum_sub += rst
            sum_total += sum_sub
    print(f'#{tc} {sum_total}')