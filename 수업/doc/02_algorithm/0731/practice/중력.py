import sys; sys.stdin = open('중력_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 1차원 배열 입력
    arr = list(map(int, input().split()))
    # print(arr)
    ans = 0
    for i in range(N):  # len(arr)
        # i위치에서 최대낙차값 : N - 1 -i : 9 - 1 = 8
        max_h = N - 1 - i
        # i 이후의 모든 상자의 높이와 비교
        for j in range(i+1, N):
            if arr[i] <= arr[j]:
                max_h -= 1
        #최대값을 유지
        if ans < max_h:
            ans = max_h
    print(f'#{tc} {ans}')
