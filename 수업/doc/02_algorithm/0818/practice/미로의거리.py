import sys; sys.stdin = open('미로의거리_input.txt')
def start_pos():
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                return i, j

def bfs(x, y):
    Q = [(x, y)]
    visited[x][y] = 1
    while Q:
        x, y = Q.pop(0)
        if arr[x][y] == 3:
            return visited[x][y]-2
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N \
                and visited[nx][ny] == 0 \
                and arr[nx][ny] != 1:
                Q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
    return 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    x, y = start_pos()
    print(f'#{tc} {bfs(x, y)}')