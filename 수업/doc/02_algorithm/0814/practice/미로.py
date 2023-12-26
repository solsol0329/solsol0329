import sys; sys.stdin = open('미로_input.txt')
def dfs(x, y):
    global flag
    #  방문체크
    visited[x][y] = 1
    if arr[x][y] == 3:
        flag = 1
        return
    # 시작정점과 인접하고 미방문 정점 -> 재귀호출
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0 \
            and (arr[nx][ny] == 0 or arr[nx][ny] == 3):
            dfs(nx, ny)


def find_pos(arr):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                return i, j

dx = [-1,1,0,0]
dy = [0,0,-1,1]
T = int(input())
for tc in range(1, T+1):
    flag = 0
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    sx, sy = find_pos(arr)
    dfs(sx, sy)
    print(f'#{tc} {flag}')