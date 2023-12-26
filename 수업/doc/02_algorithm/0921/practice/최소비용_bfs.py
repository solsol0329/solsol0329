import sys; sys.stdin = open('최소비용_input.txt')

def bfs(N):
    D[0][0] = 0
    q = []              # 소비량이 갱신된 지역의 인접 지역 저장용
    q.append((0, 0))

    while q:            # 더이상 갱신되는 경우가 없을 때까지 반복
        x, y = q.pop(0)
        for i in range(4):
            nx = x + dx[i]  # 이동할 인접 칸 좌표
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:  # 유효한 범위면
                diff = 0
                if arr[nx][ny] > arr[x][y]:  # 오르막일때
                    diff = arr[nx][ny] - arr[x][y]
                if D[nx][ny] > D[x][y] + 1 + diff:  # 갱신
                    D[nx][ny] = D[x][y] + 1 + diff
                    q.append((nx, ny))  # 주변도 갱신될 수 있으므로 저장

    return D[N - 1][N - 1]


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
INF = 987654321
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]  # 각 지역의 높이 정보
    D = [[INF] * N for i in range(N)]  # 각 칸 까지의 최소 연료 소비량

    print(f'#{tc} {bfs(N)}')
