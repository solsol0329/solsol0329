import sys; sys.stdin = open('숫자카드_input.txt', 'r')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input()))

    # 카운팅
    counts = [0] * 10
    for i in range(N):
        counts[arr[i]] += 1

    # 최대값의 인덱스
    max_idx = 0
    for i in range(1, 10):
        if counts[max_idx] <= counts[i]:
            max_idx = i
    print(f'#{tc} {max_idx} {counts[max_idx]}')