import sys; sys.stdin = open('가장빠른문자열타이핑_input.txt')
T = int(input())
for tc in range(1, T+1):
    A, B = map(str, input().split())
    N = len(A)
    M = len(B)

    cnt = 0
    i = 0 # 초기화
    while i < N-M+1 :# 조건
        flag = 1
        for j in range(M):
            if A[i+j] != B[j]:
                flag = 0
                break
        if flag:
            cnt += 1
            i += M - 1   # 검색어만큼 이동
        i += 1 # 증감

    print(f'#{tc} {N-M*cnt+cnt}')