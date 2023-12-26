import sys; sys.stdin = open("색칠하기_input.txt")
T = int(input())
for tc in range(1, T+1):
    # 10 X 10 배열 0으로 초기화
    arr = [[0] * 10 for _ in range(10)]

    n = int(input())   # 색칠할 횟수
    for _ in range(n): # 좌상단, 우하단 좌표 입력
        r1, c1, r2, c2, color = map(int, input().split())
        # 색칠하기
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                arr[i][j] += color

    # print()
    # for lst in arr:
    #     print(*lst)
    # print()
    # 겹쳐진 칸수 카운팅
    cnt = 0
    for i in range(10):
        for j in range(10):
            if arr[i][j] == 3:
                cnt += 1

    print(f'#{tc} {cnt}')