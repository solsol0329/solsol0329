import sys; sys.stdin = open('화물도크_input.txt')
def cmp(x):
    return x[1], x[0]

T =  int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr.sort(key=lambda x: (x[1], x[0]))
    # arr.sort(key=cmp)

    finish = ans = 0            # 앞 작업의 종료시간, 정답
    for i in range(N):          # 모든 작업에 대해서
        if finish <= arr[i][0]: # 앞 작업 이후에 시작하면
            ans += 1
            finish = arr[i][1]
    print(f'#{tc} {ans}')