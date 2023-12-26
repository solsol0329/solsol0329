import sys; sys.stdin = open("단순이진암호_input.txt", "r")

code = [[[[[[[0 for _ in range(2)] for _ in range(2)] for _ in range(2)] \
           for _ in range(2)] for _ in range(2)] for _ in range(2)] for _ in range(2)]

code[0][0][0][1][1][0][1] = 0
code[0][0][1][1][0][0][1] = 1
code[0][0][1][0][0][1][1] = 2
code[0][1][1][1][1][0][1] = 3
code[0][1][0][0][0][1][1] = 4
code[0][1][1][0][0][0][1] = 5
code[0][1][0][1][1][1][1] = 6
code[0][1][1][1][0][1][1] = 7
code[0][1][1][0][1][1][1] = 8
code[0][0][0][1][0][1][1] = 9


def find_pos():
    for i in range(N):
        for j in range(M - 1, -1, -1):
            if arr[i][j] == 1:
                return (i, j)


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input())) for _ in range(N)]
    # 뒤에서 끝나는 위치찾기(1)
    sx, sy = find_pos()
    # 시작위치로 이동
    for i in range(8):
        sy -= 7
    sy += 1
    # 암호 찾기
    pwd = []  # 암호코드
    for i in range(8):
        pwd.append(
            code[arr[sx][sy]][arr[sx][sy + 1]][arr[sx][sy + 2]][arr[sx][sy + 3]] \
                [arr[sx][sy + 4]][arr[sx][sy + 5]][arr[sx][sy + 6]]
        )
        sy += 7
    # 검증
    odd = pwd[0] + pwd[2] + pwd[4] + pwd[6]
    even = pwd[1] + pwd[3] + pwd[5] + pwd[7]
    # 출력
    if (odd * 3 + even) % 10 == 0:
        print(f'#{tc} {sum(pwd)}')
    else:
        print(f'#{tc} 0')
