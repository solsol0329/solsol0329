import sys; sys.stdin = open('최소비용_input.txt')

import heapq
def dijkstra(x, y):
    # 1. 시작점 설정
    heap = []
    D[x][y] = 0
    heapq.heappush(heap, (D[x][y], x, y))   # 가중치, x, y
    # 2. 정점갯수 반복(N * N)
    while heap:
    # for _ in range(N*N):
        # 2-1. 최소값
        # min_v = INF
        # for i in range(N):
        #     for j in range(N):
        #         if visited[i][j] == 0 and min_v > D[i][j]:
        #             min_v = D[i][j]
        #             x, y = i, j
        d, x, y = heapq.heappop(heap)
        # 2-2. 방문체크 + 할일
        visited[x][y] = 1
        if x == N-1 and y == N-1: return
        # 2-3. 인접정점(4)의 가중치 갱신
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 인접하고 방문 안한 정점
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                diff = 0  # 경사도
                if arr[nx][ny] > arr[x][y]:
                    diff = arr[nx][ny] - arr[x][y]
                #업데이트
                if D[nx][ny] > D[x][y] + 1 + diff:
                    D[nx][ny] = D[x][y] + 1 + diff
                    heapq.heappush(heap, (D[nx][ny], nx, ny))


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
INF = 987654321
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]# 경사도행렬
    D = [[INF] * N for _ in range(N)]  # 가중치
    visited = [[0] * N for _ in range(N)] # 방문체크

    dijkstra(0, 0)
    print(f'#{tc} {D[N-1][N-1]}')